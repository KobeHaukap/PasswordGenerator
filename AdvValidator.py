# imports
import PasswordValidator as PV
import PasswordException as PE
import inspect

# metadata for authorship information
__author__ = 'Kobe Haukap'
__version__ = '1.0'
__date__ ='2023.04.06'
__status__ = 'development'


class AdvValidator(PV.PasswordValidator):

    MIN_LIMIT = 8  # minimum character limit for password
    MAX_LIMIT = 30  # maximum character limit for password
    VALID_SYMBOLS = ('!', '@', '#', '*', '$')  # valid symbols to use in password

    def __init__(self, debug_mode=False):
        super().__init__(debug_mode=False)

    def __validate_symbols(self):
        """
        Validates the symbols in the password.
        :return: None
        """

        count = sum(1 for char in self.password if char in AdvValidator.VALID_SYMBOLS)

        if self.debug_mode:
            print(inspect.currentframe().f_code.co_name, '=', count)

        if count < super().SYMBOLS_MIN:
            raise PE.PasswordException(self.password, 'symbols', super().SYMBOLS_MIN, count)

    def __validate_min(self):
        """
        Checks if password meets minimum character requirement.
        :return: None
        """

        count = len(self.password)

        if self.debug_mode:
            print(inspect.currentframe().f_code.co_name, '=', count)

        if count < AdvValidator.MIN_LIMIT:
            raise PE.PasswordException(self.password, 'min limit', AdvValidator.MIN_LIMIT, count)

    def __validate_max(self):
        """
        Checks if password meets maximum character requirement.
        :return: None
        """

        count = len(self.password)

        if self.debug_mode:
            print(inspect.currentframe().f_code.co_name, '=', count)

        if count < AdvValidator.MAX_LIMIT:
            raise PE.PasswordException(self.password, 'max limit', AdvValidator.MAX_LIMIT, count)

    def is_valid(self, password):
        """
        Validates all characters in password and appends
        errors to a list.
        :param password:
        :return: None
        """

        super().is_valid(password)

        try:
            self.__validate_symbols()
        except PE.PasswordException as e:
            self.errors.append(e)

        try:
            self.__validate_min()
        except PE.PasswordException as e:
            self.errors.append(e)

        try:
            self.__validate_max()
        except PE.PasswordEXception as e:
            self.errors.append(e)

