import os
import glob
from pathlib import Path
import pytest
import shutil

testdata_dir: str = str(Path(__file__).parent.absolute().joinpath("testdata"))


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_sessionfinish(session, exitstatus):
    json_files = glob.glob(os.path.join(testdata_dir, "*.json"))

    for json_file in json_files:
        try:
            os.remove(json_file)
        except OSError as e:
            print(f"Error removing file {json_file} err: {e}")
    # 删除结果文件
    if os.path.exists("test_results.xml"):
        os.remove("test_results.xml")
    # 删除coverage文件
    coverage_path = os.path.join(testdata_dir, "testsolar_coverage")
    if os.path.exists(coverage_path):
        shutil.rmtree(coverage_path)
    yield
