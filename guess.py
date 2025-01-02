import random
top_of_range = input("enter a number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("please type again")
        quit()
else:
    print("please type again")
    quit()      

random_number = random.randint(0,top_of_range)
while True:
    user_guess = input("make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print("please type again")
        continue

    if user_guess == random_number:
        print("wow")
    else:
        print("oh no")
