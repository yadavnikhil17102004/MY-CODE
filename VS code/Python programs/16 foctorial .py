import random
while True:
    num = int(input("give a natural numer to add upto :"))
    if num == 0:
        num = random.randint(1,100)

    if num < 0:
        print("please enter a natural number")
    factorial = 1
    for i in range(1,num+1):
        factorial = factorial*i    
    print(f"fatorial if {num} is {factorial}")