class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(row, col):
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

            for dr in directions:
                new_row = row+dr[0]
                new_col = col+dr[1]

                if (
                    new_row in range(len(grid))
                    and new_col in range(len(grid[0]))
                    and grid[new_row][new_col] == "1"
                ):
                    grid[new_row][new_col] = "0"
                    dfs(new_row, new_col)
            return

        cnt = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    dfs(row, col)
                    cnt += 1
        return cnt
        