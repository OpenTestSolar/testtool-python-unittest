import json
import sys
from pathlib import Path
from typing import Optional, List

from dacite import from_dict
from testsolar_testtool_sdk.model.param import EntryParam

parent = str(Path(__file__).parent.resolve())
if parent not in sys.path:
    sys.path.append(parent)

from testsolar_python_unittest.collector import collect_testcases  # type: ignore  # noqa: E402


def collect_testcases_from_args(
    args: List[str], workspace: Optional[str] = None
) -> None:
    if len(args) != 2:
        raise SystemExit("Usage: python load.py <entry_file>")

    filename = args[1]

    with open(filename, "r") as f:
        entry = from_dict(data_class=EntryParam, data=json.loads(f.read()))
        if workspace:
            entry.ProjectPath = workspace
        collect_testcases(entry_param=entry)


if __name__ == "__main__":
    collect_testcases_from_args(sys.argv)
