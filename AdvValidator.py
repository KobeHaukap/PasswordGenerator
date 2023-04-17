
import PasswordValidator as PV
import PasswordException as PE
import inspect

__author__ = 'Kobe Haukap'
__version__ = '1.0'
__date__ ='2023.04.06'
__status__ = 'development'


class AdvValidator(PV.PasswordValidator):

    MIN_LIMIT = 8
    MAX_LIMIT = 30
    VALID_SYMBOLS = ('!', '@', '#', '*', '$')

    def __init__(self, debug_mode=False):
        super().__init__(debug_mode=False)

    def __validate_symbols(self):

        count = sum(1 for char in self.password if char in AdvValidator.VALID_SYMBOLS)

        if self.debug_mode:
            print(inspect.currentframe().f_code.co_name, '=', count)

        if count < super().SYMBOLS_MIN:
            raise PE.PasswordException(self.password, 'symbols', super().SYMBOLS_MIN, count)

    def __validate_min(self):

        count = len(self.password)

        if self.debug_mode:
            print(inspect.currentframe().f_code.co_name, '=', count)

        if count < AdvValidator.MIN_LIMIT:
            raise PE.PasswordException(self.password, 'min limit', AdvValidator.MIN_LIMIT, count)

    def __validate_max(self):

        count = len(self.password)

        if self.debug_mode:
            print(inspect.currentframe().f_code.co_name, '=', count)

        if count < AdvValidator.MAX_LIMIT:
            raise PE.PasswordException(self.password, 'max limit', AdvValidator.MAX_LIMIT, count)

    def is_valid(self, password):

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

