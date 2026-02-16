import pytest
import homework1.src.task6 as t6

# Verify that the word count is accurate
def test_wordCount():
    assert t6.wordCount() == 104