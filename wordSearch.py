from typing import List

def exist(board: List[List[str]],word:str) -> bool:

    #1 percorrer o grid
    n_rows = len(board)
    n_cols = len(board[0])

    for row in range(n_rows):
        for col in range(n_cols):
            if backtrack(board,n_rows,n_cols,row,col,word):
                return True
    return False

def backtrack(board,n_rows,n_cols,row,col,suffix):

    # já encontrei a palavra
    if len(suffix) == 0:
        return True
    
    # Se estou fora do board ou se a minha letra ali não é a que estou procurando:
    if (row<0 or row == n_rows or col < 0 or col == n_cols or board[row][col] != suffix[0]):
        return False
    
    board[row][col] = '#'

    directions = [(0,1),(1,0),(0,-1),(-1,0)]

    for row_offset, col_offset in directions:
        # passo o board, os passos que vou fazer e um suffixo menor caso encontre
        res = backtrack(board,n_rows,n_cols,row+row_offset,col+col_offset,suffix[1:])

        if res:
            return True
    
    return False




    # retornar se ok

    #validar a célula atual

    #marcar como visto

    #backtrack

    return False

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"

print(exist(board,word))