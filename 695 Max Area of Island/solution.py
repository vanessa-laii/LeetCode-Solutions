class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        directions = [[1,0], [0,1], [0,-1], [-1,0]]
        visited = set()
        maxArea = 0

        def bfs(row, column) -> int:
            queue = collections.deque()
            queue.append((row, column))
            visited.add((row, column))
            area = 0

            while queue:
                row, column = queue.popleft()
                area += 1
                for dr, dc in directions:
                    r, c = dr + row, column + dc
                    if r in range(rows) and c in range(columns) and grid[r][c] == 1 and ((r,c)) not in visited:
                        queue.append((r, c))
                        visited.add((r,c))
            
            return area

        for row in range(rows):
            for column in range(columns):
                piece = grid[row][column]
                if piece == 1 and ((row, column)) not in visited:
                    area = bfs(row, column)
                    maxArea = max(maxArea, area)
        
        return maxArea


    