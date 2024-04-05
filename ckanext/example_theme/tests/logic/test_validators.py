"""Tests for validators.py."""

import pytest

import ckan.plugins.toolkit as tk

from ckanext.example_theme.logic import validators


def test_example_theme_reauired_with_valid_value():
    assert validators.example_theme_required("value") == "value"


def test_example_theme_reauired_with_invalid_value():
    with pytest.raises(tk.Invalid):
        validators.example_theme_required(None)
