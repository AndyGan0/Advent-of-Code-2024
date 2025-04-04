

def get_main_diagonals(grid):
    rows = len(grid)
    cols = len(grid[0])

    main_diagonals = []

    for d_first_item in range(rows):
        current_diagonal = []
        for i in range(rows):
            j = i - d_first_item
            if 0 <= j < cols:
                current_diagonal.append(grid[i][j])
        main_diagonals.append(''.join(current_diagonal))

    for d_first_item in range(1, cols):
        current_diagonal = []
        for j in range(cols):
            i = j - d_first_item
            if 0 <= i < rows:
                current_diagonal.append(grid[i][j])
        main_diagonals.append(''.join(current_diagonal))
        

    return main_diagonals





def get_secondary_diagonals(grid):
    rows = len(grid)
    cols = len(grid[0])

    secondary_diagonals = []

    
    
    for d_first_item in range(rows):
        diagonal = []
        for i in range(rows):
            j = d_first_item - i
            if 0 <= j < cols:
                diagonal.append(grid[i][j])
        secondary_diagonals.append(''.join(diagonal))

    for d_first_item in range(1, cols):
        diagonal = []
        for j in range(cols):
            i = rows - 1 - (j - d_first_item)
            if 0 <= i < rows:
                diagonal.append(grid[i][j])
        secondary_diagonals.append(''.join(diagonal))
        

    return secondary_diagonals





def count_words(grid, word):
    word_backwords = word[::-1]
    
    count_appearance = 0


    #   for all rows
    for row in grid:
        for pointer in range(len(row)):
            temp = "".join(row[pointer: pointer + len(word)])
            if ( temp == word or temp == word_backwords):
                count_appearance += 1
        


    transposed_grid = list(zip(*grid))
    transposed_grid = [''.join(col) for col in transposed_grid]

    for column in transposed_grid:
        for pointer in range(len(column)):
            temp = column[pointer: pointer + len(word)]
            if ( temp == word or temp == word_backwords):
                count_appearance += 1



    # Main diagonals ↘
    main_diagonals = get_main_diagonals(grid)
    # Secondary diagonal ↙
    secondary_diagonals = get_secondary_diagonals(grid)


    for diagonal in main_diagonals:
        for pointer in range(len(diagonal)):
            temp = diagonal[pointer: pointer + len(word)]
            if ( temp == word or temp == word_backwords):
                count_appearance += 1    


    for diagonal in secondary_diagonals:
        for pointer in range(len(diagonal)):
            temp = diagonal[pointer: pointer + len(word)]
            if ( temp == word or temp == word_backwords):
                count_appearance += 1
        
    return count_appearance
    




# Load grid
with open("Day 4\input.txt", 'r') as file:
    grid = [line.strip() for line in file if line.strip()]
    grid = [list(string) for string in grid]

word = "XMAS"

# Count occurrences of the word
result = count_words(grid, word)

print(result)