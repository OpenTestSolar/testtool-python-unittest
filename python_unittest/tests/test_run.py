import os
import json
from pathlib import Path

from testsolar_testtool_sdk.file_reader import read_file_test_result
from testsolar_testtool_sdk.model.test import TestCase
from src.run import run_testcases_from_args

testdata_dir: str = str(Path(__file__).parent.absolute().joinpath("testdata"))


def test_run_all_testcases():
    with open(os.path.join(testdata_dir, "test_entry.json"), "w") as f:
        content = {
            "TaskId": "aa",
            "ProjectPath": testdata_dir,
            "FileReportPath": testdata_dir,
            "Collectors": [],
            "Context": {},
            "TestSelectors": [
                "."
            ]
        }
        json.dump(content, f)
        
    run_testcases_from_args(
        args=["run.py", Path.joinpath(Path(testdata_dir), "test_entry.json")],
        workspace=testdata_dir,
    )

    re = read_file_test_result(Path(testdata_dir), case=TestCase(Name="tests/testdata/test_demo01/test_demo03.py?MyTest03/test_05"))
    assert re.Test.Name
    assert re.ResultType
    assert re.Steps
    assert re.StartTime
    assert re.EndTime
    
    re = read_file_test_result(Path(testdata_dir), case=TestCase(Name="tests/testdata/test_demo01/test_demo03.py?MyTest03/test_06"))
    assert re.Test.Name
    assert re.ResultType
    assert re.Steps
    assert re.StartTime
    assert re.EndTime
    
    re = read_file_test_result(Path(testdata_dir), case=TestCase(Name="tests/testdata/test_demo01/test_demo04.py?MyTest01/test_01"))
    assert re.Test.Name
    assert re.ResultType
    assert re.Steps
    assert re.StartTime
    assert re.EndTime
    
    re = read_file_test_result(Path(testdata_dir), case=TestCase(Name="tests/testdata/test_demo01/test_demo04.py?MyTest01/test_02"))
    assert re.Test.Name
    assert re.ResultType
    assert re.Steps
    assert re.StartTime
    assert re.EndTime
    
    re = read_file_test_result(Path(testdata_dir), case=TestCase(Name="tests/testdata/test_demo02.py?MyTest02/test_03"))
    assert re.Test.Name
    assert re.ResultType
    assert re.Steps
    assert re.StartTime
    assert re.EndTime
    
    re = read_file_test_result(Path(testdata_dir), case=TestCase(Name="tests/testdata/test_demo02.py?MyTest02/test_04"))
    assert re.Test.Name
    assert re.ResultType
    assert re.Steps
    assert re.StartTime
    assert re.EndTime
        

def test_run_file():
    with open(os.path.join(testdata_dir, "test_entry.json"), "w") as f:
        content = {
            "TaskId": "aa",
            "ProjectPath": testdata_dir,
            "FileReportPath": testdata_dir,
            "Collectors": [],
            "Context": {},
            "TestSelectors": [
                "test_demo02.py"
            ]
        }
        json.dump(content, f)
        
    run_testcases_from_args(
        args=["run.py", Path.joinpath(Path(testdata_dir), "test_entry.json")],
        workspace=testdata_dir,
    )

    re = read_file_test_result(Path(testdata_dir), case=TestCase(Name="tests/testdata/test_demo02.py?MyTest02/test_03"))
    assert re.Test.Name
    assert re.ResultType
    assert re.Steps
    assert re.StartTime
    assert re.EndTime
    
    re = read_file_test_result(Path(testdata_dir), case=TestCase(Name="tests/testdata/test_demo02.py?MyTest02/test_04"))
    assert re.Test.Name
    assert re.ResultType
    assert re.Steps
    assert re.StartTime
    assert re.EndTime
        
def test_run_dir():
    with open(os.path.join(testdata_dir, "test_entry.json"), "w") as f:
        content = {
            "TaskId": "aa",
            "ProjectPath": testdata_dir,
            "FileReportPath": testdata_dir,
            "Collectors": [],
            "Context": {},
            "TestSelectors": [
                "test_demo01"
            ]
        }
        json.dump(content, f)
        
    run_testcases_from_args(
        args=["run.py", Path.joinpath(Path(testdata_dir), "test_entry.json")],
        workspace=testdata_dir,
    )

    re = read_file_test_result(Path(testdata_dir), case=TestCase(Name="tests/testdata/test_demo01/test_demo03.py?MyTest03/test_05"))
    assert re.Test.Name
    assert re.ResultType
    assert re.Steps
    assert re.StartTime
    assert re.EndTime
    
    re = read_file_test_result(Path(testdata_dir), case=TestCase(Name="tests/testdata/test_demo01/test_demo03.py?MyTest03/test_06"))
    assert re.Test.Name
    assert re.ResultType
    assert re.Steps
    assert re.StartTime
    assert re.EndTime
    
    re = read_file_test_result(Path(testdata_dir), case=TestCase(Name="tests/testdata/test_demo01/test_demo04.py?MyTest01/test_01"))
    assert re.Test.Name
    assert re.ResultType
    assert re.Steps
    assert re.StartTime
    assert re.EndTime
    
    re = read_file_test_result(Path(testdata_dir), case=TestCase(Name="tests/testdata/test_demo01/test_demo04.py?MyTest01/test_02"))
    assert re.Test.Name
    assert re.ResultType
    assert re.Steps
    assert re.StartTime
    assert re.EndTime
        
def test_run_class():
    with open(os.path.join(testdata_dir, "test_entry.json"), "w") as f:
        content = {
            "TaskId": "aa",
            "ProjectPath": testdata_dir,
            "FileReportPath": testdata_dir,
            "Collectors": [],
            "Context": {},
            "TestSelectors": [
                "test_demo01/test_demo04.py?MyTest01"
            ]
        }
        json.dump(content, f)
        
    run_testcases_from_args(
        args=["run.py", Path.joinpath(Path(testdata_dir), "test_entry.json")],
        workspace=testdata_dir,
    )

    re = read_file_test_result(Path(testdata_dir), case=TestCase(Name="tests/testdata/test_demo01/test_demo04.py?MyTest01/test_01"))
    assert re.Test.Name
    assert re.ResultType
    assert re.Steps
    assert re.StartTime
    assert re.EndTime
    
    re = read_file_test_result(Path(testdata_dir), case=TestCase(Name="tests/testdata/test_demo01/test_demo04.py?MyTest01/test_02"))
    assert re.Test.Name
    assert re.ResultType
    assert re.Steps
    assert re.StartTime
    assert re.EndTime
        
def test_run_case():
    with open(os.path.join(testdata_dir, "test_entry.json"), "w") as f:
        content = {
            "TaskId": "aa",
            "ProjectPath": testdata_dir,
            "FileReportPath": testdata_dir,
            "Collectors": [],
            "Context": {},
            "TestSelectors": [
                "test_demo01/test_demo04.py?name=MyTest01/test_01"
            ]
        }
        json.dump(content, f)
        
    run_testcases_from_args(
        args=["run.py", Path.joinpath(Path(testdata_dir), "test_entry.json")],
        workspace=testdata_dir,
    )

    re = read_file_test_result(Path(testdata_dir), case=TestCase(Name="tests/testdata/test_demo01/test_demo04.py?MyTest01/test_01"))
    assert re.Test.Name
    assert re.ResultType
    assert re.Steps
    assert re.StartTime
    assert re.EndTime