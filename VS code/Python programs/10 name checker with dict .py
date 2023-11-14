my_dict = {
     "rohan":"present",
    "soham":"present",
    "abhishek":"absent"    
}

name = input("give a name to check in dict :")

if my_dict.get(name) == None:
    print("The you are searching is not present in list !")
else:
    print( name, " is " , my_dict.get(name) )


