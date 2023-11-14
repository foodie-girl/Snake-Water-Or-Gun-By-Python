import random

def game(com,user):
    if com=="s" and user=="w":
        print("Computer Choose : Snake")
        print("You Choose : Water")
        print("Result : You Loss :(")
    elif com == "s" and user == "g":
        print("Computer Choose : Snake")
        print("You Choose : Gun")
        print("Result : You Win :)")
    elif com == "s" and user == "s":
        print("Computer Choose : Snake")
        print("You Choose : Snake")
        print("Result : Match Draw :|")
    elif com == "w" and user == "s":
        print("Computer Choose : Water")
        print("You Choose : Snake")
        print("Result : You Win :)")
    elif com == "w" and user == "g":
        print("Computer Choose : Water")
        print("You Choose : Gun")
        print("Result : You Loss :(")
    elif com == "w" and user == "w":
        print("Computer Choose : Water")
        print("You Choose : Water")
        print("Result : Match Draw :|")
    elif com == "g" and user == "w":
        print("Computer Choose : Gun")
        print("You Choose : Water")
        print("Result : You Win :)")
    elif com == "g" and user == "s":
        print("Computer Choose : Gun")
        print("You Choose : Snake")
        print("Result : You Loss :(")
    elif com == "g" and user == "g":
        print("Computer Choose : Gun")
        print("You Choose : Gun")
        print("Result : Match Draw :|")
    else:
        print("Error! Please Enter Valid Input")

print("Computer Turn : Snake(s) Water(w) Or Gun(g)")
com = random.randint(1,3)

if com == 1:
    com="s"
elif com==2:
    com="w"
elif com==3:
    com="g"

user = input("User Turn : Snake(s) Water(w) Or Gun(g) : ")

game(com,user)