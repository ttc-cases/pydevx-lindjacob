import argparse
import random


class Hand:
    def __init__(self, name):
        self.name = name

    def play(self, opponent):
        outcomes = {
            "paper": ["rock"],
            "scissors": ["paper"],
            "rock": ["scissors"]
        }
        if opponent in outcomes[self.name]:
            return f"{self.name} wins against {opponent}!"
        elif self.name == opponent:
            return f"It's a tie Both {self.name} and {opponent} played."
        else:
            return f"{opponent} wins against {self.name}."


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
