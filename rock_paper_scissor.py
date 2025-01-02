import random
item_list = ["Rock","Paper","Scissor"]
user_choice = input("Enter your move: ")
comp_choice = random.choice(item_list)
print(f"User choice = {user_choice},computer choice = {comp_choice}")

if user_choice == comp_choice:
    print("it's a tie!")
elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("paper covered rock! computer win!")
    else:
        print("Rock smashed scissor! you win!")

elif user_choice == "Paper":
    if comp_choice == "Scissor":
        print("Scissor cuts paper! computer win!")
    else:
        print("paper covered rock! you win!")
elif user_choice == "Scissor":
    if comp_choice == "Paper":
        print("Scissor cuts paper!you win!")
    else:
        print("Rock smashed scissor!computer win!")
