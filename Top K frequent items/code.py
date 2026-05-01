import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count the number of occurences for each
        count = collections.Counter(nums)
        heap = []
        # build a maxheap for all the occurences 
        for key, value in count.items():
            heapq.heappush(heap, (-1 * value, key))
        # pop k times from the heap and return an array of the kyes
        result = []
        for i in range(k):
            value, key = heapq.heappop(heap)
            result.append(key)

        return result
        
        



        