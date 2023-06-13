#!/usr/bin/env python3
"""
Parameterize a unit test
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map,get_json
from unittest.mock import patch

class TestAccessNestedMap(unittest.TestCase):

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), KeyError('a')),
        ({"a": 1}, ("a", "b"), KeyError('b'))
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_exception):
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), str(expected_exception))

class TestGetJson(unittest.TestCase):

    @patch('utils.requests.get')
    def test_get_json(self, mock_get):
        test_url_1 = "http://example.com"
        test_payload_1 = {"payload": True}
        mock_get.return_value.json.return_value = test_payload_1

        result_1 = get_json(test_url_1)

        mock_get.assert_called_once_with(test_url_1)
        self.assertEqual(result_1, test_payload_1, "Expected: OK\nActual: Failed")

        test_url_2 = "http://holberton.io"
        test_payload_2 = {"payload": False}
        mock_get.return_value.json.return_value = test_payload_2

        result_2 = get_json(test_url_2)

        mock_get.assert_called_with(test_url_2)
        self.assertEqual(result_2, test_payload_2, "Expected: OK\nActual: Failed")
