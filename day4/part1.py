# Link to challenge: https://adventofcode.com/2021/day/4
import numpy as np

def check_winners(boards):
    for board in boards:
        # Check for rows that are all equal
        for i in range(board.shape[0]):
            if np.all(board[i] == board[i][0]):
                print(f'Winner!\n{board}')
                return True, board
        # Check for columns that are all equal. Can just transpose the board and do the same check
        temp = board.T
        for i in range(temp.shape[0]):
            if np.all(temp[i] == temp[i][0]):
                print(f'Winner!\n{board}')
                return True, board
    print(f'no winner :(\n{board}')
    return False, None

def mark_boards(boards, drawing):
    # assuming boards will not have any negative values, so marking the boards with -1
    new_boards = []
    for board in boards:
        board[board == drawing] = -1
        new_boards.append(board)
    return new_boards

if __name__ == '__main__':
    # Seperated the input into two files, one for drawing numbers, one for the boards
    drawings = []
    with open('drawings.txt') as input:
        drawings = input.readline().split(',')
    # Numpy to the rescue. loadtext creates an ndarray containing all the boards as one squashed array
    boards_temp = np.loadtxt('boards.txt', dtype=int)
    # Split the big array into a list of the boards. Can just split vertically every 5 rows
    boards = np.vsplit(boards_temp, boards_temp.shape[0]/5)

    # Let the game begin!
    winning_board = None
    winning_drawing = None
    for drawing in drawings:
        print(f'Drew a {drawing}, marking boards and checking for winner')
        boards = mark_boards(boards, int(drawing))
        winner, board = check_winners(boards)
        if winner:
            winning_board = board
            winning_drawing = int(drawing)
            break

    # Now we need to calculate the solution for the challenge, which is the sum of unmarked squares times the winning drawing
    # Set all the marked squares to zero and sum all the values in the ndarray. Can do this all with np.sum(), but that is harder to read
    winning_board[winning_board == -1] = 0
    sum = np.sum(winning_board)
    print(f'Challenge answer: {sum*winning_drawing}')