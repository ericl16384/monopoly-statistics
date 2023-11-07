BOARD_LENGTH = 40

two_dice_frequency = [0] * (12+1)
for i in range(6):
    for j in range(6):
        two_dice_frequency[i+j+1+1] += 1

# print([i for i in enumerate(two_dice_frequency)])
# input()



class Board:
    def __init__(self, previous_board) -> None:
        self.tile_frequencies = [0] * BOARD_LENGTH

        if previous_board == None:
            self.tile_frequencies[0] = 1
        
        self.doubles1_frequencies = [0] * BOARD_LENGTH
        self.doubles2_frequencies = [0] * BOARD_LENGTH
        self.doubles3_frequencies = [0] * BOARD_LENGTH
    
    def freq_sum(self):
        return sum(self.tile_frequencies)
    


# def new_board(start=False):
#     b = [0]*BOARD_LENGTH
#     if start:
#         b[0] = 1
#     return b

board_captures = [Board(None)]



def print_board():
    # print("turn", len(board_captures), "=", board_captures[-1])


    board = board_captures[-1]
    total = board.freq_sum()


    print("turn", len(board_captures))

    print("i \t f \t d1 \t d2 \t d3_jail")
    for i, f in enumerate(board.tile_frequencies):
        print(i, "\t", f, "\t", board.doubles1_frequencies[i], "\t", board.doubles2_frequencies[i], "\t", board.doubles3_frequencies[i])


def generate_next_board():
    previous_board = board_captures[-1]
    board = Board(previous_board)

    board_captures.append(board)

    for x, v in enumerate(previous_board.tile_frequencies):

        # basic movement
        for i, f in enumerate(two_dice_frequency):
            next_pos = (x+i) % BOARD_LENGTH
            board.tile_frequencies[next_pos] += v*f
        
        # doubles rules
        next_doubles = (x+12) % BOARD_LENGTH
        board.doubles1_frequencies[next_doubles] += v
        board.doubles2_frequencies[next_doubles] += previous_board.doubles1_frequencies[x]
        board.doubles3_frequencies[next_doubles] += previous_board.doubles2_frequencies[x]



while True:

    print_board()

    input()

    generate_next_board()


