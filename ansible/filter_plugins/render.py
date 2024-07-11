from jinja2 import Environment

def subrender_filter(value, variables):
  ''' Print value and pass it on unchanged '''
  if type(value) is list:
    for index, item in enumerate(value):
      value[index] = subrender_filter(item, variables)
  else:
    _template = Environment().from_string(value)
    return _template.render(variables)

  return value


class FilterModule(object):
  ''' Render string as Jinja2 template module '''

  def filters(self):
    return {
      'render': subrender_filter
    }
