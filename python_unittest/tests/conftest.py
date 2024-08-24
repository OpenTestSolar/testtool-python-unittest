import os
import glob
import pytest
import shutil
from .test_run import testdata_dir

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_sessionfinish(session, exitstatus):
    json_files = glob.glob(os.path.join(testdata_dir, '*.json'))
    
    for json_file in json_files:
        try:
            os.remove(json_file)
        except OSError as e:
            print(f"Error removing file {json_file} err: {e}")
    # 删除结果文件
    os.remove("test_results.xml")
    # 删除coverage文件
    shutil.rmtree(f"./testsolar_coverage")
    yield