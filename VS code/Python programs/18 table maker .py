
num = int(input("Enter a number for making table :"))
table = []

for i in range(1,11):
    print(num,"x",i,"=",num*i)
    table.append(num*i)

print(table)
