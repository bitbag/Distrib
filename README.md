
# Distrib
# Distrib project

"""To_enable_redis_cache:
   1.pip install django-redis==3.8.3      #enable redis cache
   

   2.install redis-server
   

   3.modefy settings.py add below:
      CACHES = {
    'default': {
        'BACKEND': 'redis_cache.cache.RedisCache',
        'LOCATION': 'redis://192.168.2.157:6379/1',         #remember to change this ip_address and port, write in redis's second database
        "OPTIONS": {
            "CLIENT_CLASS": "redis_cache.client.DefaultClient",
              },
          },
      }
<<<<<<< HEAD
	  
      REDIS_TIMEOUT=7*24*60*60      
      CUBES_REDIS_TIMEOUT=60*60
      NEVER_REDIS_TIMEOUT=365*24*60*60

=======
      REDIS_TIMEOUT=7*24*60*60
      CUBES_REDIS_TIMEOUT=60*60
      NEVER_REDIS_TIMEOUT=365*24*60*60


>>>>>>> 52288767d9330800f3022c1726d642a7799d7635
   """
