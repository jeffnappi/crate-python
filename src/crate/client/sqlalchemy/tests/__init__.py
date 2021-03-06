# -*- coding: utf-8 -*-

from unittest import TestSuite, makeSuite
from .connection_test import SqlAlchemyConnectionTest
from .dict_test import SqlAlchemyDictTypeTest
from .datetime_test import SqlAlchemyDateAndDateTimeTest
from .compiler_test import SqlAlchemyCompilerTest
from .update_test import SqlAlchemyUpdateTest
from .match_test import SqlAlchemyMatchTest


def test_suite():
    tests = TestSuite()
    tests.addTest(makeSuite(SqlAlchemyConnectionTest))
    tests.addTest(makeSuite(SqlAlchemyDictTypeTest))
    tests.addTest(makeSuite(SqlAlchemyDateAndDateTimeTest))
    tests.addTest(makeSuite(SqlAlchemyCompilerTest))
    tests.addTest(makeSuite(SqlAlchemyUpdateTest))
    tests.addTest(makeSuite(SqlAlchemyMatchTest))
    return tests
