class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def fourSum(self, A, B):
        n = len(A)
        if n < 4:
            return []
        else:
            Hash = {}
            result = []
            for i in range(0, n):
                for j in range(i+1, n):
                    Sum = A[i] + A[j]
                    diff = B - Sum
                    if diff in Hash and Sum not in Hash:
                        Hash[Sum] = [(i, j)]
                        for indexes in Hash[diff]:
                            if i not in indexes and j not in indexes:
                                ans = [A[i], A[j], A[indexes[0]], A[indexes[1]]]
                                ans.sort()
                                if ans not in result:
                                    result.append(ans)
                    
                    elif diff in Hash and Sum in Hash:
                        Hash[Sum].append((i, j))
                        for indx_Sum in Hash[Sum]:
                            for indx_diff in Hash[diff]:
                                if indx_Sum[0] not in indx_diff and indx_Sum[1] not in indx_diff:
                                    ans = [A[indx_Sum[0]], A[indx_Sum[1]], A[indx_diff[0]], A[indx_diff[1]] ]
                                    ans.sort()
                                    if ans not in result:
                                        result.append(ans)
                    
                    elif diff not in Hash and Sum in Hash:
                        Hash[Sum].append((i, j))
                    
                    else:
                        if Sum not in Hash:
                            Hash[Sum] = [(i, j)]
                        else:
                            Hash[Sum].append((i, j))
                            
            if result:
                result.sort()
                return result
            return []
