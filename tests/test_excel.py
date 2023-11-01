# -*- coding: utf-8 -*-
import pytest
from . import *
from zwdoc.excel import Excel

def setup_module():
    teardown_module()

def teardown_module():
    pass

@pytest.fixture(scope='module')
def o():
    with Excel() as obj:
        yield obj

def test_open(o):
    assert o.path is None
    o.path = Path(BASE_PATH) / 'test_excel.xlsx'
    o.save()
    assert fileexist(o.path)

def test_sheets(o):
    assert o.sheet_count == 1
    o.create_sheet()
    assert o.sheet_count == 2 and o[1].title == f'New Sheet {o.sheet_count}'
    o.create_sheet('My Sheet')
    assert o.sheet_count == 3 and o['My Sheet'] is not None
    assert len(o.sheets) == o.sheet_count