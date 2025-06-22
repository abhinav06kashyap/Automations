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
param_data = {}
for col in data.columns:
    if 'Param' in col:
        param_data[col] = list(data[col].values)
    else:
        pass
Exp_result = data['Expected_Result'].values
Testing_script_name = data['Test_Sript'].values
Testing_class_name = data['Class_Name'].values

if param_data:
    print(param_data)
else:
    print("none")

@pytest.fixture
def mockios():
    #mocking argument parser for HC script
    test_args = [script_name]
    with mock.patch.object(sys, 'argv', test_args):
        test_script = importlib.import_module(script_name)
        imported_class = getattr(test_script, class_name)
    
    #patching the constructor to do nothing
    with patch.object(imported_class, '_init_', return_value=None):
        obj = imported_class("tech_spec_file.xlsx", generate_file=False)
        #Manually set required attributes
        obj.Debug = False
        obj.wbkName = "tech_spec_file.xlsx"
        obj.add_ecm = MagicMock()
        return obj
    
# Calling all paramaters for testing
@pytest.mark.parametrize('sno, param, filters, test_output, result', parameters)
def test_policy(mock_ios, sno, param, filters, test_output, result):
    return_result = getattr(mock_ios, param) (param, filters, test_output)
    assert return_result == True
    mock_ios.add_ecm.assert_called_once()
    called_param, called_result = mock_ios.add_ecm.call_args[0]
    assert called_param == param
    assert result.upper() in called_result.upper()
         