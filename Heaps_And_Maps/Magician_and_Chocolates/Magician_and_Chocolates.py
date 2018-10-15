import heapq
class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def nchoc(self, A, B):
        if A == 0 or not B:
            return 0
        count = 0
        heap = []
        for i in B:
            heapq.heappush(heap, -i)
        #print(heap)
        for j in range(A):
            heap_pop = -heapq.heappop(heap)
            count+= heap_pop
            heapq.heappush(heap, -(heap_pop//2))
            #print(heap)
        return count%(10**9+7)
        
