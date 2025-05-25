import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))]

class TestAnalyzer(unittest.TestCase):
    def test_dummy(self):
        self.assertEqual(1+1, 2)

if __name__ == '__main__':
    unittest.main()
