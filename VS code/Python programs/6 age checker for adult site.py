print('HI')
name = input('Your name pls                       :')
birth_year = input('Your birth year                     :')
birth_month = input('Your birth month (in num)           :')

print('You are ' + str((2022 - int(birth_year))) + ' years and ' + str((12 - int(birth_month))) + 'months old')
print('Dear,' +
      name)
if birth_year > str(18):
    print('which means you can access this website')
    print('Redirecting...')
else:
    print("Sorry , you can not access this website for now "
          "visit when you are eligible")
    print("Redirecting....")

print('Have a nice day !!')
