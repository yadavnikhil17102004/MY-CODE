#Printing current and previous number sum in a range(10)

num = input("number of times to add :")
numsum = 1+ int(num)
# some goofy stuff :) enable below one and disable above one
#numsum = 99999* int(num)

previous_num = 0
for i in range(1,numsum):
    xsum = previous_num + i
    print("current num:", i ,"previous number:", previous_num,"their sum:" , xsum )
    previous_num = i
    
