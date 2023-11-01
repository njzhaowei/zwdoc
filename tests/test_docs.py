# -*- coding: utf-8 -*-
import pytest

def setup_module():
    teardown_module()

def teardown_module():
    # remove temp files
    pass

# [DEF_CFG]
DEF_CFG = {
    # [DEF_CFG_1]
    'http_success_only': False,
    # [DEF_CFG_1]

    'thread_num': 5,
    'thread_timeout': 6,    # seconds

    # [DEF_CFG_2]
    'cookiespath': None
    # [DEF_CFG_2]
}
# [DEF_CFG]

@pytest.fixture(scope='module')
def ga():
    # create obj before all test
    obj = 1
    yield obj
    # clean obj after all test done
    obj = 2

@pytest.mark.parametrize(
    'arg, result', (
        ('arg1', 'arg1ret'),
        ('arg2', 'arg2ret'),
    )
)
def test_func(ga, arg, result):
    """desc
    `Sphinx reStructuretext docs <https://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html>`_
    
    see :class:`Workbook` class

    :param str arg1: AAA
    :param arg2: BBB
    :type arg2: dict{str, int}
    :return: None
    :rtype: None or str
    :raise ValueError: raises ValueError exception.

    .. code-block:: Python
        :linenos:

        test_docs(111, 222)
    
    let's show some code::

        >>> from openpyxl import Workbook
        >>> wb = Workbook()

    .. note::

        inner shell::

        $ pip install abc

        inner code

        .. code-block:: Python
            :linenos:
            
            import abc

        ref link `lxml`_ library
    
    .. warning::

        this is warning

    ref code and jump to source code see :ref:`TEST_SOURCE_CODE`
    
    .. literalinclude:: /../../tests/test_docs.py
        :caption: Default config value
        :name: TEST_DEF_CFG
        :language: python
        :start-after: [DEF_CFG]
        :end-before: [DEF_CFG]

    .. literalinclude:: /../../tests/test_docs.py
        :caption: Source Code
        :name: TEST_SOURCE_CODE
        :language: python
        :pyobject: test_func
    
    .. _lxml: http://lxml.de
    """
    assert ga == 1
    assert arg+'ret' == result