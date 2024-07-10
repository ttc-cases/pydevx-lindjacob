import unittest
from src.rps_game import Hand


class TestHand(unittest.TestCase):

    def setUp(self):
        self.paper = Hand('paper')
        self.scissors = Hand('scissors')
        self.rock = Hand('rock')

    def test_paper_vs_rock(self):
        outcome = self.paper.play("rock")
        self.assertEqual(outcome, "paper wins against rock!")

    def test_scissors_vs_paper(self):
        outcome = self.scissors.play("paper")
        self.assertEqual(outcome, "scissors wins against paper!")

    def test_rock_vs_scissors(self):
        outcome = self.rock.play("scissors")
        self.assertEqual(outcome, "rock wins against scissors!")

    def test_tie(self):
        outcome = self.rock.play("rock")
        self.assertEqual(outcome, "It's a tie Both rock and rock played.")


if __name__ == '__main__':
    unittest.main()
