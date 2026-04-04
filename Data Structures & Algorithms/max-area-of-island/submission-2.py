class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            print(grid[i])

        def dfs(row, col):
            grid[row][col] = 0
            directioins = [[0, 1], [0, -1], [1, 0], [-1, 0]]


            for dr in directioins:
                new_row = row + dr[0]
                new_col = col + dr[1]

                if (
                    new_row in range(len(grid))
                    and new_col in range(len(grid[0]))
                    and grid[new_row][new_col] == 1
                ):
                    path.append((new_row, new_col))
                    dfs(new_row, new_col)



        max_size = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                path = []
                if grid[i][j] == 1:
                    path.append((i, j))
                    dfs(i, j)
                    if len(path) > max_size:
                        max_size = len(path)


        return max_size