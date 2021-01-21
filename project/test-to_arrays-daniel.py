import numpy as np
import pandas as pd
import unittest

from pandas.core.internals.construction import to_arrays

class TestToArray(unittest.TestCase):

    def setUp(self):
        # no data ; with column names
        self.dict_noData_withCols = {
                                 'odd': [], 
                                 'even': [],
                                 'prime': []
                                }
        self.df_noData_withCols = pd.DataFrame(self.dict_noData_withCols)

        # data ; with column names
        self.dict_withData_withCols = {
                                     'odd': [1,3,5], 
                                     'even': [0,2,4],
                                     'prime': [2,3,5]
                                    }

        self.df_withData_withCols = pd.DataFrame(self.dict_withData_withCols)

    def assertTupleEqual(self, expected, actual):
        self.assertEqual(type(expected), type(actual))  # check they are the same type
        self.assertEqual(len(expected), len(actual))    # check they are the same length
        
        self.assertEqual(type(expected[0]), type(actual[0]))  # check if data arrays are the same type
        self.assertEqual(len(expected[0]), len(actual[0]))    # check if data arrays are the same length

        self.assertEqual(type(expected[1]), type(actual[1]))  # check if column arrays are the same type
        self.assertEqual(len(expected[1]), len(actual[1]))    # check if column arrays are the same length

        for i, arr in enumerate(actual[0]):
            np.testing.assert_array_equal(arr, expected[0][i])
            
        pd.testing.assert_index_equal(actual[1], expected[1])


    def test_df_noData_withCols(self):
        self.assertTupleEqual(to_arrays(self.df_noData_withCols,self.df_noData_withCols.columns),\
                            ([np.array([]), np.array([]), np.array([])], pd.Index(['odd', 'even', 'prime'], dtype='object')))

    def test_df_withData_withCols(self):
        self.assertTupleEqual(to_arrays(self.df_withData_withCols, self.df_withData_withCols.columns),\
                            ([np.array([1, 3, 5]), np.array([0, 2, 4]), np.array([2, 3, 5])], pd.Index(['odd', 'even', 'prime'], dtype='object')))

if __name__ == '__main__':
    unittest.main()
