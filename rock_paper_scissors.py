import random

user_wins = 0
computer_wins = 0

options = ['rock', 'paper', 'scissors']

while True:
    #Input the user's choice
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == 'q':
        break
    
    if user_input not in options:
        print('ERROR')
        continue
    
    random_number = random.randint(0,2)
    print(f"Computer picked: {options[random_number]}.")

    if user_input == "rock" and options[random_number] == "scissors":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and options[random_number] == "rock":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and options[random_number] == "paper":
        print("You won!")
        user_wins += 1
    
    elif user_input == options[random_number]:
        print("It's a tie!")
        
    else:
        print("You lost!")
        computer_wins += 1

print(f"You won {user_wins} times!")
print(f"Computer won {computer_wins} times!")


print("Goodbye")
