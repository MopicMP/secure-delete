"""Tests for secure-delete."""

import pytest
from secure_delete import delete


class TestDelete:
    """Test suite for delete."""

    def test_basic(self):
        """Test basic usage."""
        result = delete("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            delete("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = delete(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
