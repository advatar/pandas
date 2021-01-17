#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Software Testing Project 
Team Number: X
Student Names: Alexander Sellström
'''

from typing import *  	# noqa
import unittest  		# noqa
import logging  		# noqa
import numpy as np
import pandas as pd

__all__ = []


class ToArraysTest(unittest.TestCase):
	"""
    
	Sig:  to_arrays(data, columns, coerce_float: bool = False, dtype: Optional[DtypeObj] = None)
    Pre:
    Post:
	Parameters:
		data 
		columns
		coerce_float
		dtype
	Returns: 
		arrays, columns
	Ex:   
	
	- ABCDataFrame
	- list/tuple of lists/tuples
	- list/tuple of abc.Mapping
	- list/tuple of ABCSeries
	- list/tuple of Categorical
	- np.ndarray
	- ABCSeries
	- Index
	- something else (perhaps set of tuple/list???)	

    """
	logger = logging.getLogger('ToArraysTest')

	a = pd.Series([1, 1,      1, np.nan], index=['a', 'b', 'c', 'd'])
	b = pd.Series([1, np.nan, 1, np.nan], index=['a', 'b', 'd', 'e'])
	#c = pd.Series([1, np.nan, 1, np.nan],[1, np.nan, 1, np.nan], index=['a', 'b', 'd', 'e'])
	scalar = 1.0
	fill = 0.0
	
	def test_dataframe(self):
		ret = self.a.add(self.b, fill_value = self.fill)
		pd.testing.assert_series_equal(ret,pd.Series([2.0, 1.0, 1.0, 1.0 , np.nan], index=['a', 'b', 'c', 'd','e']))
		
	def test_tuple_of_tuples(self):
		print("test_tuple_of_tuples")
		


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    unittest.main()






