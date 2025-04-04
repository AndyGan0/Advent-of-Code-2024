import numpy as np



# Load the grid
filename = "Day 13\input.txt"
with open(filename, 'r') as file:
        grid = [line.strip() for line in file if line.strip()]
grid = [string.split(" ") for string in grid]


total_cost = 0
total_prizes = 0

for machine in range(0, len(grid), 3):
    button_a_x = int( grid[machine][2][2:-1])
    button_a_y = int( grid[machine][3][2:])
    
    button_b_x = int( grid[machine + 1][2][2:-1])
    button_b_y = int( grid[machine + 1][3][2:])
    
    prize_x = int( grid[machine + 2][1][2:-1])
    prize_y = int( grid[machine + 2][2][2:])


    A = np.array([[button_a_x, button_b_x],
                  [button_a_y, button_b_y]])
    
    B = np.array([prize_x, prize_y])

    X = np.linalg.solve(A,B)

    if np.all(np.abs(X - np.round(X)) < 1e-9):
        #   solution exists. floats error or all int
        X = np.round(X)
        if (np.all(X > 100)):
            continue

        cost = 3 * X[0] + X[1]
        total_cost += cost
        total_prizes += 1

    else:
        # Reject as there are non-integer solutions
        continue

    


print(int(total_cost))
