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
