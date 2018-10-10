import unittest
from N_max_pair_combinations import *

class test_N_max_pair_combinations(unittest.TestCase):
    def test_solve(self):
        t_1 = Solution()
        r_1 = t_1.solve([6, 7], [6, 7])
        self.assertEqual(r_1, [14, 13])
        
        t_2 = Solution()
        r_2 = t_2.solve([1,4,2,3], [2,5,1,6])
        self.assertEqual(r_2, [10, 9, 9, 8])
        
        t_3 = Solution()
        r_3 = t_3.solve([3], [2])
        self.assertEqual(r_3, [5])
        
if __name__ =='__main__':
    unittest.main()
