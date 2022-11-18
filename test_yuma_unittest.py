import unittest
from yuma import *

class TestYuma(unittest.TestCase):
    def test_runyuma(self):
        self.assertEqual(runyuma(ADMINKGET),True,'\n\tyumabot startup failed...\n')
        
if __name__ == '__main__':
    unittest.main()