F1 = input("marks obtained by of boy number 1:")
F2 = input("marks obtained by of boy number 2:")
F3 = input("marks obtained by of boy number 3:")
F4 = input("marks obtained by of boy number 4:")
F5 = input("marks obtained by of boy number 5:")
F6 = input("marks obtained by of boy number 6:")
F7 = input("marks obtained by of boy number 7:")
F8 = input("marks obtained by of boy number 8:")
F9 = input("marks obtained by of boy number 9:")

#l1 = [F1,F2]
l1 = [F1,F2,F3,F4,F5,F6,F7,F8,F9]
l2 = l1.count("0")
l3 = 9-l2
print(type(l1))
print("Number of students with more than 0 marks =" + str(l3))

avg = int(F1+F2+F3+F4+F5+F6+F7+F8+F9)/l3

print("now ther average value with bois who got more than 0 is :", avg)