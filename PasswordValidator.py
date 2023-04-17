
"""
My python password validator
"""

# imports go here
import inspect
import PasswordException as pe

__author__ = 'Kobe Haukap'
__version__ = '1.0'
__date__ ='2023.04.06'
__status__ = 'development'


class PasswordValidator:

    UPPERCASE_MIN = 2
    LOWERCASE_MIN = 2
    DIGIT_MIN = 2
    SYMBOL_MIN = 2

    def __init__(self, debug_mode=False):

        self.password = 'unknown'
        self.debug_mode = debug_mode
        self.errors = []

    def __str__(self):
        return self.password

    def __validate_uppercase(self):

        count = sum(1 for char in self.password if char.isalpha() and char.isupper())

        if self.debug_mode:
            print(inspect.currentframe().f_code.co_name, '=', count)

        if count < PasswordValidator.UPPERCASE_MIN:
            raise pe.PasswordException(self.password, 'uppercase', PasswordValidator.UPPERCASE_MIN, count)

    def __validate_lowercase(self):

        count = sum(1 for char in self.password if char.isalpha() and char.islower())

        if self.debug_mode:
            print(inspect.currentframe().f_code.co_name, '=', count)

        if count < PasswordValidator.LOWERCASE_MIN:
            raise pe.PasswordException(self.password, 'lowercase', PasswordValidator.LOWERCASE_MIN, count)

    def __validate_digit(self):

        count = sum(1 for char in self.password if char.isdigit())

        if self.debug_mode:
            print(inspect.currentframe().f_code.co_name, '=', count)

        if count < PasswordValidator.DIGIT_MIN:
            raise pe.PasswordException(self.password, 'digit', PasswordValidator.DIGIT_MIN, count)

    def __validate_symbol(self):

        count = sum(1 for char in self.password if not char.isdigit() and not char.isalpha())

        if self.debug_mode:
            print(inspect.currentframe().f_code.co_name, '=', count)

        if count < PasswordValidator.SYMBOL_MIN:
            raise pe.PasswordException(self.password, 'symbol', PasswordValidator.SYMBOL_MIN, count)

    def is_valid(self, password):

        self.password = password

        self.errors.clear()

        if self.debug_mode:
            print("==============DEBUG MODE================")
            print("password =", self)

        try:
            self.__validate_uppercase()
        except pe.PasswordException as e:
            self.errors.append(e)

        try:
            self.__validate_lowercase()
        except pe.PasswordException as e:
            self.errors.append(e)

        try:
            self.__validate_digit()
        except pe.PasswordException as e:
            self.errors.append(e)

        try:
            self.__validate_symbol()
        except pe.PasswordException as e:
            self.errors.append(e)

        if len(self.errors) == 0:
            return True
        else:
            return False


pv = PasswordValidator(debug_mode=False)

if pv.is_valid("abACD15!@#"):
    print("Valid Password")
else:
    print("Invalid Password")

print()

if pv.is_valid("aaD$$#16663"):
    print("Valid Password")
else:
    print("Invalid Password")

print()

if pv.is_valid("ndDHT35#!"):
    print("Valid Password")
else:
    print("Invalid Password")

print()

if pv.is_valid("aA1!"):
    print("Valid Password")
else:
    print("Invalid Password")

print()


