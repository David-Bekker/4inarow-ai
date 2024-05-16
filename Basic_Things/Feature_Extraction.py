def find_row_traits(gameboard, player):
    # CHECK_ROWS
    r3_nda = 0
    r3_da = 0
    r2_2n = 0
    r2_1n_1d = 0
    r2_2d = 0
    total_not_direct_positions = []
    total_direct_positions = []
    for y in range(6):
        not_direct_positions = []
        direct_positions = []
        for constent in range(4):
            sum_p = 0
            sum_0_nda = 0
            sum_0_da = 0
            newly_saved_position = 7
            for x in [0 + constent, 1 + constent, 2 + constent, 3 + constent]:
                if gameboard[y][x] == player:
                    sum_p += 1
                elif gameboard[y][x] == 0:
                    if y < 5:
                        if gameboard[y + 1][x] == 0:
                            if x not in not_direct_positions:
                                sum_0_nda += 1
                                newly_saved_position = x
                        else:
                            if x not in direct_positions:
                                sum_0_da += 1
                                newly_saved_position = x
                    else:
                        if x not in direct_positions:
                            sum_0_da += 1
                            newly_saved_position = x
                else:
                    break
            if sum_p == 3 and sum_0_nda == 1:
                r3_nda += 1
                not_direct_positions.append(newly_saved_position)
            elif sum_p == 3 and sum_0_da == 1:
                r3_da += 1
                direct_positions.append(newly_saved_position)
            elif sum_p == 2 and sum_0_nda == 2:
                r2_2n += 1
            elif sum_p == 2 and sum_0_da == 1 and sum_0_nda == 1:
                r2_1n_1d += 1
            elif sum_p == 2 and sum_0_da == 2:
                r2_2d += 1
        for i in not_direct_positions:
            total_not_direct_positions.append([y, i])
        for i in direct_positions:
            total_direct_positions.append([y, i])
    return [r3_nda, r3_da, r2_2n, r2_1n_1d, r2_2d,
            total_not_direct_positions, total_direct_positions]

def find_column_traits(gameboard, player):
    c3_da = 0
    c2_da = 0
    direct_positions = []
    for x in range(7):
        for constent in range(3):
            sum_p = 0
            sum_0 = 0
            newly_saved_position = 7
            for y in [5 - constent, 4 - constent, 3 - constent, 2 - constent]:
                if gameboard[y][x] == player:
                    sum_p += 1
                elif gameboard[y][x] == 0:
                    sum_0 += 1
                    newly_saved_position = y
                else:
                    break
            if sum_p == 3 and sum_0 == 1:
                direct_positions.append([newly_saved_position, x])
                c3_da += 1
                break
            elif sum_p == 2 and sum_0 == 2:
                c2_da += 1
    return [c3_da, c2_da, direct_positions]

def find_first_diagonal_traits(gameboard, player):
    d3_nda = 0
    d3_da = 0
    d2_2n = 0
    d2_1n_1d = 0
    d2_2d = 0
    total_not_direct_positions = []
    total_direct_positions = []
    for j in range(3):
        for i in range(4):
            # First_Diagonal
            sum_p = 0
            sum_0_nda = 0
            sum_0_da = 0
            position = 7
            for x in range(4):
                if gameboard[x + j][x + i] == player:
                    sum_p += 1
                elif gameboard[x + j][x + i] == 0:
                    position = [x + j, x + i]
                    if x + j < 5:
                        if gameboard[x + j + 1][x + i] == 0:
                            sum_0_nda += 1
                        else:
                            sum_0_da += 1
                    else:
                        sum_0_da += 1
                else:
                    break
            if sum_p == 3 and sum_0_nda == 1:
                d3_nda += 1
                total_not_direct_positions.append(position)
            elif sum_p == 3 and sum_0_da == 1:
                d3_da += 1
                total_direct_positions.append(position)
            elif sum_p == 2 and sum_0_da == 0 and sum_0_nda == 2:
                d2_2n += 1
            elif sum_p == 2 and sum_0_da == 1 and sum_0_nda == 1:
                d2_1n_1d += 1
            elif sum_p == 2 and sum_0_da == 2:
                d2_2d += 1
    return [d3_nda, d3_da, d2_2n, d2_1n_1d, d2_2d,
            total_not_direct_positions, total_direct_positions]

def find_second_diagonal_traits(gameboard, player):
    d3_nda = 0
    d3_da = 0
    d2_2n = 0
    d2_1n_1d = 0
    d2_2d = 0
    total_not_direct_positions = []
    total_direct_positions = []
    for j in range(3):
        for i in range(4):
            sum_p = 0
            sum_0_nda = 0
            sum_0_da = 0
            position = 7
            for x in range(4):
                # Second_Diagonal
                if gameboard[5 - (x + j)][x + i] == player:
                    sum_p += 1
                elif gameboard[5 - (x + j)][x + i] == 0:
                    position = [5 - (x + j), x + i]
                    if (5 - (x + j)) < 5:
                        if gameboard[6 - (x + j)][x + i] == 0:
                            sum_0_nda += 1
                        else:
                            sum_0_da += 1
                    else:
                        sum_0_da += 1
                else:
                    break
            if sum_p == 3 and sum_0_nda == 1:
                d3_nda += 1
                total_not_direct_positions.append(position)
            elif sum_p == 3 and sum_0_da == 1:
                d3_da += 1
                total_direct_positions.append(position)
            elif sum_p == 2 and sum_0_da == 0 and sum_0_nda == 2:
                d2_2n += 1
            elif sum_p == 2 and sum_0_da == 1 and sum_0_nda == 1:
                d2_1n_1d += 1
            elif sum_p == 2 and sum_0_da == 2:
                d2_2d += 1
    return [d3_nda, d3_da, d2_2n, d2_1n_1d, d2_2d,
            total_not_direct_positions, total_direct_positions]

def positions_count(big_list_of_direct_positions):
    positions = []
    new_positions = big_list_of_direct_positions
    for i in range(len(new_positions)):
        for j in new_positions[i]:
            if j not in positions:
                positions.append(j)
    return [len(positions), positions]

def find_up_forks(direct_positions, indirect_positions):
    direct_forks_count = 0
    indirect_forks_count = 0
    for i in indirect_positions:
        for j in direct_positions:
            if i[1] == j[1] and i[0] == j[0] - 1:
                direct_forks_count += 1
    for i in indirect_positions:
        for j in indirect_positions:
            if i[1] == j[1] and i[0] == j[0] - 1:
                indirect_forks_count += 1
    return [direct_forks_count, indirect_forks_count]
