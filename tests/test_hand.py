import unittest
import sys
import os
from unittest.mock import patch

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from modules.hand import Hand


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


class TestHandMock(unittest.TestCase):

    @patch('modules.hand.Hand.play')
    def test_mock_play(self, mock_play):
        mock_play.return_value = "mocked result"

        hand = Hand('rock')
        result = hand.play('scissors')

        mock_play.assert_called_once_with('scissors')
        self.assertEqual(result, "mocked result")

if __name__ == '__main__':
    unittest.main()
