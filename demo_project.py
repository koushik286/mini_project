#loop
import random

while True:
    choice = input("Roll the dice (Yes/No): ").strip().lower()
    if choice == "y":
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print(f"({die1},{die2})")
    elif choice == "n":
        print("thanks for playing see you again")
        break
    else:
        print("invalid input")
