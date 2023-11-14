import random
wanna_play = True

wins = 0
loss = 0

def game_stats():
     print("Times you have won :",(wins))
     print("Times you have lost :",(loss))

while wanna_play == True :
    you = int(input("chose rock(1) , paper(2) or scissor(3) :"))
    comp = random.randint(1,3)
    print(comp)
    print("*****************")
    if comp == you :
        print("IT's a tie")
    elif you == 1 :
        if comp == 2 :
            print(" YOU LOSS !!")
            loss = loss + 1
        elif comp == 3 :
            print(" YOU WIN !!")
            wins = wins + 1
    elif you == 2 :
            if comp == 1 :
                print(" YOU LOSS !!")
                loss = loss + 1
            elif comp == 3 :
                print(" YOU WIN !!")
                wins = wins + 1
    elif you == 3 :
            if comp == 1 :
                print(" YOU LOSS !!")
                loss = loss + 1
            elif comp == 2 :
                print(" YOU WIN !!")
                wins = wins + 1
    retry = input("Wanna retry (y/n):")
    if "y" in retry:
         wanna_play = True
    else:
         wanna_play = False
         print(game_stats())
         print("bye bye have a great day !!")
    
