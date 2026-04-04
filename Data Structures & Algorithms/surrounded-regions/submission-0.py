from typing import List
from collections import deque


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    queue = deque([])
                    queue.append((r, c))

                    visit = []
                    visit.append((r, c))

                    bc = 0

                    while queue:
                        cr, cc = queue.popleft()

                        if cr == 0 or cr == rows - 1 or cc == 0 or cc == cols - 1:
                            bc = 1

                        for dr in directions:
                            nr = cr + dr[0]
                            nc = cc + dr[1]

                            if (
                                0 <= nr < rows
                                and 0 <= nc < cols
                                and board[nr][nc] == "O"
                                and (nr, nc) not in visit
                            ):
                                queue.append((nr, nc))
                                visit.append((nr, nc))

                    if bc == 0:
                        for vr, vc in visit:
                            board[vr][vc] = "X"