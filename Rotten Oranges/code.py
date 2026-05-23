class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # adding all the rotten to a queue
        rows, columns = len(grid), len(grid[0])
        fresh = 0
        queue = deque()
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append((r,c))

        # processing the oranges
        minutes = 0
        directions = [[1,0], [0, 1], [-1, 0], [0, -1]]
        while fresh > 0 and queue:
            length = len(queue)
            for orange in range(length):
                row, column = queue.popleft()
                for dr, dc in directions:
                    r, c = dr + row, dc + column
                    if 0 <= r < rows and 0<= c < columns and grid[r][c] == 1:
                        grid[r][c] = 2
                        queue.append((r, c))
                        fresh -= 1
            
            minutes += 1
    

        return minutes if fresh == 0 else -1