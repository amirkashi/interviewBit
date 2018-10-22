class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers

    def anagrams(self, A):
        if not A:
            return A
        result = []
        n = len(A)
        result = []
        Dict = {}
        resutl_index = 0
        for i in range(n):
            sorted_i = ''.join(sorted(A[i]))
            if sorted_i not in Dict:
                result.append([i + 1])
                Dict[sorted_i] = resutl_index
                resutl_index += 1
            else:
                result[Dict[sorted_i]].append(i + 1)
        return result
