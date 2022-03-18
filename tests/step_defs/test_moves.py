import pytest
from pytest_bdd import given, parsers, scenarios, then, when
from quantik.core import Grid, Piece
from quantik.exceptions import CannotMoveException

scenarios("../features/moves.feature")


@given(
    parsers.re(r"the following board with players de4c16 and ffffff"),
    target_fixture="grid",
)
def prepare_board_for_area():
    grid = Grid()
    grid.move_to(position="2,3", piece=Piece(type="Cube", color="#de4c16"))
    return grid


@when(parsers.re(r"player ffffff moves Cube to row 1, column 3"))
def move(grid):
    pass


@then(parsers.re(r"player ffffff sees Cannot move Cube ffffff there!"))
def cannot_move_to_area(grid):
    with pytest.raises(CannotMoveException):
        grid.move_to(position="1,3", piece=Piece(type="Cube", color="#ffffff"))
