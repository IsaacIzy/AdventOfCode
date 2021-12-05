# Link to challenge: https://adventofcode.com/2021/day/4
import numpy as np

def check_winners(boards):
# For part 2, had to edit this function a bit to make sure it can handle multiple boards winning from one drawing.
# The challenge input was not working properly because only 1 board was getting removed when multiple boards were winning,
# which then compounds as more boards win, eventually leaving you with a list of all -1 boards 
    winner = False
    winners = []
    for board in boards:
        # Check for rows that are all equal
        for i in range(board.shape[0]):
            if np.all(board[i] == board[i][0]):
                print(f'Winner!\n{board}')
                winner = True
                winners.append(board)
        # Check for columns that are all equal. Can just transpose the board and do the same check we did for the rows
        temp = board.T
        for i in range(temp.shape[0]):
            if np.all(temp[i] == temp[i][0]):
                print(f'Winner!\n{board}')
                winner = True
                winners.append(board)
    if winner:
        return winner, winners
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
    # For part 2, we use mostly the same code. Just need to throw out winning boards as they come until there is only one board left
    losing_board = None
    losing_drawing = None
    for drawing in drawings:
        print(f'Drew a {drawing}, marking boards and checking for winner')
        boards = mark_boards(boards, int(drawing))
        winner, winning_boards = check_winners(boards)
        if winner and len(boards) > 1:
            # Remove winning boards from boards list
            for winning_board in winning_boards:
                boards = [board for board in boards if not (winning_board==board).all()]
        elif winner and len(boards) == 1:
            # We have a loser!
            print('The last winner has been found, what a loser ha')
            losing_board = boards[0]
            print(losing_board)
            losing_drawing = int(drawing)
            break


    # Now we need to calculate the solution for the challenge, which is the sum of unmarked squares times the losing drawing
    # Set all the marked squares to zero and sum all the values in the ndarray. Can do this all with np.sum(), but that is harder to read
    losing_board[losing_board == -1] = 0
    sum = np.sum(losing_board)
    print(f'Challenge answer: {sum*losing_drawing}')