import sqlite3
import create_tables
import init_tables
import setters
import random
import getters

def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1, die2, die1 + die2

def play_point_round():
    """
    Keep rolling until:
      - roll 7      => lose
      - roll point  => win
      - otherwise keep rolling (if user agrees)
    """
    point = getters.get_point()

    while True:
        die1, die2, score = roll_dice()

        if score == 7:
            print(f"Player rolled {die1} and {die2} (7). You lose!")
            return False

        elif score == point:
            print(f"Player rolled {die1} and {die2} ({score}). You win!")
            return True

        else:
            print(f"Player rolled {die1} and {die2} ({score}). Point is still {point}.")
            ans = input("Roll again? (yes/no): ")
            if ans.lower() != "yes":
                return False


def play_come_out_round():
    # First roll (come-out roll)
    die1, die2, point = roll_dice()
    print(f"Player rolled {die1} and {die2} ({point}).")

    if point in (7, 11):
        print("You win!")
        return True

    if point in (2, 3, 12):
        print("You lose!")
        return False

    # Otherwise, establish the point
    setters.update_point(1, point)
    print(f"Your point is {point}.")

    # Keep rolling until win or loss
    while True:
        die1, die2, score = roll_dice()
        print(f"Player rolled {die1} and {die2} ({score}).")

        if score == point:
            print("You made your point! You win!")
            return True

        if score == 7:
            print("Rolled a 7. You lose!")
            return False



def play_game():
    print("Welcome to the Casino!")
    while True:
        action = input("Enter 'p' to play, 'q' to quit: ")
        if action == 'p':
            play_come_out_round()
        elif action == 'q':
            print("Goodbye!")
            break
        else:
            print("Invalid action. Please try again.")

def main():
    ans = input("Do you want to initialize the database? (yes/no): ")
    if ans.lower() == 'yes':
        create_tables.point_table()
        create_tables.data_history()
        init_tables.init_bank(1000)
        init_tables.init_point_table()
        init_tables.init_data_history()

    # Start game either way
    play_game()

if __name__ == "__main__":
    main()
