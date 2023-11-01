import pytest
import shutil
from pathlib import Path
from . import BASE_PATH

@pytest.fixture(scope='session',autouse=True)
def session_fixture():
    tmpdir = Path(BASE_PATH)
    tmpdir.mkdir(parents=True, exist_ok=True)
    yield
    shutil.rmtree(str(tmpdir), ignore_errors=True)