import os
import pandas
from openpyxl import load_workbook
from unittest.mock import patch, MagicMock
from unittest import mock
import pytest
import importlib
import sys
import re

#confirming Testing.xlsx file path and sheet
script_dir = os.path.dirname(os.path.abspath(__file__))
full_path = os.path.join(script_dir, "Test_Data.csv")

#read data from csv
data = pandas.read_csv(full_path, header = 0)

#collect Data in individual variables
S_No = data['S.No'].values
Fun_name = data['Function_Name'].values
Param_dict = {}
for col in data.columns:
    if 'Param' in col:
        pl = []
        for i in data[col]:
            pl.append(i)  
        Param_dict[col] = pl
    else:
        pass
    for i in data['Class_Name']:
        if pandas.isnull(i):
            Testing_class_name = None
        else:
            Testing_class_name = data['Class_Name'].values
            
Exp_result = data['Expected_Result'].values
Testing_script_name = data['Test_Script'].values

#create parameter list to pass in test function
parameters=[]
for i in S_No:
    if Param_dict:
        tup = (S_No[i-1].item(), Fun_name[i-1])
        for key in Param_dict.keys():
            if pandas.isnull(Param_dict[key][i-1]):
                pass
            else:
                tup = tup + (Param_dict[key][i-1],)
        tup = tup + (Exp_result[i-1].item(),)
        parameters.append(tup)
    else:
        parameters.append((S_No[i-1].item(), Fun_name[i-1], Exp_result[i-1].item()))

#ficture to bybass argParser and initialize constructor of class if needed
@pytest.fixture
def mock_fun():
    #mocking argument parser for HC script
    test_args = [Testing_script_name[0]]
    with mock.patch.object(sys, 'argv', test_args):
        test_script = importlib.import_module(Testing_script_name[0])
        if len(Testing_class_name)>0:
            imported_class = getattr(test_script, Testing_class_name[0])
        else:
            imported_class = None
    if imported_class:
        #patching the constructor to do nothing
        with patch.object(imported_class, '__init__',return_value=None):
            if imported_class.__init__:
                obj = imported_class()
            else:
                obj = imported_class
            # Manually set required attributes
            # example if a function does something with value provided trhough a external source just do obj.<fun_name> = MagicMock()
            return obj
    else:
        return test_script

#loop to check each entry in parameter list and run test according to no of Parameters of function
for p in parameters:
    # executes for 0 parameters
    if len(p) == 3:
        decorater_parameter_names = ""
        for col in data:
            if col =="Test_Script":
                break
            elif col == 'S.No':
                decorater_parameter_names += 'S_No'+','
            elif 'Param' in col:
                pass
            else:
                decorater_parameter_names += col+','
        decorater_parameter_names = decorater_parameter_names.removesuffix(',')
        # calling all paramaters for testing
        @pytest.mark.parametrize(decorater_parameter_names, [p])
        def test_function1(mock_fun, S_No, Function_Name, Expected_Result):
            return_result = getattr(mock_fun, Function_Name)()
            assert return_result == Expected_Result    
    
    # executes for 1 parameters
    elif len(p) == 4:
        decorater_parameter_names = ""
        for col in data:
            if col =="Test_Script":
                break
            elif col == 'S.No':
                decorater_parameter_names += 'S_No'+','
            elif 'Param2' in col:
                pass
            else:
                decorater_parameter_names += col+','
        decorater_parameter_names = decorater_parameter_names.removesuffix(',')
        # calling all paramaters for testing
        @pytest.mark.parametrize(decorater_parameter_names, [p])
        def test_function2(mock_fun, S_No, Function_Name, Param1, Expected_Result):
            return_result = getattr(mock_fun, Function_Name)(Param1)
            assert return_result == Expected_Result    
    
    # executes for 2 parameters
    elif len(p) == 5:
        decorater_parameter_names = ""
        for col in data:
            if col =="Test_Script":
                break
            elif col == 'S.No':
                decorater_parameter_names += 'S_No'+','
            elif 'Param3' in col:
                pass
            else:
                decorater_parameter_names += col+','
        decorater_parameter_names = decorater_parameter_names.removesuffix(',')
        # calling all paramaters for testing
        @pytest.mark.parametrize(decorater_parameter_names, [p])
        def test_function3(mock_fun, S_No, Function_Name, Param1, Param2, Expected_Result):
            return_result = getattr(mock_fun, Function_Name)(Param1, Param2)
            assert return_result == Expected_Result     
    
    # executes for 3 parameters
    elif len(p) == 6:
        decorater_parameter_names = ""
        for col in data:
            if col =="Test_Script":
                break
            elif col == 'S.No':
                decorater_parameter_names += 'S_No'+','
            elif 'Param4' in col:
                pass
            else:
                decorater_parameter_names += col+','
        decorater_parameter_names = decorater_parameter_names.removesuffix(',')
        # # calling all paramaters for testing
        @pytest.mark.parametrize(decorater_parameter_names, [p])
        def test_function4(mock_fun, S_No, Function_Name, Param1, Param2, Param3, Expected_Result):
            return_result = getattr(mock_fun, Function_Name)(Param1, Param2, Param3)
            assert return_result == Expected_Result   
    
    # executes for 4 parameters
    elif len(p) == 7:
        decorater_parameter_names = ""
        for col in data:
            if col =="Test_Script":
                break
            elif col == 'S.No':
                decorater_parameter_names += 'S_No'+','
            elif 'Param4' in col:
                pass
            else:
                decorater_parameter_names += col+','
        decorater_parameter_names = decorater_parameter_names.removesuffix(',')
        # # calling all paramaters for testing
        @pytest.mark.parametrize(decorater_parameter_names, [p])
        def test_function4(mock_fun, S_No, Function_Name, Param1, Param2, Param3, Param4, Expected_Result):
            return_result = getattr(mock_fun, Function_Name)(Param1, Param2, Param3, Param4)
            assert return_result == Expected_Result      

    # executes for 5 parameters
    elif len(p) == 8:
        decorater_parameter_names = ""
        for col in data:
            if col =="Test_Script":
                break
            elif col == 'S.No':
                decorater_parameter_names += 'S_No'+','
            elif 'Param4' in col:
                pass
            else:
                decorater_parameter_names += col+','
        decorater_parameter_names = decorater_parameter_names.removesuffix(',')
        # # calling all paramaters for testing
        @pytest.mark.parametrize(decorater_parameter_names, [p])
        def test_function4(mock_fun, S_No, Function_Name, Param1, Param2, Param3, Param4, Param5, Expected_Result):
            return_result = getattr(mock_fun, Function_Name)(Param1, Param2, Param3, Param4, Param5)
            assert return_result == Expected_Result 
    
    # executes for 6 parameters
    elif len(p) == 9:
        decorater_parameter_names = ""
        for col in data:
            if col =="Test_Script":
                break
            elif col == 'S.No':
                decorater_parameter_names += 'S_No'+','
            elif 'Param4' in col:
                pass
            else:
                decorater_parameter_names += col+','
        decorater_parameter_names = decorater_parameter_names.removesuffix(',')
        # # calling all paramaters for testing
        @pytest.mark.parametrize(decorater_parameter_names, [p])
        def test_function4(mock_fun, S_No, Function_Name, Param1, Param2, Param3, Param4, Param5, Param6, Expected_Result):
            return_result = getattr(mock_fun, Function_Name)(Param1, Param2, Param3, Param4, Param5, Param6)
            assert return_result == Expected_Result
            
    # executes for 7 parameters
    elif len(p) == 10:
        decorater_parameter_names = ""
        for col in data:
            if col =="Test_Script":
                break
            elif col == 'S.No':
                decorater_parameter_names += 'S_No'+','
            elif 'Param4' in col:
                pass
            else:
                decorater_parameter_names += col+','
        decorater_parameter_names = decorater_parameter_names.removesuffix(',')
        # # calling all paramaters for testing
        @pytest.mark.parametrize(decorater_parameter_names, [p])
        def test_function4(mock_fun, S_No, Function_Name, Param1, Param2, Param3, Param4, Param5, Param6, Param7, Expected_Result):
            return_result = getattr(mock_fun, Function_Name)(Param1, Param2, Param3, Param4, Param5, Param6, Param7)
            assert return_result == Expected_Result
            