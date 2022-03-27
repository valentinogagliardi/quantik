from unittest import TestCase

from quantik.core import Cell, Grid, Piece
from quantik.exceptions import CannotMoveException


class TestGrid(TestCase):
    def setUp(self):
        self.grid = Grid()

    def test_move_piece_no_free_position(self):
        self.grid[2][3] = Cell(Piece(type="Pyramid", color="#de4c16"))

        with self.assertRaises(CannotMoveException) as exc:
            self.grid.move_to(
                position="2,3", piece=Piece(type="Pyramid", color="#de4c16")
            )
            self.assertEqual(str(exc), "Cannot move Pyramid there!")

    def test_move_same_piece_in_area_same_player(self):
        self.grid[2][3] = Cell(Piece(type="Cube", color="#de4c16"))

        self.assertEqual(
            self.grid.move_to(
                position="3,2", piece=Piece(type="Cube", color="#de4c16")
            ),
            "Piece moved!",
        )

    def test_move_same_piece_in_row_same_player(self):
        self.grid[2][3] = Cell(Piece(type="Cube", color="#de4c16"))

        self.assertEqual(
            self.grid.move_to(
                position="2,2", piece=Piece(type="Cube", color="#de4c16")
            ),
            "Piece moved!",
        )

    def test_move_same_piece_in_column_same_player(self):
        self.grid[2][3] = Cell(Piece(type="Cube", color="#de4c16"))

        self.assertEqual(
            self.grid.move_to(
                position="3,3", piece=Piece(type="Cube", color="#de4c16")
            ),
            "Piece moved!",
        )

    def test_move_same_piece_in_row_not_same_player(self):
        piece_player1 = Piece(type="Cube", color="#de4c16")
        piece_player2 = Piece(type="Cube", color="#ffffff")

        """Player 1 has already took position."""
        self.grid[2][3] = Cell(piece_player1)

        with self.assertRaises(CannotMoveException):
            self.grid.move_to(position="2,2", piece=piece_player2)

    def test_move_same_piece_in_column_not_same_player(self):
        piece_player1 = Piece(type="Cube", color="#de4c16")
        piece_player2 = Piece(type="Cube", color="#ffffff")

        """Player 1 has already took position."""
        self.grid[2][3] = Cell(piece_player1)

        with self.assertRaises(CannotMoveException):
            self.grid.move_to(position="1,3", piece=piece_player2)
