import unittest
import random
from credit_card_validator import credit_card_validator

"""This file runs random testing unit tests for the credit_card_validator function
Assignment: HW3: Random Testing Hands On
Author: Flemicas
Date: 11/02/2026"""

# Visa
#   Prefix(es): 4
#   Length: 16
# MasterCard
#   Prefix(es): 51 through 55 and 2221 through 2720 
#   Length: 16
# American Express
#   Prefix(es): 34 and 37
#   Length: 15

def luhn_algo(card_num:str) ->int:
    reverse_num: list[int] = list(map(int, str(card_num)))
    doubled_num: list[int] = []
    result: int = 0
    checksum_digit: int = 0
    for i in range(len(reverse_num)):
        if ((i % 2)== 0):
            result = reverse_num[i]*2
            if (result > 9):
                result -= 9
            doubled_num.append(result)
        else:
            doubled_num.append(reverse_num[i])
        result = 0
    for num in doubled_num:
        result += num
    checksum_digit = (10-(result % 10)) % 10
    return card_num + str(checksum_digit)       

def generate_valid_MasterCard_range2() -> str:
    prefix:str = str(random.randint(2221, 2720))
    cardNumber:str = prefix
    for i in range(11):
        cardNumber += str(random.randint(0,9))
    validCardNumber = luhn_algo(cardNumber)
    return validCardNumber

def generate_invalid_MasterCard_range2() -> str:
    prefix:str = str(random.randint(2221, 2720))
    cardNumber:str = prefix
    for i in range(12):
        cardNumber += str(random.randint(0,9))
    return cardNumber

TESTS_TO_GENERATE:int = 100

class TestCase(unittest.TestCase):

    def test_valid_MasterCard_range2(self):
        # This test runs valid master cards in the 2221-2720 range
        for i in range(TESTS_TO_GENERATE):
            credit_card_validator(generate_valid_MasterCard_range2())

    def test_invalid_MasterCard_range2(self):
        # This test runs invalid master cards in the 2221-2720 range
        for i in range(TESTS_TO_GENERATE):
            credit_card_validator(generate_invalid_MasterCard_range2())


if __name__ == '__main__':
    unittest.main()
