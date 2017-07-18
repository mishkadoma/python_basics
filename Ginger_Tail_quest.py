from sys import exit

amount_of_lives = 3

def get_player_name():
    player_name = raw_input("> ")
    return player_name

def game_start():
    """
    All that block purpose is to start the game
    """
    global amount_of_lives
    if amount_of_lives < 1:
        print "You have no more lives."
        exit(1)
    else:
        print "you have %d lives" % amount_of_lives

    print "Enter your name: \t"

    player_name = get_player_name()

    print "I greet you, %s. " % player_name, "Welcome to the Royal Quest."
    print "You are Ginger Tail, i guess? (put 'yes' or 'no')"

    ginger = raw_input('> ')

    if ginger == 'yes' or ginger == 'y':
        print "You are all right then. I'd like to play with you."
        print "The giant rock is falling on your head right now. Choose what to do: "
        print "1. Step left . 2. Step right. 3. Stand still."

        step_choice = raw_input('oO0Oo.> ')

        if step_choice == '1' or step_choice == 'left':
            print "Woahh! You are alive! But you fall into pit full of snakes. \nThey doesn't look friendly. Get out and run NOW.."
            print "Press 'Enter' to get out"
            raw_input()
            level_2()
        elif step_choice == '2' or step_choice == 'right':
            print "This rock was so giant. And sadly you was a bit slow. You are dead.. Take other try?"
            amount_of_lives -= 1
            game_over()
        elif step_choice == '3' or step_choice == 'still' or step_choice == 'stand':
            print "Maybe you'd miss my speech. I said the ENORMOUS GIAND ROCK is FALLING onto your HEAD. You're dead OFK. So what did you expect?"
            amount_of_lives -= 1
            game_over()
        else:
            print "Wrong option. An error occurse"
            exit(1)
    elif ginger == 'no' or ginger == 'n':
        print "You cannot play my game 'cause you are not Ginger Tall. \nMay change your mind and come back later?"
        exit(1)
    else:
        print "I can't understand you. Just type 'yes' or 'no' next time"
        game_over()

def level_2():
    """Under construction"""
    print "Hidden level!"


def game_over():
    print "Press 'Enter' to give it another try. Press 'CTRL + C' to quit"
    raw_input()
    game_start()

game_start()
