from ansible.errors import AnsibleFilterError, AnsibleFilterTypeError

def comment_ports(ruleset, comment):
    ''' Walk allowed_tcp_ports, add comment to every port that doesn't have one '''

    for portdict in ruleset['allowed_tcp_ports']:
        if 'comment' not in portdict.keys():
            portdict['comment'] = comment
    return ruleset

class FilterModule(object):
    ''' Monitoring rules processing filters '''

    def filters(self):
        return {
            'comment_ports': comment_ports
        }
