'''
A two-player Rock-Paper-Scissors game. 

Remember the rules:
                                Rock beats scissors
                                Scissors beats paper
                                Paper beats rock
'''

def main(user1,user2):
    print("------------------------------------------------------------------------------------------")
    print("\tPlayer 1: ",user1," \tPlayer 2: :",user2)
    print("------------------------------------------------------------------------------------------")
    checkRes(user1,user2)

def checkValidInput(user1,user2):
    if user1 in ('r','p','s') and user2 in ('r','p','s'):
        main(user1,user2)
    else:
        print("\n\tPlease enter a valid respose!")

def checkRes(user1,user2):
    if user1==user2:
        print("\tSame inputs, it's a TIE!!")

    elif user1=='r':
        if user2=='p':
            print("\tPlayer 2 is the winner")
        else:
            print("\tPlayer 1 is the winner")

    elif user1=='p':
        if user2=='r':
            print("\tPlayer 1 is the winner")
        else:
            print("\tPlayer 2 is the winner")

    elif user1=='s':
        if user2=='r':
            print("\tPlayer 2 is the winner")
        else:
             print("\tPlayer 1 is the winner")
    else:
        pass
              


if __name__=='__main__':
    print('''
                ROCK  - PAPER - SCISSORS GAME
                The rules:
                                Rock beats scissors
                                Scissors beats paper
                                Paper beats rock
                                Accepted input values are:
                                    R/r  -ROCK
                                    P/p - PAPER
                                    S/s - Scissors 
                ''')
    print("\t______________________________________")
    checkValidInput(input("\n\tPlayer 1: Enter Choice(r,p or s): ").lower(),input("\n\tPlayer 2: Enter Choice(r,p or s): ").lower())
