from pytest_bdd import given, parsers, scenarios, then, when
from quantik.core import Grid, Piece

scenarios("../features/victory.feature")


"""
Player wins in an area
"""


@given(
    parsers.re(r"the following board with players de4c16 and ffffff"),
    target_fixture="grid",
)
def board_for_victory_in_area():
    grid = Grid()
    grid.move_to(position="0,0", piece=Piece(type="Sphere", color="#de4c16"))
    grid.move_to(position="0,1", piece=Piece(type="Pyramid", color="#ffffff"))
    grid.move_to(position="2,2", piece=Piece(type="Cube", color="#de4c16"))
    grid.move_to(position="1,0", piece=Piece(type="Cylinder", color="#ffffff"))
    grid.move_to(position="0,3", piece=Piece(type="Cylinder", color="#de4c16"))
    return grid


@when(parsers.re(r"player ffffff moves Cube to row 1, column 1"))
def move_for_victory(grid):
    grid.move_to(position="1,1", piece=Piece(type="Cube", color="#ffffff"))


@then(parsers.re(r"player ffffff sees you won!"))
def victory_in_area(grid):
    assert grid.get_winner() == "#ffffff you won!"


"""
Player wins in a row
"""


@given(
    parsers.re(r"the following board with players de4c16 and 222"),
    target_fixture="grid",
)
def board_for_victory_in_row():
    grid = Grid()
    grid.move_to(position="0,0", piece=Piece(type="Sphere", color="#de4c16"))
    grid.move_to(position="0,1", piece=Piece(type="Pyramid", color="#222"))
    grid.move_to(position="2,2", piece=Piece(type="Sphere", color="#de4c16"))
    grid.move_to(position="1,0", piece=Piece(type="Cylinder", color="#222"))
    grid.move_to(position="0,3", piece=Piece(type="Cylinder", color="#de4c16"))
    return grid


@when(parsers.re(r"player 222 moves Cube to row 0, column 2"))
def move_for_victory_in_row(grid):
    grid.move_to(position="0,2", piece=Piece(type="Cube", color="#222"))


@then(parsers.re(r"player 222 sees you won!"))
def victory_in_row(grid):
    assert grid.get_winner() == "#222 you won!"


"""
Player wins in a column
"""


@given(
    parsers.re(r"the following board with players BDF7B7 and 3943B7"),
    target_fixture="grid",
)
def board_for_victory_in_column():
    grid = Grid()
    grid.move_to(position="0,3", piece=Piece(type="Cylinder", color="#BDF7B7"))
    grid.move_to(position="1,0", piece=Piece(type="Cylinder", color="#3943B7"))
    grid.move_to(position="0,0", piece=Piece(type="Cube", color="#BDF7B7"))
    grid.move_to(position="2,1", piece=Piece(type="Sphere", color="#3943B7"))
    grid.move_to(position="2,0", piece=Piece(type="Pyramid", color="#BDF7B7"))
    return grid


@when(parsers.re(r"player 3943B7 moves Sphere to row 3, column 0"))
def move_for_victory_in_column(grid):
    grid.move_to(position="3,0", piece=Piece(type="Sphere", color="#3943B7"))


@then(parsers.re(r"player 3943B7 sees you won!"))
def victory_in_column(grid):
    assert grid.get_winner() == "#3943B7 you won!"
