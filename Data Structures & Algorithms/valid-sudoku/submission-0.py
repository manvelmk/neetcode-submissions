# Valid Sudoku
# You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

# Each row must contain the digits 1-9 without duplicates.
# Each column must contain the digits 1-9 without duplicates.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
from collections import defaultdict

class Solution:
    EMPTY_CELL = "."
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = defaultdict(set) # maintains entries in rows of the board
        cols = defaultdict(set) # maintains entries in columns of the board
        subDiv = defaultdict(set) # maintains entries in the sub-squares of the board 3x3
        
        for row in range(len(board)):
            for col in range(len(board[0])): # Time complexity already O^n^2
                entry = board[row][col]
                if entry != self.EMPTY_CELL: # only considering the non-empty cells
                    # any matgch below means we had the same entry in that set previously, fail outright
                    if (entry in rows[row] or
                        entry in cols[col] or 
                        entry in subDiv[row // 3, col // 3]): # uses // for floor division, no decimal
                        return False
                    # no quick failure, register the entry in all three sets
                    rows[row].add(entry)
                    cols[col].add(entry)
                    subDiv[row // 3, col // 3].add(entry)
        return True # no duplicates were found, technically a "valid" board