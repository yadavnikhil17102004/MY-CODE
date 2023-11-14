height = input("you hight (ex: 5.5 feet or 167 cm) :")

if "feet" in height:
    hincm = height[0:-4]
    hincm = float(hincm)
    print("Your high in cm is ", (hincm*30.48) ,"cm .") 
elif "cm" in height:
    hinfeet = height[0:-2]
    hinfeet = float(hinfeet)
    print("Your high in feet is ", (hinfeet/30.48) ,"feet .") 

