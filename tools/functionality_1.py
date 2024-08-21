import random


#                                           WORKING FINE

def convert_try(int_to_str = False, str_to_int = False, data = None ):
    if (int_to_str == True and str_to_int == True) or (int_to_str == False and str_to_int == False):
        return 
    elif int_to_str == True:
        try :
            data = str(data)
        except:
            pass
    elif str_to_int == True:
        try:
            data = int(data)
        except:
            pass
    return data




#                                           WORKING FINE
def compare_moves (player_move , bot_move ):
    if player_move == bot_move:
        return "DRAW"
    elif player_move != bot_move:
        if player_move == "rock":
            if bot_move == "scissor":
                winner_move= player_move
            elif bot_move == "paper":
                winner_move= bot_move
        elif player_move == "paper":
            if bot_move == "scissor":
                winner_move= bot_move
            elif bot_move == "rock":
                winner_move= player_move
        elif player_move == "scissor":
            if bot_move == "paper":
                winner_move= player_move
            elif bot_move == "rock":
                winner_move=  bot_move
    return winner_move




#                                                      WORKING FINE
def bot_move():
    int_move = random.randint(0,2)
    moves = ["rock","paper","scissor"]
    final_move = moves[int_move]
    return final_move
    



#                                                       WORKING FINE 
def move_anouncer(player_move, bot_move, winner_move):
    if winner_move==player_move:
        final =  f"Players move was {player_move} and Bot move was {bot_move}, thus Player won!!!!"
    elif winner_move== bot_move:
        final = f"Players move was {player_move} and Bot move was {bot_move}, thus Bot won...."
    elif winner_move == "draw":
        final = f"Players move was {player_move} and Bot move was {bot_move}, thus It was a DRAW"
    return final




def input_process_data(convert_try = convert_try):
    player_move = input("1.Rock\n2.Paper\n3.Scissor\nEnter your move : ")
    # try:
    #     player_move = int(player_move)
    # except:
    #     pass
    player_move = convert_try(str_to_int = True, data = player_move)
    moves = ["rock","paper","scissor"]
    print(type(player_move))
    if type(player_move) == type(int):
        try:
            player_move = moves[player_move-1]        
        except: 
            player_move = "invalid"
    elif type(player_move) == type(str):
        if player_move[0].lower() == "r":
            player_move = moves[0]
        elif player_move[0].lower() == "p":
            player_move = moves[1]
        elif player_move[0].lower() == "s":
            player_move= moves[-1] 
        else:
            player_move = "invalid"
    return player_move





def services(command):
    functionalities =["Intro", "Rules"]
    intro = """Hello user.Welcome to my game.\nYou have to enter a move and our randomated simulted player will play one against you.\nJust like a real life player."""
    rules = """This game is about choosing winner on a randomized fasion.\nEach round of this can be played only between two players.\nIn this case one player will be our api.\nSO,,,,\nplayer will type his move and then itll be processed that who own that round.\nROCK beats SCISSORS.\nSCISSORS beats PAPER.\nPAPER beats ROCK."""
    if command == "intro":
        return intro
    elif command == "rules":
        return rules
    elif command == "functionalities":
        return functionalities



#                                                               TESTING AREA

# print(compare_moves("rock","paper"))
# print(compare_moves("paper","scissor"))
# print(compare_moves("paper","paper"))


# print(bot_move())


print(input_process_data())