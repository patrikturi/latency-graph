import random
from multiprocessing.pool import ThreadPool
from time import sleep

from icmplib import ping

# TODO: handle exceptions/no internet
def get_latency_ms(address, request_id):
    response = ping(address, count=1, id=request_id, timeout=5)

    if response.packet_loss:
        return None
    return response.min_rtt


def ping_thread(address, request_id):
    return get_latency_ms(address, request_id)


pool = ThreadPool(processes=12)

x = pool.apply_async(ping_thread, ('google.com', 1))
print(x.ready())
sleep(1)
print(x.ready())
print(x.get())
