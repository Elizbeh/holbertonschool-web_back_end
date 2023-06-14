#!/usr/bin/env python3
"""
Mocking a property
"""

import unittest
from client import GithubOrgClient
from unittest.mock import patch, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """
    Unit tests for the GithubOrgClient class.
    """

    def test_public_repos_url(self):
        """
        Test case to verify the behavior of the _public_repos_url property.
        The test mocks the GithubOrgClient.org property and verifies that the
        _public_repos_ur property returns the expected URL based on the
        mocked payload.
        """
        mock_payload = {
                'repos_url': 'https://api.github.com/orgs/google/repos'
                }
        expected_result = mock_payload['repos_url']

        with patch(
                'client.GithubOrgClient.org', new_callable=PropertyMock,
                return_value=mock_payload
                ):
            client = GithubOrgClient('Google')
            result = client._public_repos_url
            self.assertEqual(result, expected_result)
