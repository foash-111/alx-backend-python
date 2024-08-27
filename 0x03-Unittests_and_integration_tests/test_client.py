#!/usr/bin/env python3

import unittest
from unittest.mock import patch
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
