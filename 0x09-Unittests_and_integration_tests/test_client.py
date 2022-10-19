#!/usr/bin/env python3
""" Parameterize patch as decorators """
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ test class """
    """ input to test the function """

    @parameterized.expand([
        ("google"),
        ("abc"),
        ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get):
        """ test that the method returns correct value """

        test_url = f"https://api.github.com/orgs/{org_name}"
        test_payload = {"payload": True}
        mock_get.return_value = test_payload
        result = GithubOrgClient(org_name)
        self.assertEqual(result.org, test_payload)
        mock_get.assert_called_once_with(test_url)
