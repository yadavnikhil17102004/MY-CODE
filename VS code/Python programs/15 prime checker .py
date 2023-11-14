import random


while True:
      num = int(input("number to check the prime or just type 0 for random number :"))
      if num == 0:
          num = random.randint(1,1000000)
      prime = True

      for i in range(2,num):
         if num % i == 0:
            prime = False
         break

      if prime == True:
         print(f"given number {num} is prime")
      elif prime == False:
          pass
         #print(f"given number {num} is not prime")