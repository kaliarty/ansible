from ansible.errors import AnsibleFilterError, AnsibleFilterTypeError

def debug_print(value):
    ''' Print value and pass it on unchanged '''
    print("DEBUG: {}".format(value))
    return value

class FilterModule(object):
    ''' Monitoring rules processing filters '''

    def filters(self):
        return {
            'dprint': debug_print
        }
