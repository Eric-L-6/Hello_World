#Udemy milestone project 1
#Learnt error handling + game logic
#Knots and crosses using 2d list


#Functions

#given a 3 x 3 2d array, will print in tic tac toe format
def print_board(game_arr):
    print("   0   1   2")
    print(f"0  {game_arr[0][0]} | {game_arr[0][1]} | {game_arr[0][2]}")
    print("   ---------")
    print(f"1  {game_arr[1][0]} | {game_arr[1][1]} | {game_arr[1][2]}")
    print("   ---------")
    print(f"2  {game_arr[2][0]} | {game_arr[2][1]} | {game_arr[2][2]}")

#convert input string of form "x,y" as tuple
def convert_coord(coord):
    return tuple(coord.split(","))

#alternates user and returns 1 or 2 
def alternate(user):
    return (user + 1) % 2

#check win condition based on current x and y
def check_win(user_pos, game_arr):
    x,y = user_pos
    
    #check current row:
    if game_arr[x][0] == game_arr[x][1] == game_arr[x][2]:
        return True
    
    #check current column
    elif game_arr[0][y] == game_arr[1][y] == game_arr[2][y]:
        return True
    
    #always check diagonals
    elif (game_arr[0][0] == game_arr[1][1] == game_arr[2][2]) or (game_arr[0][2] == game_arr[1][1] == game_arr[2][0]):
        if game_arr[1][1] != " ":
            return True
    
    #no win condition met
    return False

#take in player input coord
#checks if valid
#updates and prints board

def user_input(game_arr, user):

    valid_form = False
    valid_bound = False
    valid_pos = False
    bounds = [0,1,2]
    coord = " , "
    
    while (valid_form == False or valid_bound == False or valid_pos == False):
        print_board(game_arr)
        print(" ")
        coord = input("Please input your desired coordinate in the form 'x,y': ")
        
        #first: check correct format
        if (len(coord) == 3 and coord[1] == ','):
            valid_form = True
        else:
            #clear_output()
            print("\033c")

            print("Your coordinates are in the wrong format.")
            continue

        #convert into x,y
        x,y = convert_coord(coord)
        x = int(x)
        y = int(y)

        #second: check within bounds
        if (x in bounds and y in bounds):
            valid_bound = True
        else:
            #clear_output()
            print("\033c")

            print("Coordinates need to be in the range 0-2")
            continue
        
        #check if position is non-empty
        if game_arr[x][y] == " ":
            valid_pos = True
        else:
            #clear_output()
            print("\033c")

            print("That position is already taken")
            continue
            
    #inserting onto game and showing users
    game_arr[x][y] = user_dict[str(user)]
    return (x,y)

#check if player wants to replay
def replay():
    print("Do you want to play again?")
    return input("Yes or No ").lower() == "yes"

#"Main function"
if __name__ == "__main__":

    play = True
    user_dict = {"0": "X", "1":"O"}

    while play == True:

        game_arr = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
        #can be initialised as game_arr = [[" "]*3]*3
        user = 0
        win = False
        tie = 0

        while win == False and tie < 9:
            print(f"Player {user + 1}")
            user_pos = user_input(game_arr,user)
            win = check_win(user_pos, game_arr)
            user = alternate(user)
            tie += 1
            #clear_output()
            print("\033c")


        print_board(game_arr)
        if win == True:
            print (f"Player {alternate(user) + 1} wins!")
        elif tie == 9:
            print("Tie! No one wins")
        
        play = replay()
        #clear_output()
        print("\033c")


    #player has exited
    print("Thank you for playing!")

