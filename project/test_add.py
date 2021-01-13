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


class AddTest(unittest.TestCase):
	"""
    Test Suite for pandas.Series.add

	Return Addition of series and other, element-wise (binary operator add).
	Equivalent to series + other, but with support to substitute a fill_value for missing data in either one of the inputs.

	Sig:  Series.add(other, level=None, fill_value=None, axis=0)
    Pre:
    Post:
	Parameters:
		other
			Series or scalar value
		fill_value = None or float value, default None (NaN)
			Fill existing missing (NaN) values, and any new element needed for successful Series alignment, with this value before computation. 
			If data in both corresponding Series locations is missing the result of filling (at that location) will be missing.
		levelint or name
			Broadcast across a level, matching Index values on the passed MultiIndex level.
	Returns: 
		Series The result of the operation.
	Ex:   
	
    """
	logger = logging.getLogger('AddTest')
	a = pd.Series([1, 1,      1, np.nan], index=['a', 'b', 'c', 'd'])
	b = pd.Series([1, np.nan, 1, np.nan], index=['a', 'b', 'd', 'e'])
	#c = pd.Series([1, np.nan, 1, np.nan],[1, np.nan, 1, np.nan], index=['a', 'b', 'd', 'e'])
	scalar = 1.0
	fill = 0.0
	
	def test_add_series(self):
		ret = self.a.add(self.b, fill_value = self.fill)
		pd.testing.assert_series_equal(ret,pd.Series([2.0, 1.0, 1.0, 1.0 , np.nan], index=['a', 'b', 'c', 'd','e']))
		
	def test_add_scalar(self):
		self.a.add(self.scalar)
		# we expect a to be = 2.0, 2.0, 2.0, 1.0

	def test_add_nan(self):
		self.a.add(np.nan, fill_value = self.fill)
		# we expect a to be  = 1.0 1.0 1.0 0.0

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    unittest.main()






