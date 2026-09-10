class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # check rows
        for i in range(len(board)):
            seen = set()
            for j in range(len(board)):
                val = board[i][j]
                if val == ".":
                    continue
                if val in seen:
                    return False
                seen.add(val)

        # check cols
        for i in range(len(board[0])):
            seen = set()
            for j in range(len(board)):
                val = board[j][i]
                if val == ".":
                    continue
                if val in seen:
                    return False
                seen.add(val)

        # check all the 3x3 grids
        gridStart = [[0, 0], [0, 3], [0, 6],
                [3, 0], [3, 3], [3, 6],
                [6, 0], [6, 3], [6, 6],
                ]

        for cord in gridStart:
            x, y = cord
            seen = set()
            for i in range(x, x + 3):
                for j in range(y, y + 3):
                    val = board[i][j]
                    if val == ".":
                        continue
                    if val in seen:
                        return False
                    seen.add(val)

        return True
        