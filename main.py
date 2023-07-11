def main():
    intro()

    map = [["","",""],
           ["","",""],
           ["","",""]]
    
    winner = ""
    curr_player = "O"
    while winner == "":
        x,y = input(f"Current Player: {curr_player}:    ").split(",")
        x,y = int(x),int(y)
        map[x][y] = curr_player
        print(map)


def intro():
    print("Tic Tac Toe")
    print("Instructions:")
    print("O goes first, X follows")
    print("enter your position with the help below:")

    print("0,0 | 0,1 | 0,2")
    print("----------------")
    print("1,0 | 1,1 | 1,2")
    print("----------------")
    print("2,0 | 2,1 | 2,2")

def check_winner(map):
    print("Checking Winner")

main()