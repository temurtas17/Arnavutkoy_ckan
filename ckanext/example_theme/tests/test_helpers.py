"""Tests for helpers.py."""

import ckanext.example_theme.helpers as helpers


def test_example_theme_hello():
    assert helpers.example_theme_hello() == "Hello, example_theme!"
