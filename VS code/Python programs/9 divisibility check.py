print("first creating a set type any number to add or type 0 to close making set")
my_set = set()

while True:
    num = int(input("Number to add :"))
    if num == 0:
        break
    my_set.add(num)

print(my_set)
div = int(input("which number to check divisbility :"))

for i in my_set:
    if i % div == 0:
        print(i)