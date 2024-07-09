import argparse
import random

class Hand:
   def __init__(self, name):
       self.name = name

   def play(self):
       # Define the winning logic
       outcomes = {
           "paper": ["rock"],
           "scissors": ["paper"],
           "rock": ["scissors"]
       }
       # Determine the opponent's hand
       opponent = random.choice(["paper", "scissors", "rock"])
       # Check if the hand wins
       if opponent in outcomes[self.name]:
           return f"{self.name} wins against {opponent}!"
       elif self.name == opponent:
           return f"It's a tie Both {self.name} and {opponent} played."
       else:
           return f"{opponent} wins against {self.name}."

if __name__ == "__main__":
   parser = argparse.ArgumentParser(description="Play a game of Rock, Paper, Scissors.")
   parser.add_argument("--hand", type=str, choices=["paper", "scissors", "rock"], help="Your hand ('paper', 'scissors', or 'rock')")

   args = parser.parse_args()

   # Choose a random hand for the script
   script_hand = Hand(random.choice(["paper", "scissors", "rock"]))

   print(f"You chose: {args.hand}")
   print(f"The script chose: {script_hand.name}")
   print(script_hand.play())