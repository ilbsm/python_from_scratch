""" Most important modules in my recent work include math, itertools, BeautifulSoup, random, time."""

# 0. Introduction
""" In Python, the functions are packed into modules. The modules can be imported into the file with"""

import math
import requests
import time

""" You can also import specific functions, classes or even variables from the modules, using"""

from itertools import product, combinations
from bs4 import BeautifulSoup
from random import random, randint, shuffle

# 1. Math
""" 'Math' is a library of basic mathematical functions. """


def test_math():
    a = 2
    print(math.sqrt(2))
    print(math.log(2))
    print(math.sin(2))
    return


""" It is useful for basic calculations. For more complex things one usually uses NumPy library"""

# 2. Itertools

""" Library useful for any kind of combinations, permutations etc. For example, if you want to probe each pair of a
2D 5x5 grid you would do:"""


def test_combinations():
    for element in combinations(range(5), 2):
        print(list(element))
    return


""" Similarly, instead of a nested loop, you can use product, e.g. to write every 4-bit sequence:"""


def test_product():
    for element in product(range(2), 4):
        print(list(element))
    # you can also make it a Python list:
    return [list(element) for element in product(range(2), 4)]

# 3. Random


""" Random is basically a library for generating (pseudo) random numbers:"""


def generate_random():
    # you can make random number from the interval (0, 1)
    print(random)
    # or random int in the interval (a, b)
    print(randint(5, 10))
    # or shuffle existing list
    my_list = list(range(1,10))
    print(shuffle(my_list))
    return

# 4. Requests and BeautifulSoup


""" Requests is a library for downloading things from the web. Beautifull soup is a tool to analyze the HTML pages"""


def test_requests():
    # downloading the sit
    address = 'https://knotprot.cent.uw.edu.pl/view/1j85/A/'
    resp = requests.get(address)
    page_source = resp.text

    # parsing the text and getting the knotted core of 1j85
    soup = BeautifulSoup(page_source, 'html.parser')
    table = soup.find("table", {"class": "table table-hover table-condensed"})
    for row in table.findAll("tr"):
        cells = row.findAll("td")
        if len(cells) >= 7:
            knot = cells[4].text.strip()
            knotted_core = cells[6].text
            print("Knot: " + knot + "; knotted core length: " + cells[6].text)
    return

# 5. Time


""" Time is a library for time measurements. It is useful for timing your code."""


def test_time():
    print("Now is " + str(time.asctime(time.localtime(time.time()))))
    time.sleep(3)
    print("And 3 seconds later is " + str(time.asctime(time.localtime(time.time()))))


if __name__ == '__main__':
    test_time()
