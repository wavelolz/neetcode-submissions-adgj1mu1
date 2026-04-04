class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def bt(inx, row, col):
            if word[inx] == board[row][col]:
                inx += 1
                if inx == len(word):
                    return True
                
                temp = board[row][col]
                board[row][col] = "#"

                if row+1<len(board) and board[row+1][col] != "#":
                    if bt(inx, row+1, col):
                        return True

                if row>0 and board[row-1][col] != "#":
                    if bt(inx, row-1, col):
                        return True

                if col+1<len(board[0]) and board[row][col+1] != "#":
                    if bt(inx, row, col+1):
                        return True

                if col>0 and board[row][col-1] != "#":
                    if bt(inx, row, col-1):
                        return True

                board[row][col] = temp

            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if bt(0, i, j):
                    return True
        return False
