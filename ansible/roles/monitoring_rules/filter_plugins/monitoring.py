from ansible.errors import AnsibleFilterError, AnsibleFilterTypeError

def ruleset_to_prometheus(ruleset, **kwargs):
    ''' Walk all rules, set job names, generate targets from on_behalf and port '''
    
    ruleset = ruleset if isinstance(ruleset, list) else [ruleset]  # handle dicts and lists of dicts
    for rule in ruleset:
        if 'job_name' not in rule:
            rule['job_name'] = kwargs['job_name']
        if 'static_configs' not in rule:
            rule['static_configs'] = [{}]
        if not isinstance(rule['static_configs'], list):
            raise AnsibleFilterTypeError("static_configs must be a list. Failing rule: {}".format(rule))
        for config in rule['static_configs']:
            if 'targets' not in config:
                if 'port' not in rule:
                    raise AnsibleFilterError("Either port or targets must be present. None found in rule: {}".format(rule))
                if 'on_behalf' not in kwargs:
                        raise AnsibleFilterError("Wither 'on_behalf' or targets must be filled in. None found in rule: {}".format(rule))
                config['targets'] = [str(kwargs['on_behalf']) + ':' + str(rule['port'])]
        del rule['port']
    return ruleset


class FilterModule(object):
    ''' Monitoring rules processing filters '''

    def filters(self):
        return {
            'ruleset_to_prometheus': ruleset_to_prometheus
        }
