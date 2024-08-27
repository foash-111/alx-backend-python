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
    def test_org(self, url, expected):
        client = GithubOrgClient(url)
        with patch.object(
                GithubOrgClient, 'org',
                return_value=expected) as get_mock:
            self.assertEqual(client.org(), expected)
            get_mock.assert_called_once()
