
num = int(input("star size :"))

for i in range(num):
    print("x"*(i+1), end="" )
    print(" " * 2 *(num-i-1), end="" )
    print("x" * (2*i+1))

for i in range(num):
    print(" " * (num-i-1), end="" )
    print("x" * (2*i+1), end="" )
    print(" " * (num-i-1))