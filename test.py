import io
import unittest
from unittest.mock import patch
from TicTacToe import TicTacToe

class TestTicTacToe(unittest.TestCase):
  def setUp(self):
    self.game = TicTacToe()
    self.game.print_grid()

  @patch('sys.stdout', new_callable=io.StringIO)
  def testPrintEmptyGrid(self, mock_stdout):
    self.game.print_grid()
    self.assertEqual(mock_stdout.getvalue(), "- - -\n- - -\n- - -\n\n")

  def testGridEmpty(self):
    self.game.reset_game()
    self.assertTrue(self.game.grid_is_empty(0, 0))

  @patch('sys.stdout', new_callable=io.StringIO)
  def testInvalidPlay(self, mock_stdout):
    self.game.play(0, 0)
    self.game.play(0, 0)
    self.assertEqual(mock_stdout.getvalue(), "Jogada inválida!\n")
    
  @patch('sys.stdout', new_callable=io.StringIO)
  def testNoWinner(self, mock_stdout):
    self.game.reset_game()
    self.game.play(0, 0)
    self.game.play(0, 1)
    self.game.play(0, 2)
    self.game.play(2, 0)
    self.game.play(2, 1)
    self.game.play(2, 2)
    self.game.play(1, 0)
    self.game.play(1, 1)
    self.game.play(1, 2)
    self.assertEqual(mock_stdout.getvalue(), "O jogo empatou!\n")

  @patch('sys.stdout', new_callable=io.StringIO)
  def testWinner(self, mock_stdout):
    self.game.reset_game()
    self.game.play(0, 0)
    self.game.play(2, 0)
    self.game.play(0, 1)
    self.game.play(2, 1)
    self.game.play(0, 2)
    self.assertEqual(mock_stdout.getvalue(), "Você ganhou!\n")