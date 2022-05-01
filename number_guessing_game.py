import random as r

print("********************************************")
print("********************************************")
print("********************************************")
print("************** WELCOME BOSS*****************")
print("*********TO THE WORLD OF NUMBERS************")
print("********************************************")
print("********************************************")
print("********************************************")
answer=r.randint(0,24)
def easy():
    print("please enter a number below 25")
    try:
        user_guess=int(input(">"))
        if user_guess==answer:
            print("hurrey! your guess is correct")
        elif user_guess > answer:
            print("sorry boss you went higher than the actual answer")
            easy()
        elif user_guess < answer:
            print("sorry boss you went much more lower than the actual answer")
            easy()

    except ValueError:
        print("please enter a number")
        easy()


def hard():
    print("please enter a number below 25")
    try:
        user_guess=int(input(">"))
        tries=0
        while tries < 5:
            if user_guess==answer:
                print("boss you have guessed a correct answer :")
                break
            elif user_guess > answer:
                print("sorry boss you went higher than the actual answer(*_*)")
                tries +=1
                if tries==5:
                    print(f"\nyou are failed you had {tries} tries")
                else:
                    print("please guess the number: ")
            elif user_guess < answer:
                print("sorry boss you went lower than the actual answer(*_*)")
                tries +=1
                if tries == 5:
                    print(f"\nyou are failed you had {tries} tries")
                else:
                    print("please guess the number: ")

    except ValueError:
        print("!!please enter a number")


def pre_game():
    print("How would you like to play?")
    print("press 1-EASY MODE\n press 2- HARD MODE")
    operation=input(">")
    if operation =="1":
        easy()
    elif operation =="2":
        hard()

pre_game()
