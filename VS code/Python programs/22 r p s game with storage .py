import random
wanna_play = True

with open("rps_win_score","r") as w:
     w = int(w.read())
with open("rps_loss_score","r") as l:
     l = int(l.read())

wins = w
loss = l

def game_stats():
     print("Times you have won :",(wins))
     print("Times you have lost :",(loss))

while wanna_play == True :
    you = int(input("chose rock(1) , paper(2) , scissor(3) or type(o) to stop :"))
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
    
    if 0 == you:
         wanna_play = False
         print(game_stats())
         with open("rps_win_score","w") as w:
              w.write(str(wins))
         with open("rps_loss_score","w") as l:
              l.write(str(loss))
              
         print("bye bye have a great day !!")
    
