import numpy as np

def letter_to_number(letter):
    letter = letter.upper()
    if letter == "A":
        return 0
    elif letter == "B":
        return 1
    elif letter == "C":
        return 2
    elif letter == "D":
        return 3
    elif letter == "E":
        return 4
    elif letter == "F":
        return 5
    else:
        return 6

def input_sequence_order(move, matrix):
    color = move[0]
    place_x = letter_to_number(move[1])
    place_y = letter_to_number(move[2])
    matrix[place_x][place_y] = color

def input_sequence_chaos(move, matrix):
    if move != 'Start':
        new_put_1 = str(matrix[letter_to_number(move[0])][letter_to_number(move[1])]) + str(move[2])+str(move[3])
        input_sequence_order(new_put_1, matrix)
        new_put_2 = str(0) + str(move[0])+str(move[2])
        input_sequence_order(new_put_2, matrix)


board = np.array(([0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0]))

input_sequence_order("2Gb", board)
input_sequence_chaos("BdGd", board)

print(board)
