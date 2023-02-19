import unittest

from task1 import *


class Tests(unittest.TestCase):
    def test_strategy1_input1(self):
        days = 5
        houses = 3
        schedule = [[1, 3],
                    [2, 5],
                    [5, 5]]
        noOfHouses = count_houses(schedule, days, houses)
        print(noOfHouses)
