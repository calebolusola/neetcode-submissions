class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # first check every row for duplicates
        # check every column for duplicates
        # check every 3x3 grid for duplicates
        
        num_board_rows = 9
        
        row_stripped = [[x for x in numbers if x != "."] for numbers in board]
        
        # check row for duplicates
        row_valid = all(len(x) == len(set(x)) for x in row_stripped)
        if not row_valid:
            return False
        
        # a column is row[i] in every row for every i in len(board)
        cols_stripped = [[row[i] for row in board if row[i] != '.'] for i in range(num_board_rows)]
        
        # check cols for duplicates
        cols_valid = all(len(x) == len(set(x)) for x in cols_stripped)
        if not cols_valid:
            return False
        
        # construct array of 3x3 grids.
        
        # to construct a 3x3 grid, we return the nth 3 elements
        # for n in range rows skipping 3 up until the first n rows
        # for every n in range len board skipping by 3
        
        # for example:
        for row_start in range(0, 9, 3):
            for col_start in range(0, 9, 3):
                box = []
                for row in range(3):
                    for col in range(3):
                        value = board[row_start+row][col_start+col]
                        if value != ".":
                            box.append(value)
                if len(set(box)) != len(box):
                    return False

        return True