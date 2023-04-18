
"""
My python password validator
"""

# imports
import inspect
import PasswordException as pe

# metadata for authorship information
__author__ = 'Kobe Haukap'
__version__ = '1.0'
__date__ ='2023.04.06'
__status__ = 'development'


class PasswordValidator:

    UPPERCASE_MIN = 2  # minimum number of uppercase letters required
    LOWERCASE_MIN = 2  # minimum number of lowercase letters required
    DIGIT_MIN = 2   # minimum number of digits required
    SYMBOL_MIN = 2  # minimum number of symbols required

    def __init__(self, debug_mode=False):
        """

        :param debug_mode:
        """

        self.password = 'unknown'  # initializes users password
        self.debug_mode = debug_mode  # initializes debug mode
        self.errors = []  # initializes list to append errors to

    def __str__(self):
        """

        :return: None
        """
        return self.password

    def __validate_uppercase(self):
        """
        Validates number of uppercase letters in password.
        :return: None
        """

        # counts the number of uppercase letters in password
        count = sum(1 for char in self.password if char.isalpha() and char.isupper())

        # displays the character type and the character count
        if self.debug_mode:
            print(inspect.currentframe().f_code.co_name, '=', count)

        # raises error if uppercase requirement not met
        if count < PasswordValidator.UPPERCASE_MIN:
            raise pe.PasswordException(self.password, 'uppercase', PasswordValidator.UPPERCASE_MIN, count)

    def __validate_lowercase(self):
        """
        Validates number of lowercase letters in password.
        :return: None
        """

        # counts the number of lowercase letters in password
        count = sum(1 for char in self.password if char.isalpha() and char.islower())

        # displays the character type and the character count
        if self.debug_mode:
            print(inspect.currentframe().f_code.co_name, '=', count)

        # raises error if lowercase requirement not met
        if count < PasswordValidator.LOWERCASE_MIN:
            raise pe.PasswordException(self.password, 'lowercase', PasswordValidator.LOWERCASE_MIN, count)

    def __validate_digit(self):
        """
        Validates number of digits in password.
        :return: None
        """

        # counts the number of digits in password
        count = sum(1 for char in self.password if char.isdigit())

        # displays the character type and the character count
        if self.debug_mode:
            print(inspect.currentframe().f_code.co_name, '=', count)

        # raises error if digit requirement is not met
        if count < PasswordValidator.DIGIT_MIN:
            raise pe.PasswordException(self.password, 'digit', PasswordValidator.DIGIT_MIN, count)

    def __validate_symbol(self):
        """
        Validates number of symbols in password
        :return: None
        """

        # counts number of symbols in password
        count = sum(1 for char in self.password if not char.isdigit() and not char.isalpha())

        # displays the character type and the character count
        if self.debug_mode:
            print(inspect.currentframe().f_code.co_name, '=', count)

        # raises error is symbol requirement is not met
        if count < PasswordValidator.SYMBOL_MIN:
            raise pe.PasswordException(self.password, 'symbol', PasswordValidator.SYMBOL_MIN, count)

    def is_valid(self, password):
        """
        Displays debug mode, validates all characters in the password,
        and appends any errors to list.

        :param password: users password
        :return: None
        """

        self.password = password

        self.errors.clear()

        # displays debug mode and displays password
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


# tests multiple passwords and prints whether they are valid or not
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


