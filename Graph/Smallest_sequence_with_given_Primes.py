#https://pythonexample.com/code/smallest-sequence-with-given-primes-interviewbit/
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @return a list of integers
    def solve(self, A, B, C, D):
        ans = []
        lst = set()
        lst.add(A)
        lst.add(B)
        lst.add(C)
        
        for i in range(D):
            Min = min(lst)
            ans.append(Min)
            lst.add(Min * A)
            lst.add(Min * B)
            lst.add(Min * C)
            lst.remove(Min)
        return ans
