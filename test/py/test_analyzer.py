import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from py.analyzer import analyze_package

class TestAnalyzer(unittest.TestCase):
    def test_flask_analysis(self):
        result = analyze_package("flask")
        self.assertIn("dependencies", result)

if __name__ == '__main__':
    unittest.main()
