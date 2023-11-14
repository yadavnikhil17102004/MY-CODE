amount = input('Amount :')
discount_avail = True
if discount_avail:
    payment = (int(amount) - int(amount)*20//100)
else:
    payment = (int(amount) - int(amount)*10//100)

print(' YOU HAVE TO PAY ' + str(payment) + ' Rs')

print('have a nice day !!')
