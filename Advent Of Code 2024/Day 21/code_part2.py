import sys
import numpy as np



# Load the grid
filename = "Day 21\input.txt"
with open(filename, 'r') as file:
    door_codes = [line for line in file]
door_codes = [x[:-1] if x[-1] == '\n' else x for x in door_codes ]
door_codes = [x.strip() for x in door_codes ]



def translate_door_code_into_robot_moves(code):
    button_positions = {
        '7': (0,0),
        '8': (1,0),
        '9': (2,0),
        '4': (0,1),
        '5': (1,1),
        '6': (2,1),
        '1': (0,2),
        '2': (1,2),
        '3': (2,2),
        '0': (1,3),
        'A': (2,3)
    }


    last_position = 'A'
    robot_moves = [""]

    while len(code) != 0:
        robot_move_in_axis = tuple(a - b for a, b in zip(button_positions[code[0]], button_positions[last_position]))

        current_moves = [{
            'move': "",
            'axis_moves_waiting': robot_move_in_axis,            
            'position': button_positions[last_position]
        }]


        while any(x['axis_moves_waiting'] != (0,0) for x in current_moves):

            for move in current_moves:
                if (move['axis_moves_waiting'][0] == 0 or move['axis_moves_waiting'][1] == 0 ):
                    #   need to move only in 1 axis
                    if (move['axis_moves_waiting'][0] < 0):
                        move['move'] += '<'
                        move['axis_moves_waiting'] = (move['axis_moves_waiting'][0] + 1, move['axis_moves_waiting'][1])
                        move['position'] = (move['position'][0] - 1, move['position'][1])
                    elif (move['axis_moves_waiting'][0] > 0):
                        move['move'] += '>'
                        move['axis_moves_waiting'] = (move['axis_moves_waiting'][0] - 1, move['axis_moves_waiting'][1])
                        move['position'] = (move['position'][0] + 1, move['position'][1])
                    elif (move['axis_moves_waiting'][1] < 0):
                        move['move'] += '^'
                        move['axis_moves_waiting'] = (move['axis_moves_waiting'][0], move['axis_moves_waiting'][1] + 1)
                        move['position'] = (move['position'][0], move['position'][1] - 1)
                    elif (move['axis_moves_waiting'][1] > 0):
                        move['move'] += 'V'
                        move['axis_moves_waiting'] = (move['axis_moves_waiting'][0], move['axis_moves_waiting'][1] - 1)
                        move['position'] = (move['position'][0], move['position'][1] + 1)

                else:
                    #   need to move in both axis
                    if (move['axis_moves_waiting'][0] < 0 and move['position'] != (1,3)):
                        current_moves.append({
                            'move': move['move'] + '<',
                            'axis_moves_waiting': (move['axis_moves_waiting'][0] + 1, move['axis_moves_waiting'][1]),
                            'position': (move['position'][0] - 1, move['position'][1]),
                        })
                    elif (move['axis_moves_waiting'][0] > 0):
                        current_moves.append({
                            'move': move['move'] + '>',
                            'axis_moves_waiting': (move['axis_moves_waiting'][0] - 1, move['axis_moves_waiting'][1]),
                            'position': (move['position'][0] + 1, move['position'][1]),
                        })
                    
                    if (move['axis_moves_waiting'][1] > 0 and move['position'] != (0,2) ):
                        move['move'] += 'V'
                        move['axis_moves_waiting'] = (move['axis_moves_waiting'][0], move['axis_moves_waiting'][1] - 1)
                        move['position'] = (move['position'][0], move['position'][1] + 1)
                    elif (move['axis_moves_waiting'][1] < 0):
                        move['move'] += '^'
                        move['axis_moves_waiting'] = (move['axis_moves_waiting'][0], move['axis_moves_waiting'][1] + 1)    
                        move['position'] = (move['position'][0], move['position'][1] - 1) 


        for move in current_moves:
            move['move'] += 'A'
        
        new_robot_moves = []
        for already_existing_moves in robot_moves: 
            for move in current_moves:
                new_robot_moves.append(already_existing_moves + move['move'])        
        robot_moves = new_robot_moves

        last_position = code[0]
        code = code[1:]

    return robot_moves







def translate_into_next_robot_moves(previous_robot_move):
    button_positions = {
        '^': (1,0),
        'A': (2,0),
        '<': (0,1),
        'V': (1,1),
        '>': (2,1)
    }


    last_position = 'A'
    next_robot_moves = [""]

    while len(previous_robot_move) != 0:
        robot_move_in_axis = tuple(a - b for a, b in zip(button_positions[previous_robot_move[0]], button_positions[last_position]))

        current_moves = [{
            'move': "",
            'axis_moves_waiting': robot_move_in_axis,            
            'position': button_positions[last_position]
        }]


        while any(x['axis_moves_waiting'] != (0,0) for x in current_moves):

            for move in current_moves:
                if (move['axis_moves_waiting'][0] == 0 and move['axis_moves_waiting'][1] == 0):
                    continue

                if (move['axis_moves_waiting'][0] == 0 or move['axis_moves_waiting'][1] == 0 ):
                    #   need to move only in 1 axis
                    if (move['axis_moves_waiting'][0] < 0):
                        move['move'] += '<'
                        move['axis_moves_waiting'] = (move['axis_moves_waiting'][0] + 1, move['axis_moves_waiting'][1])
                        move['position'] = (move['position'][0] - 1, move['position'][1])
                    elif (move['axis_moves_waiting'][0] > 0):
                        move['move'] += '>'
                        move['axis_moves_waiting'] = (move['axis_moves_waiting'][0] - 1, move['axis_moves_waiting'][1])
                        move['position'] = (move['position'][0] + 1, move['position'][1])
                    elif (move['axis_moves_waiting'][1] < 0):
                        move['move'] += '^'
                        move['axis_moves_waiting'] = (move['axis_moves_waiting'][0], move['axis_moves_waiting'][1] + 1)
                        move['position'] = (move['position'][0], move['position'][1] - 1)
                    elif (move['axis_moves_waiting'][1] > 0):
                        move['move'] += 'V'
                        move['axis_moves_waiting'] = (move['axis_moves_waiting'][0], move['axis_moves_waiting'][1] - 1)
                        move['position'] = (move['position'][0], move['position'][1] + 1)

                else:
                    if (move['axis_moves_waiting'][0] < 0 and move['position'] == (1,0)):
                        move['move'] += 'V'
                        move['axis_moves_waiting'] = (move['axis_moves_waiting'][0], move['axis_moves_waiting'][1] - 1)
                        move['position'] = (move['position'][0], move['position'][1] + 1)
                        continue
                    elif (move['axis_moves_waiting'][1] < 0 and move['position'] == (0,1)):
                        move['move'] += '>'
                        move['axis_moves_waiting'] = (move['axis_moves_waiting'][0] - 1, move['axis_moves_waiting'][1])
                        move['position'] = (move['position'][0] +1, move['position'][1]) 
                        continue


                    #   need to move in both axis
                    if (move['axis_moves_waiting'][0] < 0):
                        current_moves.append({
                            'move': move['move'] + '<',
                            'axis_moves_waiting': (move['axis_moves_waiting'][0] + 1, move['axis_moves_waiting'][1]),
                            'position': (move['position'][0] - 1, move['position'][1]),
                        })
                    elif (move['axis_moves_waiting'][0] > 0):
                        current_moves.append({
                            'move': move['move'] + '>',
                            'axis_moves_waiting': (move['axis_moves_waiting'][0] - 1, move['axis_moves_waiting'][1]),
                            'position': (move['position'][0] + 1, move['position'][1]),
                        })


                    
                    if (move['axis_moves_waiting'][1] > 0):
                        move['move'] += 'V'
                        move['axis_moves_waiting'] = (move['axis_moves_waiting'][0], move['axis_moves_waiting'][1] - 1)
                        move['position'] = (move['position'][0], move['position'][1] + 1)
                    elif (move['axis_moves_waiting'][1] < 0):
                        move['move'] += '^'
                        move['axis_moves_waiting'] = (move['axis_moves_waiting'][0], move['axis_moves_waiting'][1] + 1)    
                        move['position'] = (move['position'][0], move['position'][1] - 1) 


        for move in current_moves:
            move['move'] += 'A'
        
        temp = []
        for already_existing_moves in next_robot_moves: 
            for move in current_moves:
                temp.append(already_existing_moves + move['move'])        
        next_robot_moves = temp

        last_position = previous_robot_move[0]
        previous_robot_move = previous_robot_move[1:]

    return next_robot_moves







#   dict for dynamic programming
robot_k_moves_length = { }

def find_robot_move_after_k_robots(robot_move, k = 25):

    if (k not in robot_k_moves_length):
        robot_k_moves_length[k] = {}    
    
    if (k == 0):
        return len(robot_move)


    robot_move = robot_move.split('A')
    robot_move = [x + 'A' for x in robot_move[:-1]]


    total_length = 0
    for move in robot_move:
        if move in robot_k_moves_length[k]:
            length_of_move = robot_k_moves_length[k][move]
        else:
            next_robot_move_list = translate_into_next_robot_moves(move)

            length_of_move = find_robot_move_after_k_robots( next_robot_move_list[0], k = k-1)
            for i in range(1, len(next_robot_move_list)):
                new_length = find_robot_move_after_k_robots(next_robot_move_list[i], k = k-1)
                if (new_length < length_of_move):
                    length_of_move = new_length

        total_length += length_of_move
        robot_k_moves_length[k][move] = length_of_move


    return total_length






code_complexities = []

for code in door_codes:
    translated_code_1st_robot_list = translate_door_code_into_robot_moves(code)
    min_length = min(len(x) for x in translated_code_1st_robot_list)
    translated_code_1st_robot_list = [x for x in translated_code_1st_robot_list if len(x) == min_length]


    length_after_k_moves = find_robot_move_after_k_robots(translated_code_1st_robot_list[0], 25)
    for u in range(1, len(translated_code_1st_robot_list)):
        new_length = find_robot_move_after_k_robots(translated_code_1st_robot_list[u], 25)
        if (new_length < length_after_k_moves):
            length_after_k_moves = new_length




    numeric_part_of_code = int(code[:-1])
    code_complexities.append(length_after_k_moves * numeric_part_of_code)

sum = sum(code_complexities)
print(sum)