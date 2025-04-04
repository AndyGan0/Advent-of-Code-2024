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



def translate_robot_moves_into_previous_robot_moves(next_robot_moves):    
    button_positions = {
        '^': (1,0),
        'A': (2,0),
        '<': (0,1),
        'V': (1,1),
        '>': (2,1)
    }

    last_position = 'A'
    previous_robot_moves = []

    while len(next_robot_moves) != 0:
        previous_robot_move_in_axis = tuple(a - b for a, b in zip(button_positions[next_robot_moves[0]], button_positions[last_position]))

        if (previous_robot_move_in_axis[1] > 0):
            previous_robot_moves.append('V')
            previous_robot_move_in_axis = (previous_robot_move_in_axis[0], previous_robot_move_in_axis[1] - 1)        
        
        for j in range(abs(previous_robot_move_in_axis[0])):
            if (previous_robot_move_in_axis[0] < 0):
                previous_robot_moves.append('<')
            elif (previous_robot_move_in_axis[0] > 0):
                previous_robot_moves.append('>')
        
        for i in range(abs(previous_robot_move_in_axis[1])):
            if (previous_robot_move_in_axis[1] < 0):
                previous_robot_moves.append('^')
            elif (previous_robot_move_in_axis[1] > 0):
                previous_robot_moves.append('V')



        previous_robot_moves.append('A')
        last_position = next_robot_moves[0]
        next_robot_moves = next_robot_moves[1:]

    return ''.join(previous_robot_moves)



code_complexities = []

for code in door_codes:
    translated_code_1st_robot_list = translate_door_code_into_robot_moves(code)
    
    translated_moves_2nd_robot_list = []
    for item in translated_code_1st_robot_list:
        translated_moves_2nd_robot_list.append(translate_robot_moves_into_previous_robot_moves(item))
    min_length = min(len(s) for s in translated_moves_2nd_robot_list)
    translated_moves_2nd_robot_list = [x for x in translated_moves_2nd_robot_list if len(x) == min_length]


    translated_moves_to_human_list = []
    for item in translated_moves_2nd_robot_list:
        translated_moves_to_human_list.append(translate_robot_moves_into_previous_robot_moves(item))
    min_length = min(len(s) for s in translated_moves_to_human_list)
    translated_moves_to_human_list = [x for x in translated_moves_to_human_list if len(x) == min_length]




    length_of_last_sequence = len(translated_moves_to_human_list[0])
    numeric_part_of_code = int(code[:-1])
    code_complexities.append(length_of_last_sequence * numeric_part_of_code)


print(sum(code_complexities))