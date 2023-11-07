BOARD_LENGTH = 40

two_dice_frequency = [0]*12
for i in range(6):
    for j in range(6):
        two_dice_frequency[i+j+1] += 1



def new_board(start=False):
    b = [0]*BOARD_LENGTH
    if start:
        b[0] = 1
    return b

board_captures = [new_board(True)]



def print_board():
    # print("turn", len(board_captures), "=", board_captures[-1])


    board = board_captures[-1]
    total = sum(board)


    print("turn", len(board_captures))

    for i, f in enumerate(board):
        print(i, "\t", f)
    


while True:

    print_board()

    input()


    board_captures.append(new_board())

    for x, v in enumerate(board_captures[-2]):
        for i, f in enumerate(two_dice_frequency):
            next_pos = (x+i+1) % BOARD_LENGTH
            board_captures[-1][next_pos] += v*f


