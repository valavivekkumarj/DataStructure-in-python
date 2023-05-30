import random

ucount = 0
ccount = 0
drawcount = 0
while True:
    for i in range(1, 6):
        userin = input(
            """enter choice: 
        r  for rock
        s for sizer
        p for paper"""
        )

        if userin == "r":
            user = "rock"
        elif userin == "s":
            user = "sizer"
        elif userin == "p":
            user = "paper"

        l = ["rock", "paper", "sizer"]
        compin = random.choice(l)

        # now check for draw condition
        if user == compin:
            print("your choice: " + user + "       computer choice: " + compin)
            print("draw")
            # ucount = ucount + 1
            # ccount = ccount +1
            drawcount = drawcount + 1
        elif (
            (user == "rock" and compin == "sizer")
            or (user == "sizer" and compin == "paper")
            or (user == "paper" and compin == "rock")
        ):
            print("your choice: " + user + "       computer choice: " + compin)
            print("you win")
            ucount = ucount + 1
        else:
            print("your choice: " + user + "       computer choice: " + compin)
            print("you lose")
            ccount = ccount + 1

        if i == 5:
            print("you win  == " + str(ucount))
            print("computer win == " + str(ccount))
            print("draw ==  " + str(drawcount))
