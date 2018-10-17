class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def twoSum(self, A, B):
        n = len(A)
        if 1 < n:
            value_index = {}
            for i in range(n):
                if A[i] not in value_index:
                    if B - A[i] not in value_index:
                        value_index[A[i]] = i+1
                    else:
                        return value_index[B - A[i]],  i+1
                
                else:
                    if B - A[i] in value_index:
                        return  value_index[B - A[i]], i+1
        return []
