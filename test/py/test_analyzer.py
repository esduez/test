import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from py.analyzer import analyze_package

class TestAnalyzer(unittest.TestCase):
    def test_package_analysis(self):
        """Test if package analysis returns correct structure"""
        result = analyze_package("flask")
        self.assertIsInstance(result, dict)
        self.assertIn("dependencies", result)
        self.assertIn("tea_rewards", result)
        
    def test_invalid_package(self):
        """Test error handling for invalid packages"""
        with self.assertRaises(Exception):
            analyze_package("invalid_package_123")

if __name__ == '__main__':
    unittest.main()
