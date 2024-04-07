import random

def spin_chamber():
    # Simulate spinning the chamber by randomly selecting a new chamber position
    return random.randint(0, 6)

def play_round():
    # Prompt the user to input a number between 0 and 6 representing their chosen chamber
    user_input = int(input("Enter a number between 0 and 6: "))
    
    # Simulate spinning the chamber for the bullet
    bullet_chamber = spin_chamber()
    
    # Simulate spinning the chamber for the player's choice
    player_chamber = spin_chamber()
    
    if player_chamber == bullet_chamber:
        print("You have shot yourself.")
    else:
        print("Looks like you will live to see another day.")

def main():
    # Loop to allow the player to play multiple rounds
    while True:
        play_round()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

if __name__ == "__main__":
    main()
