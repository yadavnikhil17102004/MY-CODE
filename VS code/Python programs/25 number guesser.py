import random
import time

high = 20
low  = 1

print("Your have to guess a number !!")
range_change = input(f"Wanna change(Y/N) ? (current {low} to {high}) :")
if "y" in range_change:
    change_range = True
    while change_range == True:
        low = input("Lowest point :")
        high = input("Highest Point:")
        if int(high)>int(low):
            change_range = False
        else:
            print("Please enter valid value !!")

print(f"Range of number will be {low} to {high}")
wanna_play = True
wanna_retry =True

while wanna_play == True :
    print("Computer is thinking of a number !")
    num=random.randint(int(low),int(high))
    print("*")
    time.sleep(0.50)
    print("*")
    time.sleep(0.50)
    print("*")
    time.sleep(0.50)
    print("*")
    time.sleep(0.50)
    
    wanna_retry = True
    turns = 0
    try:
         while wanna_retry == True:
            guess = input("Guess the number ?:")
            if int(guess)<int(num):
                print("It's higher !")
                turns += 1
            elif int(guess)>int(num):
                print("It's lower !")
                turns+=1
            elif int(guess)==int(num):
                if turns == 0:
                    print(f"WOW HOW DID YOU DO THAT 0-0 YOU GOT IT RIGHT IN FIRST TRY !!")
                print(f"Great you guessed it right in {turns} chances")
                wanna_retry = False
    except ValueError as err:
            print('Oh no!, that is not a valid value. Try again...')
            print(err)
    retry = input("Do you wanna retry (Y/N)?")
    if "y" in retry:
         continue
    elif "n" in retry:
        wanna_play = False
    
