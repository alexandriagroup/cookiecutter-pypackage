#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

test_{{ cookiecutter.package_name }}
----------------------------------

Tests for `{{ cookiecutter.package_name }}` module.
"""
import pytest

from {{ cookiecutter.package_name }} import {{ cookiecutter.package_name }}


@pytest.fixture
def response():
    """Sample pytest fixture.
    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repo_name }}')
    pass


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument.
    """
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string
    pass
