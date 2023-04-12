
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

    def __init__(self, password, error_type, min_required, count):
        self.log = {'password': password,
                    'error_type': error_type,
                    'min_required': min_required,
                    'count': count}
        with open('password_log.txt', 'a', newline='\n') as csvfile:
            writer = csv.writer(csvfile, delimiter='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([password, error_type, min_required, count])


class PasswordValidator:

    __UPPERCASE_MIN = 2
    __LOWERCASE_MIN = 2
    __DIGIT_MIN = 2
    __SYMBOL_MIN = 2

    def __init__(self, debug_mode=False):

        self.__password = 'unknown'
        self.__debug_mode = debug_mode
        self.__errors = []

    def __str__(self):
        return self.__password

    def __validate_uppercase(self):

        count = sum(1 for char in self.__password if char.isalpha() and char.isupper())

        if self.__debug_mode:
            print(inspect.currentframe().f_code.co_name, '=', count)

        if count < PasswordValidator.__UPPERCASE_MIN:
            raise PasswordException(self.__password, 'uppercase', PasswordValidator.__UPPERCASE_MIN, count)

    def __validate_lowercase(self):

        count = sum(1 for char in self.__password if char.isalpha() and char.islower())

        if self.__debug_mode:
            print(inspect.currentframe().f_code.co_name, '=', count)

        if count < PasswordValidator.__LOWERCASE_MIN:
            raise PasswordException(self.__password, 'lowercase', PasswordValidator.__LOWERCASE_MIN, count)

    def __validate_digit(self):

        count = sum(1 for char in self.__password if char.isdigit())

        if self.__debug_mode:
            print(inspect.currentframe().f_code.co_name, '=', count)

        if count < PasswordValidator.__DIGIT_MIN:
            raise PasswordException(self.__password, 'digit', PasswordValidator.__DIGIT_MIN, count)

    def __validate_symbol(self):

        count = sum(1 for char in self.__password if not char.isdigit() and not char.isalpha())

        if self.__debug_mode:
            print(inspect.currentframe().f_code.co_name, '=', count)

        if count < PasswordValidator.__SYMBOL_MIN:
            raise PasswordException(self.__password, 'symbol', PasswordValidator.__SYMBOL_MIN, count)

    def is_valid(self, password):
        self.__password = password

        if self.__debug_mode:
            print("==============DEBUG MODE================")
            print("password =", self)

        try:
            self.__validate_uppercase()
        except PasswordException as e:
            self.__errors.append(e)

        try:
            self.__validate_lowercase()
        except PasswordException as e:
            self.__errors.append(e)

        try:
            self.__validate_digit()
        except PasswordException as e:
            self.__errors.append(e)

        try:
            self.__validate_symbol()
        except PasswordException as e:
            self.__errors.append(e)

        if len(self.__errors) == 0:
            return True
        else:
            for e in self.__errors:
                print(f"Password must contain {e.log['min_required']} {e.log['error_type']} "
                      f"but yours only contained {e.log['count']}")
                return False


pv = PasswordValidator(debug_mode=False)

if pv.is_valid(""):
    print("Valid Password")
else:
    print("Invalid Password")

print()

if pv.is_valid(""):
    print("Valid Password")
else:
    print("Invalid Password")

print()

if pv.is_valid(""):
    print("Valid Password")
else:
    print("Invalid Password")

print()

if pv.is_valid(""):
    print("Valid Password")
else:
    print("Invalid Password")

print()


