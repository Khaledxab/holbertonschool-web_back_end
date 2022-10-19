#!/usr/bin/env python3
""" Parameterize patch as decorators with making property
and more patching """
import unittest
from unittest.mock import patch, PropertyMock
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

    def test_public_repos_url(self):
        """ test that the method returns correct value """
        test_payload = {"repos_url": "holberton"}
        with patch.object(GithubOrgClient, 'org', new_callable=property) as mock:
            mock.return_value = test_payload
            result = GithubOrgClient('holberton')
            self.assertEqual(result._public_repos_url, test_payload['repos_url'])

    @patch("client.get_json", return_value=[{"name": "holberton"}])
    def test_public_repos(self, mock_get):
        """ test that the method returns correct value """
        test_payload = [{"name": "holberton"}]
        with patch.object(GithubOrgClient, '_public_repos_url', new_callable=PropertyMock) as mock:
            test_client = GithubOrgClient("hoberton")
            test_return = test_client.public_repos()
            self.assertEqual(test_return, ["holberton"])
            mock_get.assert_called_once
