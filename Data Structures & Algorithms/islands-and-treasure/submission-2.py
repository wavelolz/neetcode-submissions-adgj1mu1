from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # start from every treasure
        # use bfs, the first time any treasure touch a land it guarantees a shortest path
        search = deque([])

        
        def bfs(row, col, nearest_treasure):
            direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]

            for dr in direction:
                new_row = row+dr[0]
                new_col = col+dr[1]

                if (new_row in range(len(grid)) and 
                    new_col in range(len(grid[0])) and 
                    grid[new_row][new_col] == 2147483647):
                        if nearest_treasure < grid[new_row][new_col]:
                            grid[new_row][new_col] = nearest_treasure+1
                        search.append((new_row, new_col, nearest_treasure+1))


        treasure_loc = [(row, col) for row in range(len(grid)) for col in range(len(grid[0])) if grid[row][col] == 0]
        for row, col in treasure_loc:
            search.append((row, col, 0))
        

        while search:
            next_search_row, next_search_col, dist = search.popleft()
            bfs(next_search_row, next_search_col, dist)


  




