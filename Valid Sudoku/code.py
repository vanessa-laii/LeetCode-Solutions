class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #1. whats the input format
        rows = len(board)
        columns = len(board[0])

        rowSet, columnSet, boxes = set(), set(), set()

        for row in range(rows):
            for column in range(columns):
                piece = board[row][column]
                if piece == ".":
                    continue
                print(piece)
                # check sets
                if (piece, row) in rowSet or (piece, column) in columnSet:
                    print(piece, row)
                    return False
                if (piece, row//3, column//3) in boxes:
                    print(piece, row//3, column//3)
                    return False
                
                rowSet.add((piece, row))
                columnSet.add((piece, column))
                boxes.add((piece, row//3, column//3))
                print("Hello")
        
        return True
                


        