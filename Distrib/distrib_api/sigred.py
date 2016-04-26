from django.conf import settings
from django.core.cache import cache

def ReadFromRedis(self, playbook):
    key = playbook
    value = cache.get(key)
    if value == None:
        print 'value is null'
    else:
        print 'value is %s' value
    return  (key,value)

def WriteToRedis(request):
    dics = {}
    if request.method == 'POST':
        dics = eval(json.dumps(request.POST))
        try:
            for k,val in dics.items():
                print k,val
                if k != 'csrfmiddlewaretoken':
                    cache.set(k,val)
        except Exception,e:
            return render(request,'basex.html',{'sdf':dics})

def GetFromRedis(request,*args):
    dicc = {}
    for i in args:
        try:
            dicc[i] = cache.get(i)
        except Exception,e:
            return render(request,'basex.html',{'sdf':e})
    return render(request,'basex.html',{'sdf':dicc})
