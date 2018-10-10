import heapq
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        n = len(A)
        if n == 0:
            return []
        if n == 1:
            return [A[0] + B[0]]
        A.sort(reverse=True)
        B.sort(reverse=True)
        #print (A)
        #print (B)
        heap = []
        dup_check = set()
        Sum = ((A[0] + B[0]) * -1, 0 ,0)
        #print(Sum)
        dup_check.add(Sum)
        heapq.heappush(heap, Sum)
        ans = []
        while len(ans) < n:
            pop = heapq.heappop(heap)
            ans.append(pop[0]*-1)
            if len(ans) == n:
                break
            i = pop[1]
            j = pop[2]
            #print(i, j)
            
            temp_1 = ((A[i+1] +  B[j] ) * -1, i+1, j )
            if temp_1 not in dup_check:
                dup_check.add(temp_1)
                heapq.heappush(heap, temp_1)
            #print (temp_1)
            temp_2 = ((A[i] +  B[j+1] ) * -1, i, j+1 )
            if temp_2 not in dup_check:
                dup_check.add(temp_2)
                heapq.heappush(heap, temp_2)
            #print (temp_2)
            #print (ans)

        return  ans

