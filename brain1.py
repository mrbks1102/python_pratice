def print_board(rows):
    for i in range(3):
        for j in range(3):
            print(rows[i][j], end='')
        print()
    print()


def init_board():
    rows = [['□'] * 3 for i in range(3)]
    return rows


rows = init_board()
print_board(rows)
