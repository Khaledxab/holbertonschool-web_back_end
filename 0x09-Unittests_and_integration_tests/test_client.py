#!/usr/bin/env python3
""" Parameterize patch as decorators with making property
and more patching, Integration tests """
import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from urllib.error import HTTPError


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
    def test_public_repos(self, test_input, mock_property, mock_get):
        """ test that the method returns what it is supposed to """
        test_client = GithubOrgClient(test_input)
        result = test_client.public_repos()
        self.assertEqual(result, mock_get.return_value)
        mock_property.assert_called_once()
        mock_get.assert_called_once_with(mock_property.return_value)

    """ to test the function for following inputs """
    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected, test_input):
        """ test that the method returns what it is supposed to """
        test_client = GithubOrgClient("khaledxab")
        result = test_client.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ TESTCASE """

    @classmethod
    def setUpClass(cls):
        """ APImethod to return example payload """

        cls.get_patcher = patch('requests.get', side_effect=HTTPError)

    @classmethod
    def tearDownClass(cls):
        """ API method to stop the patcher"""

        cls.get_patcher.stop()

    def test_public_repos(self):
        """ test githubOrgClient.public_repos"""

        test_class = GithubOrgClient("khaledxab")
        assert True

    def test_public_repos_with_license(self):
        """ test githubOrgClient.public_repos_with_license"""

        test_class = GithubOrgClient("khaledxab")
        assert True
