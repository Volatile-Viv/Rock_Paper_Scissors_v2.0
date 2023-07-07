import random

def intro():
    intro_print ='''
        = = = = = = = = = = ROCK, PAPER AND SCISSORS v2.0 = = = = = = = = = =
        ---------------------------------------------------------------------------
        This is the project based on a very famous hand game that you may have
        played with your friends in your childhood. It is widely known as
        Rock, paper and Scissors.

        YALA YOLO !!!
        ---------------------------------------------------------------------------

        PROJECT TITLE: ROCK, PAPER AND SCISSORS
        VERSION: v2.0

        Whats's new?
        1. This version have levels now.
        2. You will get a better User Interface(I think so)
    '''

    print(intro_print)


def menu():
    print('''
    = = = = = = = = = = = = = MAIN MENU = = = = = = = = = = = = = =

         /              PRESS 'S' FOR START           \\
        /                                              \\
       |                PRESS 'H' FOR HELP              |
        \\                                              /
         \\              PRESS 'Q' FOR EXIT            /

    = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    ''')

    k = input('Enter here --> ')
    k = k.upper()

    if k == 'S':
        game()

    elif k == 'H':
        level_list = ['BRONZE', 'SILVER', 'GOLD', 'PLATINUM', 'LEGEND', 'ULTRA LEGEND', 'THE REAL GAMER']

        print(f'''

        This game contains 7 levels ({level_list})

        Points < 0 : Bronze
        Points < 5 : Silver
        Points < 10 : Gold
        Points < 20 : Platinum
        Points < 30 : Diamond
        Points < 50 : Legend
        Points < 100 : The Real Gamer
        
        TIP : SUCCESS TAKES TIME !!!
        \n\n''')

        game()

    elif k == 'Q':
        exit()

    else:
        print("Invalid input.\n\n")


def game():
    print('''
             = = = = = = = = = = =   GAME STARTED   = = = = = = = = = = =

                      /            PRESS 'R' FOR ROCK            \\
                     /                                            \\
                    |              PRESS 'P' FOR PAPER             |
                     \\                                            /
                      \\            PRESS 'S' FOR SCISSOR         /

                                   Press 'Q' to Quit the game

             = = = = = = = = = = = = = = ==== = = = = = = = = = = = = = =
             ''')
    rps = ['R', 'P', 'S']
    rps2 = ['ROCK', 'PAPER', 'SCISSOR']
    points = 0

    level_list = ['BRONZE', 'SILVER', 'GOLD', 'PLATINUM', 'LEGEND', 'ULTRA', 'THE REAL GAMER']
    level = 'BRONZE'

    user = 'R'
    wish = ['Yoho', 'You are winning', 'You can beat him', 'You got 1 point', 'Nice luck']
    wish1 = ['OOPS', 'You are losing', 'This can beat you', 'You lost 1 point', 'Bad luck']
    l = random.randint(0, 4)

    while user != 'Q':
        user = input('Enter here -> ')
        user = user.upper()

        k = random.randint(0, 2)
        pc = rps[k]
        pc_print = rps2[k]

        if user != 'R' and user != 'P' and user != 'S' and user != 'Q':
            print('Invalid Input !!!')

        elif user == 'Q':
            break

        else:
            if user == pc:
                print("Computer --> ", pc_print)
                print("Wow !!! Nice match with Computer")
                print("Total points --> ", points)

            elif user == 'R' and pc == 'P':
                points = points - 1
                print("Computer --> ", pc_print)
                print(wish1[l])
                print("Total points --> ", points)

            elif user == 'R' and pc == 'S':
                points = points + 1
                print("Computer --> ", pc_print)
                print(wish[l])
                print("Total points --> ", points)

            elif user == 'P' and pc == 'R':
                points = points + 1
                print("Computer --> ", pc_print)
                print(wish[l])
                print("Total points --> ", points)

            elif user == 'P' and pc == 'S':
                points = points - 1
                print("Computer --> ", pc_print)
                print(wish1[l])
                print("Total points --> ", points)

            elif user == 'S' and pc == 'R':
                points = points - 1
                print("Computer --> ", pc_print)
                print(wish1[l])
                print("Total points --> ", points)

            elif user == 'S' and pc == 'P':
                points = points + 1
                print("Computer --> ", pc_print)
                print(wish[l])
                print("Total points --> ", points)

            else:
                print('Error')
            print('\n\n')

    if points <= 0:
        level = 'Bronze'
        
    elif points < 5:
        level = 'Silver'

    elif points < 10:
        level = 'Gold'

    elif points < 20:
        level = 'Platinum'

    elif points < 30:
        level = 'Diamond'

    elif points < 50:
        level = 'Legend'

    elif points < 100:
        level = 'The Real Gamer'

    else:
        level = 'God??? Is that you???'

    print("\n\nThanks for playing this game !!!")
    print('I hope you have enjoyed playing this game.')

    print("\nTotal points --> ", points)
    print("Level: ", level)


intro()
menu()

print('\n\t- Akriti and Vivek')
