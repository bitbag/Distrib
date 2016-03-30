from django.conf import settings
from django.core.cache import cache

def read_from_redis(self, playbook):
    key = playbook
    value = cache.get(key)
    if value == None:
        print 'value is null'
    else:
        print 'value is %s' value
    return  (key,value)
