from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def bfs(row, col):
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            affected = 0

            for dr in directions:
                new_row = row + dr[0]
                new_col = col + dr[1]

                if (
                    new_row in range(len(grid))
                    and new_col in range(len(grid[0]))
                    and grid[new_row][new_col] == 1
                ):
                    grid[new_row][new_col] = 2
                    rotten.append((new_row, new_col))
                    affected += 1

            return affected

        rotten = deque([])

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    rotten.append((row, col))

        total_fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    total_fresh += 1
        if total_fresh == 0:
            return 0

        total_time = 0
        next_iter = 0
        current_iter = len(rotten)

        while rotten:
            next_row, next_col = rotten.popleft()
            new_affected = bfs(next_row, next_col)
            total_fresh -= new_affected
            current_iter -= 1
            next_iter += new_affected

            if current_iter == 0:
                total_time += 1
                current_iter, next_iter = next_iter, 0
                if total_fresh == 0:
                    return total_time
                
            else:
                if total_fresh == 0:
                    return total_time+1


            # for i in range(len(grid)):
            #     print(grid[i])
            # print(total_time)
            # print(current_iter)
            # print("=====")




        return -1