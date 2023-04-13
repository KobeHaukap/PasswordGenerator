
import PasswordValidator
import PasswordException as PE
import inspect


class AdvValidator(PasswordValidator):

    __VALID_SYMBOLS = ('!', '@', '#', '*')

    def __init__(self, debug_mode=False):
        super().__init__(debug_mode=False)

    def __validate_symbols(self):

        count = sum(1 for char in self.__password if char in AdvValidator.__VALID_SYMBOLS)

        if self.__debug_mode:
            print(inspect.currentframe().f_code.co_name, '=', count)

        if count < super.UPPERCASE_MIN:
            raise PE.PasswordException(self.__password, 'uppercase', super.UPPERCASE_MIN, count)


