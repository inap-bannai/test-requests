import requests
import grequests
import threading
from functools import partial
from typing import List

from pprint import pprint
from random import seed
from random import random
import time


# seed random number generator
# https://machinelearningmastery.com/how-to-generate-random-numbers-in-python/
seed(1)

u = "http://slowwly.robertomurray.co.uk/delay/3000/url/http://google.co.uk"


def do_request(num: int) -> threading.Thread:
    def worker(num: int) -> None:
        # doesn't execute sequentially bc random length sleep.
        # time.sleep(random())
        result = requests.get(u)
        print(f"{num=}")
        pprint(result)

    t = threading.Thread(target=partial(worker, num=num))
    t.start()
    return t


def request_threads():
    thread_list: List[threading.Thread] = []
    for n in range(100):
        thread_list.append(do_request(num=n))

    for t in thread_list:
        t.join()


def execute_grequests():
    rs = (grequests.get(u) for u in [u] * 100)
    pprint(grequests.map(rs))


def main() -> None:
    start = time.time()
    request_threads()  # elapsed_time:21.476648092269897[sec]
    # execute_grequests()  # elapsed_time:31.84117317199707[sec]
    elapsed_time = time.time() - start
    print("elapsed_time:{0}".format(elapsed_time) + "[sec]")


if __name__ == "__main__":
    main()
