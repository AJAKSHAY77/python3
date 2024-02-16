# learning

password = input("enter your pass : ")
passsword_lenth = len(password)

if (passsword_lenth)<= 6:
    print("weak")


elif (passsword_lenth)>= 10:
    print("strong")