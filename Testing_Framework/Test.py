import os
import pandas
from openpyxl import load_workbook
from unittest.mock import patch, MagicMock
from unittest import mock
import pytest
import importlib
import sys

parameters=[]
#confirming Testing.xlsx file path and sheet
script_dir = os.path.dirname(os.path.abspath(__file__))
full_path = os.path.join(script_dir, "Test_Data.csv")
#read data from csv
data = pandas.read_csv(full_path, header = 0)
S_No = data['S.No'].values
Fun_name = data['Function_Name'].values
Param_dict = {}
for col in data.columns:
    if 'Param' in col:
        Param_dict[col] = list(data[col].values)
    else:
        pass
Exp_result = data['Expected_Result'].values
Testing_script_name = data['Test_Script'].values
Testing_class_name = data['Class_Name'].values

for i in S_No:
    if Param_dict:
        tup = (S_No[i-1], Fun_name[i-1])
        for key in Param_dict.keys():
            tup = tup + (Param_dict[key][i-1],)
        tup = tup + (Exp_result[i-1],)
        parameters.append([tup])
    else:
        parameters.append([(S_No[i-1], Fun_name[i-1], Exp_result[i-1])])

# @pytest.fixture
# def mockios():
#     #mocking argument parser for HC script
#     test_args = [Testing_script_name[0]]
#     with mock.patch.object(sys, 'argv', test_args):
#         test_script = importlib.import_module(Testing_script_name[0])
#         if Testing_class_name:
#             imported_class = getattr(test_script, Testing_class_name[0])
#         else:
#             pass
    
#     #patching the constructor to do nothing
#     with patch.object(imported_class, '_init_', return_value=None):
#         obj = imported_class()
#         #Manually set required attributes
#         obj = MagicMock()
#         return obj

decorater_parameter_names = ""
for col in data:
    if "Test_Script" not in col and "Class_Name" not in col:
        decorater_parameter_names+=','+col
    else:
        pass
    
# print(parameters[-1][])

# # calling all paramaters for testing
# @pytest.mark.parametrize(getattr(decorater_parameter_names), parameters)
# def test_policy(sno, function, param, test_output, result):
#     return_result = getattr(mock_ios, param) (param, filters, test_output)
#     assert return_result == parameters[-1]
#     # mock_ios.add_ecm.assert_called_once()
    # called_param, called_result = mock_ios.add_ecm.call_args[0]
         