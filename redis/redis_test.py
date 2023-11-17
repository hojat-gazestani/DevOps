#!/usr/bin/python3

import time
import redis
import concurrent.futures


start = time.perf_counter()

r = redis.Redis(host='192.168.56.51', port=6379, decode_responses=True)

def do_something(count):
    print(f'Doing {count} ...')
    r.get('foo')
    return(f'Done {count}')

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = executor.map(do_something, range(99999999999))

    for result in results:
        print(result)

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
