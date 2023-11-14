print('HI')
name = input('Your name pls           :')
birth_date = input('your birth date (mm/yyyy) :')
year = int(birth_date[3:])
month = int(birth_date[0:2])
print('You are ' + str(2022 - year) + ' years and ' + str(12 - month) + ' months old !')

if year > 18:
    print('which means you can access this website')
    print('Redirecting...')
else:
    print("Sorry , you can not access this website for now "
          "visit when you are eligible")
    print("Redirecting....")

print('Have a nice day !!')
