#loop
import random

while True:
    choice = input("Roll the dice (Yes/No): ").lower()
    if choice == "y":
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print(f"({die1},{die2})")
    elif choice == "n":
        print("thanks for playing see you again")
        break
    else:
        print("invalid input")
    
    
    
    
    
#     import random

# while True:
#     choice = input("Roll the dice (Yes/No): ").strip().lower()
    
#     if choice == "yes":  # Checks if user wants to roll the dice
#         die1 = random.randint(1, 6)
#         die2 = random.randint(1, 6)
#         print(f"You rolled: ({die1}, {die2})")
    
#     elif choice == "no":  # Checks if user wants to exit
#         print("Thanks for playing! See you again.")
#         break  # Exits the loop
    
#     else:
#         print("Invalid input. Please enter 'Yes' or 'No'.")
