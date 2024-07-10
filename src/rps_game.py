import argparse
import random
from modules.hand import Hand


def choose_random_hand():
    return Hand(random.choice(["paper", "scissors", "rock"]))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Play a game of Rock, Paper, Scissors.")
    parser.add_argument("--hand", type=str, choices=[
                        "paper", "scissors", "rock"], help="Your hand ('paper', 'scissors', or 'rock')")

    args = parser.parse_args()

    script_hand = choose_random_hand()
    print(f"You chose: {args.hand}")
    print(f"The script chose: {script_hand.name}")
    print(script_hand.play(args.hand))
