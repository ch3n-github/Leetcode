class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        line=[]
        row=[]
        box=[]
        dic=[1,2,3,4,5,6,7,8,9]
        for _ in range(9):
            line.append([])
            row.append([])
            box.append([])
        for i in range(9):
            for j in range(9):
                if board[i][j]!="." and (board[i][j] not in line[i]) and board[i][j] not in row[j] and (board[i][j] not in box[i//3*3+j//3]):
                    line[i].append(board[i][j])
                    row[j].append(board[i][j])
                    box[i//3*3+j//3].append(board[i][j])
                elif board[i][j]!=".":
                    return False
        return True