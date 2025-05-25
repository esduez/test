import pytest
import sys
import os

# Kritik yol ayarı (3 seviye yukarı çık)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from py.analyzer import analyze_package

def test_package_analysis():
    result = analyze_package("flask")
    assert isinstance(result, dict)
    assert "dependencies" in result
    assert isinstance(result["dependencies"], list)

def test_invalid_package():
    with pytest.raises(Exception):
        analyze_package("invalid_package_123")
