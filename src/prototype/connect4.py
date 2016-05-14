COLUMNS = 7
ROWS = 6
TOTAL_MOVES = ROWS * COLUMNS
WIN = 4

board = [ [] for column in range(COLUMNS) ]

def get_cell(board, cell):
    x, y = cell
    if (x >= 0) and (y >= 0):
        try:
            return board[x][y]
        except IndexError:
            return None
    else:
        return None

def display_board(board):
    for row in reversed(range(ROWS)):
        ascii_row = ''
        for column in range(COLUMNS):
            cell = get_cell(board, (column, row))
            if cell is None:
                symbol = '.'
            elif cell:
                symbol = '+'
            else:
                symbol = 'x'
            ascii_row = ascii_row + symbol
        print(ascii_row)
    label = ''.join(str(column) for column in range(COLUMNS))
    print(label)

def get_column():
    while True:
        input_ = input('Column: ')
        try:
            column = int(input_)
            if 0 <= column < COLUMNS:
                break
            else:
                print('Not a valid column')
        except:
            print('Not an integer')
    return column

def check_win(player, board, lastmove):
    lines = [[(1,1),(-1,-1)],[(1,0),(-1,0)],[(1,-1),(-1,+1)],[(0,-1)]]
    for line in lines:
        longest = 1
        for d in line:
            p = lastmove
            q = (p[0]+d[0], p[1]+d[1])
            while player == get_cell(board, q):
                longest = longest + 1
                p = q
                q = (p[0]+d[0], p[1]+d[1])
            if longest >= WIN:
                return True
    return False

display_board(board)

def move(player, board, column):
    board[column].append(player)
    row = len(board[column]) - 1
    return (column,row)

moves = 0
win = False
while moves < TOTAL_MOVES:
    if moves % 2 == 0:
        player = True
    else:
        player = False

    column = get_column()
    if len(board[column]) < ROWS:
        lastmove = move(player, board, column)
        win = check_win(player, board, lastmove)
        moves = moves + 1
    else:
        print('Column full! Try again.')
    print('moves: ' + str(moves))
    display_board(board)
    if win:
        print('Connect 4!')
        break
