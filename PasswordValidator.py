

"""
My python password validator
"""

# imports go here
import inspect
import csv

__author__ = 'Kobe Haukap'
__version__ = '1.0'
__date__ ='2023.04.06'
__status__ = 'development'

class PasswordException(Exception):


class PasswordValidator:

    __UPPERCASE_MIN = 2
    __LOWERCASE_MIN = 2
    __DIGIT_MIN = 2
    __SYMBOL_MIN = 2

    def __init__(self, password=None, debug_mode=False):

        self.__password = password
        self.__debug_mode = debug_mode

    def __str__(self):

        if self.__password is None:
            return "None"
        else:
            return self.__password

    def __is_uppercase_valid(self):

        count = sum(1 for char in self.__password if char.isupper())

        if self.__debug_mode:
            print(f"{count:3d} = {inspect.currentframe().f_code.co_name}")

        if count >= 2:
            True
        else:
            print(f"Password must have at least {PasswordValidator.__UPPERCASE_MIN} uppercase letters.")
            return False

    def __is_lowercase_valid(self):

        count = sum(1 for char in self.__password if char.islower())

        if self.__debug_mode:
            print(f"{count:3d} = {inspect.currentframe().f_code.co_name}")

        if count >= 2:
            True
        else:
            print(f"Password must have at least {PasswordValidator.__LOWERCASE_MIN} lowercase letters.")
            return False

    def __is_digit_valid(self):

        count = sum(1 for char in self.__password if char.isupper())

        if self.__debug_mode:
            print(f"{count:3d} = {inspect.currentframe().f_code.co_name}")

        if count >= 2:
            True
        else:
            print(f"Password must have at least {PasswordValidator.__DIGIT_MIN} digits.")
            return False

    def __is_symbol_valid(self):

        count = sum(1 for char in self.__password if char.isupper())

        if self.__debug_mode:
            print(f"{count:3d} = {inspect.currentframe().f_code.co_name}")

        if count >= 2:
            True
        else:
            print(f"Password must have at least {PasswordValidator.__SYMBOL_MIN} special characters.")
            return False

    def is_valid(self, password=None):

        if password is None:
            raise Exception("Password cannot be empty.")

        self.__password = password

        if self.__debug_mode:
            print("==============DEBUG MODE================")
            print(self)

        uppercase_valid = self.__is_uppercase_valid()
        lowercase_valid = self.__is_lowercase_valid()
        digit_valid = self.__is_digit_valid()
        symbol_valid = self.__is_symbol_valid()

        if uppercase_valid:
            return True
        else:
            return False

        if lowercase_valid:
            return True
        else:
            return False

        if digit_valid:
            return True
        else:
            return False

        if symbol_valid:
            return True
        else:
            return False


pv = PasswordValidator(debug_mode=False)

if pv.is_valid("aA"):
    print("Valid Password")
else:
    print("Invalid Password")
