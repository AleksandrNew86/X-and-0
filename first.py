
game = [[" ", "1", "2", "3"], ["1", " ", " ", " "], ["2", " ", " ", " "], ["3", " ", " ", " "]]
first_step = True
end_game = False


def output(g):
    for i in range(len(g)):
        print(' | '.join(g[i]))
        if i == 3:
            break
        print("______________")


def check_win(g):
    for i in range(1,4):
        if g[i][1] == g[i][2] == g[i][3] != " " or\
        g[1][i] == g[2][i] == g[3][i] != " ":
            return True
    if g[1][1] == g[2][2] == g[3][3] != " " or\
    g[1][3] == g[2][2] == g[3][1] != " ":
        return True
    else:
        return False


def handle_input(c):
    c = c.split(",")
    if (c[0] in ["1", "2", "3"]) and (c[1] in ["1", "2", "3"]) and game[int(c[0])][int(c[1])] == " ":
        return True
    else:
        return False


def new_game():
    _continue_ = input("Do you want to continue a new game? (Y/N): ").lower()
    if _continue_ == "y":
        global game
        global first_step
        game = [[" ", "1", "2", "3"], ["1", " ", " ", " "], ["2", " ", " ", " "], ["3", " ", " ", " "]]
        first_step = True
        print("A new game:")
        output(game)
    elif _continue_ == "n":
        global end_game
        end_game = True
    else:
        print("The wrong answer")
        new_game()


output(game)

while True:
    if end_game:
        break
    full_field = True
    for i in game[1:]:
        for j in i[1:]:
            if j == " ":
                full_field = False
                break
    if full_field:
        _continue = input("All cells are busy. It is a draw. Do you want to begin again? (Y/N): ").lower()
        if _continue == "y":
            game = [[" ", "1", "2", "3"], ["1", " ", " ", " "], ["2", " ", " ", " "], ["3", " ", " ", " "]]
            first_step = True
            print("A new game:")
            output(game)
        elif _continue == "n":
            print("The game is ended.")
            break
        else:
            print("The wrong answer")
            continue
    if end_game:
        break
    if first_step:
        a = input("The gamer 'X' enter position in format 'row','column': ")
        if handle_input(a):
            a = a.split(",")
            game[int(a[0])][int(a[1])] = "X"
            output(game)
            first_step = False
            if check_win(game):
                print("The Gamer 'X' won! Congratulation!")
                new_game()
        else:
            print("The wrong format or your input is already busy.")
    else:
        b = input("The gamer '0' enter position in format 'row','column': ")
        if handle_input(b):
            b = b.split(",")
            game[int(b[0])][int(b[1])] = "0"
            output(game)
            first_step = True
            if check_win(game):
                print("The Gamer '0' won! Congratulation!")
                new_game()
                break
        else:
            print("The wrong format or your input is already busy.")
