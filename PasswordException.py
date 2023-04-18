# imports
import csv

# metadata for authorship information
__author__ = 'Kobe Haukap'
__version__ = '1.0'
__date__ ='2023.04.06'
__status__ = 'development'


class PasswordException(Exception):

    def __init__(self, password, error_type, min_required, count):
        """
        Creates a list and appends information to a .txt file.
        :param password: None
        :param error_type: None
        :param min_required: None
        :param count: None
        """

        # list that contains information used in .txt file
        self.log = {'password': password,
                    'error_type': error_type,
                    'min_required': min_required,
                    'count': count}

        # creates and opens a .txt file and writes the values of the list inside
        with open('password_log.txt', 'a', newline='\n') as csvfile:
            writer = csv.writer(csvfile, delimiter='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([password, error_type, min_required, count])