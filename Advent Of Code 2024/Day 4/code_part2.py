

def count_x_word_in_grid(grid, word):
    # Dimensions of the grid
    rows = len(grid)
    cols = len(grid[0])
    word_len = len(word)

    count = 0

    word_backwords = word[::-1]

    for i in range(rows - word_len + 1):
        for j in range (cols - word_len + 1):
            microscope = [grid[i][j:j+3],
                          grid[i+1][j:j+3],
                          grid[i+2][j:j+3]]
            
            first_diagonal = []            
            first_diagonal.append(microscope[0][0])
            first_diagonal.append(microscope[1][1])
            first_diagonal.append(microscope[2][2])
            first_diagonal = ''.join(first_diagonal)


            second_diagonal = []            
            second_diagonal.append(microscope[0][2])
            second_diagonal.append(microscope[1][1])
            second_diagonal.append(microscope[2][0])
            second_diagonal = ''.join(second_diagonal)

            if ((first_diagonal == word or first_diagonal == word_backwords) and (second_diagonal == word or second_diagonal == word_backwords) ):
                count += 1

    
        
    return count
    






with open("Day 4\input.txt", 'r') as file:
    grid = [line.strip() for line in file if line.strip()]


word = "MAS"

result = count_x_word_in_grid(grid, word)

print(result)