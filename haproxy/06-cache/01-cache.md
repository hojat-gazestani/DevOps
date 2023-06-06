# Cache

* __total-max-size:__ size in __RAM__ of the cache in __megabytes__. Its __maximum__ value is __4095__
* __max-object-size:__  maximum size of the __objects__ to be cached
  * __Must not__ be greater than an half of __"total-max-size"__
  * default __256th__
  * All objects with sizes __larger__ than "max-object-size" will __not be cached__
* __max-age:__ Define the maximum __expiration duration__
  * default value is __60 seconds__

```bash
defaults
    mode http
    timeout client 30s
    timeout connect 10s
    timeout server 30s

cacke It-cache
    total-max-size 50   # size in RAM of the cache in megabytes. max 4095
    max-object-size 12  # size of any object in byte
    max-age 5           # second
    

frontend Italy
    bind *:80
    mode http
    use_backend my_app

backend my_app
    http-request cache-use It-cache
    http-response cache-store It-cache
	server MyApp8010 192.168.56.22:8010
```