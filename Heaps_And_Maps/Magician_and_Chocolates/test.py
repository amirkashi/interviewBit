import unittest
from Magician_and_Chocolates import *


class test_mgician_and_chocolates(unittest.TestCase):
    def test_nchoc(self):
        t_1 = Solution()
        r_1 = t_1.nchoc(3, [6, 5])
        self.assertEqual(r_1, 14)
        

if __name__ == '__main__':
    unittest.main()
