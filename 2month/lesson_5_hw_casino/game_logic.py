import random
from decouple import config

def read_initial_capital():
    return int(config('MY_MONEY'))

def place_bet(capital):
    while True:
        try:
            bet = int(input(f"Place your bet (Current capital: ${capital}): "))
            if bet <= capital:
                return bet
            else:
                print("Insufficient funds. Try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def play_game():
    capital = read_initial_capital()
    slots = list(range(1, 11))

    while True:
        bet = place_bet(capital)
        selected_slot = int(input("Select a slot (1-10): "))
        if selected_slot not in slots:
            print("Invalid slot number. Please choose again.")
            continue

        winning_slot = random.choice(slots)
        print(f"Winning slot: {winning_slot}")

        if selected_slot == winning_slot:
            print("Congratulations! You win!")
            capital += bet * 2
        else:
            print("Sorry, you lose.")
            capital -= bet

        print(f"Current capital: ${capital}")

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            break

    print("Game over.")
    if capital > read_initial_capital():
        print("Congratulations! You're a winner!")
    else:
        print("Better luck next time!")

if __name__ == "__main__":
    play_game()
