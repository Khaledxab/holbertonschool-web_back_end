#!/usr/bin/env python3
""" Parameterize patch as decorators with making property
and more patching """
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ TESTCASE """
    """ to test the function for following inputs """
    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json')
    def test_org(self, test_input, mock_get):
        """ test that the method returns what it is supposed to """
        test_client = GithubOrgClient(test_input)
        result = test_client.org
        self.assertEqual(result, mock_get.return_value)
        mock_get.assert_called_once_with(
            f'https://api.github.com/orgs/{test_input}')

    """ to test the function for following inputs """
    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, test_input, mock_property):
        """ test that the method returns what it is supposed to """
        test_client = GithubOrgClient(test_input)
        result = test_client._public_repos_url
        self.assertEqual(result, mock_property.return_value['repos_url'])
        mock_property.assert_called_once()

    """ to test the function for following inputs """
    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json')
    @patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock)
    def test_public_repos(self, test_input, mock_property, mock_get):
        """ test that the method returns what it is supposed to """
        test_client = GithubOrgClient(test_input)
        result = test_client.public_repos()
        self.assertEqual(result, mock_get.return_value)
        mock_property.assert_called_once()
        mock_get.assert_called_once_with(mock_property.return_value)

    """ to test the function for following inputs """
    @parameterized.expand([
        ({"license": {"key": "my_license"}}), ({}),
        ])
    def test_has_license(self, test_input, test_license):
        """ to unit-test GithubOrgClient.has_license """
        test_client = GithubOrgClient("test")
        result = test_client.has_license(test_input, test_license)
        self.assertEqual(result, test_license in test_input['license']['key'])
