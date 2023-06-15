grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

xnGridVal = 0
ynGridVal = 0
inGrid = []


for ynGridVal in range(len(grid[ynGridVal])):
    inGrid.append([])
    for xnGridVal in range(len(grid)):
        inGrid[ynGridVal].append(grid[xnGridVal][ynGridVal])

print(inGrid)
