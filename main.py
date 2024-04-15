import random

# Game variables
players = ['player', 'computer']  # List of player names
game_array = [" ", " ", " ", " ", " ", " ", " ", " ", " ", ]  # Represents the game board


def rules():
    """Prints the tic-tac-toe board layout with numbered positions."""
    print("--- Mark the spaces using numbers ---")
    print(" 1 ", " 2 ", " 3 ", sep='|')
    print("-----------")
    print(" 4 ", " 5 ", " 6 ", sep='|')
    print("-----------")
    print(" 7 ", " 8 ", " 9 ", sep='|')


# Function to print the current state of the game board
def game_status(array):
    count = 0
    text = ''
    for item in array:
        text += " "+item+" |"
        count += 1
        if count % 3 == 0:

            print(text[0:-1])
            text = ''
            if count != 9:
                print("-----------")


# Function to check if all elements in a list are the same
def are_same_all(items):
    for item in items:
        if item != items[0]:
            return False
    return True


def is_same_index(indexs):
    same_indexs = []
    for index in range(len(indexs) - 1):
        if indexs[index] in same_indexs:
            continue

        for j in range(index + 1, len(indexs)):
            if indexs[index] == indexs[j]:
                same_indexs.append(indexs[j])
    return same_indexs

# Function to check if any win conditions are met
def checked_game(game):
    success_array = []
    success_index = []
    items = []
    # Check if there is a match in the line
    for row in range(9):
        items.append(game[row])
        success_index.append(row)
        if len(items) == 3:
            if ' ' not in items:
                if are_same_all(items):
                    success_array.append(success_index)

            success_index = []
            items = []
    # To check three columns
    for i in range(3):
        items = []

        index = i
        for col in range(3):
            if not col == 0:
                index = index + 3
            success_index.append(index)
            items.append(game[index])
        if ' ' not in items:
            if are_same_all(items):
                success_array.append(success_index)
        items = []
        success_index = []

        # right and left cross control with index
        if i == 0:
            for cross in range(3):
                index = cross * 4
                items.append(game[index])
                success_index.append(index)
            if ' ' not in items:
                if are_same_all(items):
                    success_array.append(success_index)
            success_index = []
        elif i == 2:
            for cross in range(1, 4):
                index = cross * 2
                items.append(game[index])
                success_index.append(index)
            if ' ' not in items:
                if are_same_all(items):
                    success_array.append(success_index)
            success_index = []

    return success_array


def computer(array, mark, mode):

    if mode == 'e':
        while True:
            num = random.randrange(0, 9)
            if array[num] == ' ':
                array[num] = mark
                break
    else:
        # The current game series was copied and possible areas for AI were found.
        possible_area = []
        copy = array.copy()
        for i in range(9):
            if copy[i] == ' ':
                copy[i] = mark
        result = checked_game(copy)
        if len(result) > 0:
            for items in result:
                for index in items:
                    if array[index] == " ":
                        possible_area.append(index)

        # Identification of advantageous intersection areas
        if len(possible_area) > 0:
            for i in range(3):
                result = is_same_index(possible_area)
                if len(result) > 0:
                    possible_area = result

                else:
                    ai_choose = random.choice(possible_area)
                    array[ai_choose] = mark
                    if mode != 'v':  # In the hardest mode, it allows the computer to win by making multiple moves 😊
                        break


# Main game loop
def game_start():
    start_choose = [True, False]
    status = random.choice(start_choose)
    rules()
    print("Welcome to a simple Tic-Tac-Toe game!")
    name = input(" What's ur name? ")
    players[0] = name

    while True:
        difficulty = input('What is the game difficulty? Easy , hard , very hard. (e or h or v ) ')
        if 'e' == difficulty.lower() or difficulty.lower() == 'h' or difficulty.lower() == 'v':
            break
        else:
            print(f'Please enter a valid option. "{difficulty}" expression is not defined')
    mode = difficulty

    while True:
        if status:
            player = players[0]
            mark = "X"
        else:
            player = players[1]
            mark = 'O'
            computer(game_array, mark, mode)
        print(f"Player {player} turn to play")
        try:
            if status:
                answer = int(input('Select numbers and put sign e.g(1, 2 or 3 ...): '))
                if 1 <= answer <= 9:

                    if game_array[answer-1] != ' ':
                        print('You cannot mark an already filled position. Please select an empty area!')
                        continue
                else:
                    raise ValueError
                game_array[answer-1] = mark

            status = not status
        except ValueError:
            print('Please enter numbers between 1 and 9!')
            continue
        game_status(game_array)
        if len(checked_game(game_array)) > 0:
            print(f'The game is over, the winner is {player}!')
            break


game_start()

