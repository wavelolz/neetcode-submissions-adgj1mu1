from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        at_set, pa_set = set(), set()
        rows, cols = len(heights), len(heights[0])

        def dfs(row, col, visited):
            visited.add((row, col))

            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc

                if (
                    0 <= new_row < rows
                    and 0 <= new_col < cols
                    and heights[new_row][new_col] >= heights[row][col]
                    and (new_row, new_col) not in visited
                ):
                    dfs(new_row, new_col, visited)

        # Pacific (left + top)
        for r in range(rows):
            dfs(r, 0, pa_set)
            dfs(r, cols - 1, at_set)

        for c in range(cols):
            dfs(0, c, pa_set)
            dfs(rows - 1, c, at_set)

        return list(at_set & pa_set)