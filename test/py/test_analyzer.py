import unittest
import sys
import os

# Kritik yol ayarı
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from py.analyzer import analyze_package

class TestAnalyzer(unittest.TestCase):
    def test_analysis(self):
        result = analyze_package("flask")
        self.assertIsInstance(result, dict)
        self.assertIn("dependencies", result)
        
if __name__ == '__main__':
    unittest.main()
