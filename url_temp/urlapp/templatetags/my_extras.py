from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
    '''
    This method is to add filters
    '''
    return value.replace(arg,'')

#register.filter('cut',cut)
