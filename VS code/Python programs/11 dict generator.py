mydict = {
    "student":"state"
}

while True:
    name = input("student name :")
    state = input("state ")
    if mydict.get(name) == None:
        mydict[name] = state
        print("added")
    else:
        break


print(mydict.items())