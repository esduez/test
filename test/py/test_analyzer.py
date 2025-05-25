import pytest
import sys
import os

# Mutlak yol ayarı
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from py.analyzer import analyze_package

class TestAnalyzer:
    def test_analysis(self):
        result = analyze_package("flask")
        assert isinstance(result, dict)
        assert "dependencies" in result
        
    def test_invalid_package(self):
        with pytest.raises(Exception):
            analyze_package("invalid_package_123")
