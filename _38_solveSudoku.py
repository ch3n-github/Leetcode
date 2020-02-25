class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        line=[set(range(1,10)) for _ in range(9)]
        row=[set(range(1,10)) for _ in range(9)]
        box=[set(range(1,10)) for _ in range(9)]
        empty=[]
        for i in range(9):
            for j in range(9):
                if board[i][j]!=".":
                    line[i].remove(int(board[i][j]))
                    row[j].remove(int(board[i][j]))
                    box[i//3*3+j//3].remove(int(board[i][j]))
                else:empty.append([i,j])
        def solve_suduku(i):
        
            for num in line[empty[i][0]]&row[empty[i][1]]&box[empty[i][0]//3*3+empty[i][1]//3]:
                line[empty[i][0]].remove(num)
                row[empty[i][1]].remove(num)
                box[empty[i][0]//3*3+empty[i][1]//3].remove(num)
                board[empty[i][0]][empty[i][1]]=str(num)
                if solve_suduku(i+1):
                    return True
                board[empty[i][0]][empty[i][1]]="."
                line[empty[i][0]].add(num)
                row[empty[i][1]].add(num)
                box[empty[i][0]//3*3+empty[i][1]//3].add(num)
        solve_suduku(0)