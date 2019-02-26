class Solution:
    # @param A : list of integers
    # @return a list of integers

    def equal(self, A):
        n = len(A)
        if n < 4:
            return []
        result = []
        sum_i_j = {}
        for i in range(0, n):
            for j in range(i + 1, n):
                Sum = A[i] + A[j]

                if Sum not in sum_i_j:
                    sum_i_j[Sum] = [i, j]
                else:
                    if sum_i_j[Sum][0] != i and sum_i_j[Sum][0] != j and sum_i_j[Sum][1] != i and sum_i_j[Sum][1] != j:
                        result.append(sum_i_j[Sum] + [i, j])

        return sorted(result)[0 ]
