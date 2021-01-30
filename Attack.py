import random


chars = "ABCDEFGHIJKLNOPQRSTUVWXYZabcdefghijklnopqrstuvwxyz0123456789"
chars_list = list(chars)

password = input("Enter Pass ")

guespassword = ""

while(guespassword != password):
    guespassword = random.choices(chars_list, k=len(password))

    print("<=============" + str(guespassword) + "===============>")

    if(guespassword == list(password)):
        print("Password is " + "".join(guespassword))
        break
