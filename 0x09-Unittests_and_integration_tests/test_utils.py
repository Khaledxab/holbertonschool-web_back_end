#!/usr/bin/env python3
""" Parameter a unit test """
import unittest
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """ testcase """
    @parameterized.expand([
        ({'a': 1}, ('a',), 1),
        ({'a': {'b': 2}}, ('a',), {'b': 2}),
        ({'a': {'b': 2}}, ('a', 'b'), 2)
    ])
    def test_access_nested_map(self, nested_map, path, answer):
        """ test """
        self.assertEqual(access_nested_map(nested_map, path), answer)
