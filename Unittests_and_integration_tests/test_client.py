#!/usr/bin/env python3
"""
Mocking a property
"""

from typing import List
import requests


class GithubOrgClient:
    """
    Class to interact with the GitHub API for an organization
    """

    def __init__(self, org_name: str) -> None:
        self._org_name = org_name
        self._base_url = f'https://api.github.com/orgs/{org_name}'

    def org(self) -> dict:
        """
        Method to get organization information
        """
        response = self._get(f'{self._base_url}')
        return response.json()

    def public_repos_url(self) -> str:
        """
        Property to get the public repositories URL of the organization
        """
        return f'{self._base_url}/repos'

    def _get(self, url: str) -> requests.Response:
        """
        Helper method to send GET requests
        """
        response = requests.get(url)
        response.raise_for_status()
        return response

