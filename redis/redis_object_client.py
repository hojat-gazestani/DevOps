#!/usr/bin/python3

import time
import redis
import concurrent.futures

start = time.perf_counter()

r = redis.Redis(host='192.168.56.51', port=6379, decode_responses=True)
sucess = 0
class Client():

    number_of_client = 0

    def __init__(self, count):
        self.id = count
        Client.number_of_client += 1

    def get_req(self):
        global sucess
        sucess += 1
        return(f'Doing {self.id} ...', r.get('foo'))

def Create_client(num):
    client = Client(num)
    print(client.get_req())

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = executor.map(Create_client, range(9))

    for result in results:
        print('this is resut:', result)

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)', "Number of client:", str(Client.number_of_client), "Sucess: ", sucess)
