from ansible.errors import AnsibleFilterError, AnsibleFilterTypeError
import re
from datetime import datetime

def config_to_summary(item, **kwargs):
    ''' Generate a summary from an nginx_config item '''
    # Example data: see below
    endpoints = []
    upstreams = {} # maps upstream names to upstream servers' addresses
    for upstream in item["config"]["upstreams"]:
        name = upstream["name"]
        addresses = list(map(lambda s: s["address"], upstream["servers"]))
        upstreams[name] = addresses

    for server in item["config"]["servers"]:
        upstream_paths = {} # maps upstream names to list of listening URLs
        for location in server["locations"]:
            if "proxy" not in location.keys():
                continue
            upstream_name = re.search(r"https?://(.*)", location["proxy"]["pass"]).group(1)
            if not upstream_name in upstream_paths.keys():
                upstream_paths[upstream_name] = []
            # TODO: support multiple listeners per server
            port = server["core"]["listen"][0]["port"]
            url = (
                ('https://' if 'ssl' in server.keys() else 'http://') + 
                server["core"]["server_name"] +
                ('' if (str(port) == "80" or str(port) == "443") else ':' + str(server["core"]["listen"][0]["port"])) +
                location["location"]
            )
            upstream_paths[upstream_name].append(url)
        # generate summary item
        for upstream, paths in upstream_paths.items():
            endpoint = {
                "name": upstream,
                "urls": paths,
                "details": {
                    "access_logs": list(map(lambda x: x["path"], server["log"]["access"])),
                    "upstreams": upstreams[upstream]
                }
            }
            endpoints.append(endpoint)
    return endpoints


class FilterModule(object):
    ''' Monitoring rules processing filters '''

    def filters(self):
        return {
            'config_to_summary': config_to_summary
        }


# Example input (copied from Ansible):
#
#nginx_one_proxy_subscriptions_headers:
#  - field: Upgrade
#    value: $http_upgrade
#  - field: Connection
#    value: "upgrade"
#
#nginx_one_proxy_config:
#  template_file: http/default.conf.j2
#  deployment_location: /etc/nginx/conf.d/one.conf
#  config:
#    servers:
#      - core:
#          listen: "{{ nginx_listen_ssl }}"
#          server_name: "{{ nginx_hosts.one.hostname | default(omit) }}"
#          error_page: "{{ nginx_default_http_error_pages }}"
#        ssl:
#          certificate: "{{ nginx_cert_dir }}/{{ nginx_hosts.one.crt | default(omit) }}"
#          certificate_key: "{{ nginx_cert_dir }}/{{ nginx_hosts.one.crt_key | default(omit) }}"
#        log:
#          access:
#            - path: "/var/log/nginx/{{ nginx_hosts.one.hostname | default(omit) }}.access.log"
#              format: main
#        headers:
#          add_headers: "{{ nginx_headers }}"
#        proxy:
#          hide_header:
#            - X-Powered-By
#        locations: "{{ nginx_one_proxy_default_locations + nginx_default_webserver }}"
#    upstreams:
#      - name: keycloak
#        ip_hash: true
#        servers:
#          - address: "{{ keycloak.host }}:{{ keycloak.port }}"
#            weight: 1
#      - name: mmm-be
#        ip_hash: true
#        servers:
#          - address: "{{ mmm.host }}:{{ mmm.http_port }}"
#            weight: 1
#      - name: mmm-fe
#        ip_hash: true
#        servers:
#          - address: "{{ frontend.host }}:{{ frontend.http_port }}"
#            weight: 1
#
#nginx_one_proxy_default_locations:
#  - location: /
#    proxy:
#      pass: http://mmm-fe
#      set_header: "{{ nginx_proxy_headers }}"
#  - location: /auth
#    proxy:
#      pass: http://keycloak
#      set_header: "{{ nginx_proxy_headers }}"
#  - location: /graphql
#    proxy:
#      pass: http://mmm-be
#      set_header: "{{ nginx_proxy_headers }}"
#  - location: /actuator
#    rewrite:
#      return:
#        code: 403
#  - location: /subscriptions
#    proxy:
#      pass: http://mmm-be
#      http_version: "1.1"
#      set_header: "{{ nginx_one_proxy_subscriptions_headers + nginx_proxy_headers }}"