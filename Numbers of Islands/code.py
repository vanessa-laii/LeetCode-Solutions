class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, columns = len(grid) , len(grid[0])
        res = 0
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def bfs(row, column):
            queue = deque()
            queue.append((row, column))
            grid[row][column] = "0"
            while queue:
                row, column = queue.popleft()
                for dr, dc in directions:
                    if 0 <= dr + row < rows and 0 <= dc + column < columns and grid[dr + row][dc + column] == "1":
                        queue.append((dr+row, dc + column))
                        grid[dr+row][dc + column] = "0"

        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == "1":
                    res += 1
                    bfs(row, column)
        
        return res


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, columns = len(grid) , len(grid[0])
        res = 0
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def dfs(row, column):
            if not 0 <= row < rows or not 0<= column < columns or grid[row][column] == "0":
                return 
            grid[row][column] = "0" 
            for dr, dc in directions:
                dfs(dr+row, dc+column)            

        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == "1":
                    res += 1
                    dfs(row, column)
        
        return res

        