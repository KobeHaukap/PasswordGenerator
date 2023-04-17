
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