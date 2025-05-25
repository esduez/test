import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from py.analyzer import analyze_package

def test_package_analysis():
    result = analyze_package("flask")
    assert isinstance(result, dict)
    assert "dependencies" in result
    assert isinstance(result["dependencies"], list)

def test_invalid_package():
    with pytest.raises(Exception):
        analyze_package("invalid_package_123")
