def numberIslands(grid):

    row,col = len(grid),len(grid[0])
    count = 0

    for row,col in grid:

        if grid[row][col] == 1 :
            return 5 
    return 0

#para cada célula:
# se é uma terra não visitada, incrementar contador de ilha


grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

print(numberIslands(grid))