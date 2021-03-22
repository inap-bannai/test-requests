import requests
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


def do_request(num: int) -> threading.Thread:
    def worker(num: int) -> None:
        # doesn't execute sequentially bc random length sleep.
        # time.sleep(random())
        result = requests.get("http://slowwly.robertomurray.co.uk/delay/3000/url/http://google.co.uk")
        print(f"{num=}")
        pprint(result)

    t = threading.Thread(target=partial(worker, num=num))
    t.start()
    return t


def main() -> None:
    thread_list: List[threading.Thread] = []
    for n in range(10):
        thread_list.append(do_request(num=n))

    for t in thread_list:
        t.join()


if __name__ == "__main__":
    main()
