"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""

from my_module.functions import remove_nans
from my_module.functions import choose_columns
from my_module.functions import summary_stats

import pandas as pd
from numpy import nan
##
##

def test_remove_nans():
    
    dummy_dataframe = pd.DataFrame(data = {'col1': [1, 2], 'col2': [nan, 4]})
    altered_dataframe = pd.DataFrame(data = {'col1': [2], 'col2': [4.0]})


    assert remove_nans(dummy_dataframe, "col1").equals(dummy_dataframe)
    assert isinstance(remove_nans(dummy_dataframe, "col1"), pd.DataFrame)
    assert remove_nans(dummy_dataframe, "col2").equals(altered_dataframe)
    
    

def test_choose_columns():
    dummy_dataframe = pd.DataFrame(data = {'col1': [1, 2], 'col2': [nan, 4]})
    altered_dataframe = pd.DataFrame(data = {'col1': [1, 2]})
    
    assert choose_columns(dummy_dataframe, 'col1', 'col2').equals(dummy_dataframe)
    assert isinstance(choose_columns(dummy_dataframe, 'col1'), pd.DataFrame)
    assert choose_columns(dummy_dataframe, 'col1').equals(altered_dataframe)
    

def test_summary_stats():
    dummy_dataframe = pd.DataFrame(data = {'Country':['US', 'Canada'], 'Value':[23, 345]})
    
    assert summary_stats(dummy_dataframe, 'Value')['Statistics'][0] == 345.0
    assert isinstance(summary_stats(dummy_dataframe, 'Value'), pd.DataFrame)
    assert len(summary_stats(dummy_dataframe, 'Value')) == 5



                 
    