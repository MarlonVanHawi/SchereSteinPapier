import random

user_wins = 0
computer_wins = 0
ties = 0
options = ["schere", "stein", "papier"]

while True:
    user_input = input("Wähle aus Schere/Stein/Papier oder Q zum beenden: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # Schere: 0, Stein: 1, Papier: 2
    computer_pick = options[random_number]
    print("Der Computer hat", computer_pick + " gewählt")

    if user_input == "rock" and computer_pick == "scissors":
        print("Du hast gewonnen!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("Du hast gewonnen!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("Du hast gewonnen!")
        user_wins += 1

    elif user_input == computer_pick:
        print("Untentschieden!")
        ties += 1

    else:
        print("Du hast verloren")
        computer_wins += 1

print("Du hast", user_wins, " mal gewonnen.")
print("Der Computer hat ", computer_wins, " gewonnen.")
print("Es gab", ties , " untentschieden")
print("Goodbye!")