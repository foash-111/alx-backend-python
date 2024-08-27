#!/usr/bin/env python3

import unittest
from unittest.mock import patch
from client import GithubOrgClient
from parameterized import parameterized
from utils import get_json


class TestGithubOrgClient(unittest.TestCase):
    """Test methods inside GithubOrgClient class"""
    @parameterized.expand([
        ('https://www.google.co.uk/', {'status': 200}),
        ('https://abc.com/', {'status': 201})
    ])
    @patch.object(GithubOrgClient, 'org')
    def test_org(self, url, expected, get_mock):
        """test  the org method inside GithubOrgClient class,
        with a mocked response"""
        client = GithubOrgClient(url)
        get_mock.return_value = expected
        self.assertEqual(client.org(), expected)
        get_mock.assert_called_once()
