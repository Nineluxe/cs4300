import pytest
import homework1.src.task7 as t7

# Verify that only valid URLs are accepted
def test_isURL():
    assert t7.isURL("https://google.com")
    assert not t7.isURL("some random string")