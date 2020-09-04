# Kasra Mojallal

import numpy as np


# this function is used to read the nfa from file
def read_file():
    f = open("NFA_Input_2.txt", "r")

    # save our alphabet in a array
    my_chars = f.readline().split()
    chars = []

    for i in range(len(my_chars)):
        chars.append(int(my_chars[i]))

    chars.append(206)

    #  save our states in an array
    my_states = f.readline().split()
    states = []

    for i in range(len(my_states)):
        states.append(int(my_states[i][-1]))

    #  save our starting and finishing states
    start_s = int(f.readline()[-2])
    end_s = int(f.readline()[-2])

    arr_2 = [[] for i in range(10)]

    #  array to store which state takes us where
    arr_0 = np.full((300, 300, 300), -1)

    #  this function reads the whole file and stores what state to go from which state
    while True:
        str0 = f.readline()
        if str0 == '\n':
            break
        if arr_0[int(str0[1]), ord(str0[3]), 0] == -1:
            arr_0[int(str0[1]), ord(str0[3]), 0] = int(str0[-2])
        elif arr_0[int(str0[1]), ord(str0[3]), 0] != -1 and arr_0[int(str0[1]), ord(str0[3]), 1] == -1:
            arr_0[int(str0[1]), ord(str0[3]), 1] = int(str0[-2])
        else:
            arr_0[int(str0[1]), ord(str0[3]), 2] = int(str0[-2])

    #  this function calculates the closure for every state
    counter = 0
    for i in range(len(states)):
        if arr_0[i, 206, 0] != -1:
            we = int(arr_0[i, 206, 0])
            arr_2[counter].append(states[i])
            arr_2[counter].append(int(arr_0[i, 206, 0]))
            if arr_0[we, 206, 0] != -1:
                arr_2[counter].append(int(arr_0[we, 206, 0]))
            counter += 1
        else:
            arr_2[counter].append(states[i])
            counter += 1

    cn = 0
    for i in range(len(arr_2)):
        if arr_2[i]:
            cn += 1

    # this array will be used for storing all our selection states
    arr_x = [[] for i in range(cn)]

    for i in range(cn):
        arr_x[i] = arr_2[i]

    print(arr_x)

    # this arrays will be having the information about the path of every selection state
    to_state_a = [[] for i in range(len(arr_x))]
    to_state_a2 = [[] for i in range(len(arr_x))]
    to_state_b = [[] for i in range(len(arr_x))]
    to_state_b2 = [[] for i in range(len(arr_x))]

    arr = []

    #  this long function calculates the path for every selection state
    #  with '0' input and '1' input
    for i in range(len(arr_x)):
        for j in range(len(arr_x[i])):
            if arr_0[arr_x[i][j], 48, 0] != -1:
                arr.append(arr_0[arr_x[i][j], 48, 0])
        for k in range(len(arr_x)):
            if set(arr) == set(arr_x[k]):
                to_state_a[i] = arr_x[k]
        arr = []
        for p in range(len(arr_x[i])):
            if arr_0[arr_x[i][p], 48, 1] != -1:
                arr.append(arr_0[arr_x[i][p], 48, 1])
        for z in range(len(arr_x)):
            if set(arr) == set(arr_x[z]):
                to_state_a2[i] = arr_x[z]

        arr = []

        for j in range(len(arr_x[i])):
            if arr_0[arr_x[i][j], 49, 0] != -1:
                arr.append(arr_0[arr_x[i][j], 49, 0])
        for k in range(len(arr_x)):
            if set(arr) == set(arr_x[k]):
                to_state_b[i] = arr_x[k]
        arr = []
        for p in range(len(arr_x[i])):
            if arr_0[arr_x[i][p], 49, 1] != -1:
                arr.append(arr_0[arr_x[i][p], 49, 1])
        for z in range(len(arr_x)):
            if set(arr) == set(arr_x[z]):
                to_state_b2[i] = arr_x[z]

        arr = []

    print(to_state_a)
    print(to_state_a2)
    print(to_state_b)
    print(to_state_b2)

    arr_start = arr_x[0]

    #  this array stores the ending selection states
    arr_end = []

    for i in range(len(arr_x)):
        if end_s in arr_x[i]:
            arr_end.append(arr_x[i])

    return my_chars, arr_x, to_state_a, to_state_a2, to_state_b, to_state_b2, arr_start, arr_end


#  this simple function writes our data on the file
def write_to_file(my_ch_w, array1_w, to_a_w, to_a2_w, to_b_w, to_b2_w, start_w, end_w):
    f = open("DFA_Output_2.txt", "w")

    #  writes the alphabet
    for i in range(len(my_ch_w)):
        f.write(my_ch_w[i] + ' ')
    f.write('\n')

    #  writes the states
    for i in range(len(array1_w)):
        f.write('[ ')
        for j in range(len(array1_w[i])):
            f.write('q' + str(array1_w[i][j]) + ' ')
        f.write('] ')
    f.write('\n')

    #  writes the starting selection state
    f.write('[ ')
    for i in range(len(start_w)):
        f.write('q' + str(start_w[i]) + ' ')
    f.write(']' + '\n')

    #  writes the ending states
    for i in range(len(end_w)):
        f.write('[ ')
        for j in range(len(end_w[i])):
            f.write('q' + str(end_w[i][j]) + ' ')
        f.write('] ')
    f.write('\n')

    #  writes the path for selection states with '0' input
    for i in range(len(to_a_w)):
        if to_a_w[i]:
            f.write('[ ')
            for j in range(len(array1_w[i])):
                f.write('q' + str(array1_w[i][j]) + ' ')
            f.write(']    ' + my_ch_w[0] + '    [')
            for j in range(len(to_a_w[i])):
                f.write('q' + str(to_a_w[i][j]) + ' ')
            f.write(']\n')

    #  writes the path for selection states with '0' input
    for i in range(len(to_a2_w)):
        if to_a2_w[i]:
            f.write('[ ')
            for j in range(len(array1_w[i])):
                f.write('q' + str(array1_w[i][j]) + ' ')
            f.write(']    ' + my_ch_w[0] + '    [')
            for j in range(len(to_a2_w[i])):
                f.write('q' + str(to_a2_w[i][j]) + ' ')
            f.write(']\n')

    #  writes the path for selection states with '1' input
    for i in range(len(to_b_w)):
        if to_b_w[i]:
            f.write('[ ')
            for j in range(len(array1_w[i])):
                f.write('q' + str(array1_w[i][j]) + ' ')
            f.write(']    ' + my_ch_w[1] + '    [')
            for j in range(len(to_b_w[i])):
                f.write('q' + str(to_b_w[i][j]) + ' ')
            f.write(']\n')

    #  writes the path for selection states with '1' input
    for i in range(len(to_b2_w)):
        if to_b2_w[i]:
            f.write('[ ')
            for j in range(len(array1_w[i])):
                f.write('q' + str(array1_w[i][j]) + ' ')
            f.write(']    ' + my_ch_w[1] + '    [')
            for j in range(len(to_b2_w[i])):
                f.write('q' + str(to_b2_w[i][j]) + ' ')
            f.write(']\n')


#  the main function
if __name__ == "__main__":
    my_ch, array1, to_a, to_a2, to_b, to_b2, start, end = read_file()

    write_to_file(my_ch, array1, to_a, to_a2, to_b, to_b2, start, end)
