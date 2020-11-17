arr = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
x_turn = True
game_not_ended = True


def print_field():
    field = """---------
| {} {} {} |
| {} {} {} |
| {} {} {} |
---------""".format(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5],
                    arr[6], arr[7], arr[8])
    print(field)


cells = ["1 3", "2 3", "3 3", "1 2", "2 2", "3 2", "1 1", "2 1", "3 1"]


def get_input():
    global x_turn
    while game_not_ended:
        move = input("Enter coordinates: ")
        digit_checker = move.replace(" ", "").isdigit()

        if not digit_checker or len(move) < 2:
            print("You should enter numbers!")
            get_input()
        elif move not in cells:
            print("Coordinates should be from 1 to 3!")
            get_input()
        else:
            cell_checker(move)


def cell_checker(correct_input):
    cell_1_1 = arr[6]
    cell_1_2 = arr[3]
    cell_1_3 = arr[0]
    cell_2_1 = arr[7]
    cell_2_2 = arr[4]
    cell_2_3 = arr[1]
    cell_3_1 = arr[8]
    cell_3_2 = arr[5]
    cell_3_3 = arr[2]

    if correct_input == "1 1" and cell_1_1 != " ":
        print("This cell is occupied! Choose another one!")
        get_input()
    elif correct_input == "1 2" and cell_1_2 != " ":
        print("This cell is occupied! Choose another one!")
        get_input()
    elif correct_input == "1 3" and cell_1_3 != " ":
        print("This cell is occupied! Choose another one!")
        get_input()
    elif correct_input == "2 1" and cell_2_1 != " ":
        print("This cell is occupied! Choose another one!")
        get_input()
    elif correct_input == "2 2" and cell_2_2 != " ":
        print("This cell is occupied! Choose another one!")
        get_input()
    elif correct_input == "2 3" and cell_2_3 != " ":
        print("This cell is occupied! Choose another one!")
        get_input()
    elif correct_input == "3 1" and cell_3_1 != " ":
        print("This cell is occupied! Choose another one!")
        get_input()
    elif correct_input == "3 2" and cell_3_2 != " ":
        print("This cell is occupied! Choose another one!")
        get_input()
    elif correct_input == "3 3" and cell_3_3 != " ":
        print("This cell is occupied! Choose another one!")
        get_input()
    else:
        make_move(correct_input)


def make_move(correct_value):
    global x_turn
    if x_turn:
        arr[cells.index(correct_value)] = "X"
        x_turn = False
    else:
        arr[cells.index(correct_value)] = "O"
        x_turn = True

    print_field()
    game_state_checker()


def game_state_checker():
    global game_not_ended
    if ((arr[0] == "X" and arr[1] == "X" and arr[2] == "X")
            or (arr[0] == "X" and arr[4] == "X" and arr[8] == "X")
            or (arr[0] == "X" and arr[3] == "X" and arr[6] == "X")
            or (arr[1] == "X" and arr[4] == "X" and arr[7] == "X")
            or (arr[2] == "X" and arr[5] == "X" and arr[8] == "X")
            or (arr[2] == "X" and arr[4] == "X" and arr[6] == "X")
            or (arr[3] == "X" and arr[4] == "X" and arr[5] == "X")
            or (arr[6] == "X" and arr[7] == "X" and arr[8] == "X")):
        print("X wins")

        game_not_ended = False

    elif ((arr[0] == "O" and arr[1] == "O" and arr[2] == "O")
            or (arr[0] == "O" and arr[4] == "O" and arr[8] == "O")
            or (arr[0] == "O" and arr[3] == "O" and arr[6] == "O")
            or (arr[1] == "O" and arr[4] == "O" and arr[7] == "O")
            or (arr[2] == "O" and arr[5] == "O" and arr[8] == "O")
            or (arr[2] == "O" and arr[4] == "O" and arr[6] == "O")
            or (arr[3] == "O" and arr[4] == "O" and arr[5] == "O")
            or (arr[6] == "O" and arr[7] == "O" and arr[8] == "O")):
        print("O wins")
        game_not_ended = False

    elif arr[0] != " " and arr[1] != " " and arr[2] != " " and arr[3] != " " and arr[4] != " " and arr[5] != " " and arr[6] != " " and arr[7] != " " and arr[8] != " ":
        print("Draw")
        game_not_ended = False


print_field()
get_input()
input()
