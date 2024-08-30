#!/usr/bin/env python3

import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient
from parameterized import parameterized
from client import get_json


class TestGithubOrgClient(unittest.TestCase):
    """Test methods inside GithubOrgClient class"""
    @parameterized.expand([
        ('google', {'status': 200}),
        ('abc', {'status': 201})
    ])
    def test_org(self, org_name, expected):
        """test  the org method inside GithubOrgClient class,
        with a mocked response"""
        with patch(
                'client.get_json', return_value=expected) as get_mock:

            client = GithubOrgClient(org_name)
            full_url = client.ORG_URL.format(org=org_name)

            self.assertEqual(client.org, expected)
            get_mock.assert_called_once_with(full_url)

    @parameterized.expand([
        ('google', {'repos_url': 'https://www.google.co.uk/'}),
        ('abc', {'repos_url': 'https://abc.com/'})
    ])
    def test_public_repos_url(self, org_name, expected):
        """create a fake url and test it"""
        with patch.object(
                GithubOrgClient, 'org', new_callable=PropertyMock) as get_mock:

            client = GithubOrgClient(org_name)
            get_mock.return_value = expected
            self.assertEqual(client._public_repos_url, expected['repos_url'])

# new_callable=PropertyMock:
# This tells patch.object to create a mock specifically for a property.

    @patch('client.get_json')  # Step 1: Mock the get_json function
    def test_public_repos(self, get_mock):
        """follow the steps, carefully"""
        repos = [  # Step 2: Define the fake repository data
            {'name': 'google'},
            {'name': 'abc'}
        ]
        get_mock.return_value = repos
        # Step 3: Set the mock to return this data

        with patch.object(
                GithubOrgClient, '_public_repos_url', new_callable=PropertyMock
                ) as mock_url:
            mock_url.return_value = 'https://www.google.co.uk/'
            # Step 4: Mock the _public_repos_url property

            client = GithubOrgClient('google')
            # Create an instance of GithubOrgClient
            result = client.public_repos()
            # Call the public_repos method

            self.assertEqual(result, ['google', 'abc'])
            # Step 5: Check if the result matches the expected list
            mock_url.assert_called_once()
            # Ensure _public_repos_url was called exactly once
            get_mock.assert_called_once_with('https://www.google.co.uk/')
            # Ensure get_json was called with the correct URL

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """check if has licence or not"""
        client = GithubOrgClient('admin')
        self.assertEqual(client.has_license(repo, license_key), expected)


# Use @patch as a decorator to mock get_json
# Use patch as a context manager to mock
