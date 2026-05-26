class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # make a heap of the distances and points
        heap = []
        for x, y in points:
            distance = -1 * math.sqrt(x*x + y*y)
            heapq.heappush(heap, (distance, (x,y)))
            while len(heap) > k:
                heapq.heappop(heap)
                
        # want the shortest distances
        result = []
        while heap:
            result.append(heapq.heappop(heap)[1])

        return result

        # pop out the k closest (shortest distances)


        