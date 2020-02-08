"""Module of unit tests for active-business module.

__author__ = 'Max Luckystar'
__email__ = 'data.maxluckystar@gmail.com'
__website__ = ''
__ copyright__ = 'Copyright 2020, Max Luckystar'
__version__ = '1.0'
"""

import unittest
from active_business import Event, find_active_businesses

# @classmethod
# def setUpClass(cls):
#     print('\nsetupClass')

# @classmethod
# def tearDownClass(cls):
#     print('\ntearDownClass\n')

# def setUp(self):
#     self.connection_posgtresql_1 = PostgreSqlDb(
#         'postgres', 'postgrespass', 'localhost', '5433', 'crm')
#     self.connection_posgtresql_2 = PostgreSqlDb(
#         'postgres', self.passw, 'localhost', '5433', 'crm')
#     print('\nsetUp **********************')

# def tearDown(self):
#     print('\ntearDown **********************\n\n\n')


class TestMain(unittest.TestCase):
    """Test Case for find_active_businesses.

    Arguments:
        unittest {TestCase} -- class TestCase from unittest module
    """

    def test_find_active_businesses(self):
        """Test_1.

        Result [2, 3] Test Pass
        """
        lines = [['ads', '7', '3'],
                 ['ads', '8', '2'],
                 ['ads', '5', '1'],
                 ['page_views', '11', '2'],
                 ['page_views', '12', '3'],
                 ['photo_views', '10', '3'],
                 ['reviews', '7', '2']]

        events = [Event(line[0], int(line[1]), int(line[2])) for line in lines]

        self.assertEqual(find_active_businesses(events), [2, 3])

    # def test_find_active_businesses(self):
    #     """Test_2.

    #     Result [2, 3] Test Pass
    #     """
    #     lines = [['ads', '7', '3'],
    #              ['ads', '8', '2'],
    #              ['ads', '5', '1'],
    #              ['page_views', '11', '2'],
    #              ['page_views', '12', '3'],
    #              ['photo_views', '10', '3'],
    #              ['reviews', '7', '2']]

    #  events = [Event(line[0], int(line[1]), int(line[2])) for line in lines]

    #     self.assertEqual(find_active_businesses(events), [2, 3])


if __name__ == "__main__":
    unittest.main()
