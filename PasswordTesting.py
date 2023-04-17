
import PasswordException
import PasswordValidator

__author__ = 'Kobe Haukap'
__version__ = '1.0'
__date__ ='2023.04.06'
__status__ = 'development'


def display_errors(pw):

    print("Invalid Password")
    for e in pw.errors:
        print(f"{e.log['password']} Password must contain {e.log['min_required']} {e.log['error_type']}"
              f"but yours only contained {e.log['count']}")




