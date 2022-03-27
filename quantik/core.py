from quantik.exceptions import CannotMoveException


class Player:
    def __init__(self, name=None, color=None):
        self.name = name
        self.color = color


class Piece:
    def __init__(self, type=None, color=None):
        self.type = type
        self.color = color


class Cell:
    def __init__(self, piece=Piece(type="", color="")):
        self.piece = piece


class Grid:
    def __init__(self):
        self.grid = self._init_grid()
        self.last_player = None

    def _init_grid(self):
        """
        Area indexes are considered with the natural access order of lists.
        """
        self.areas = [
            ["0,0", "0,1", "1,0", "1,1"],
            ["0,2", "0,3", "1,2", "1,3"],
            ["2,0", "2,1", "3,0", "3,1"],
            ["2,2", "2,3", "3,2", "3,3"],
        ]

        self.rows = [
            ["0,0", "0,1", "0,2", "0,3"],
            ["1,0", "1,1", "1,2", "1,3"],
            ["2,0", "2,1", "2,2", "2,3"],
            ["3,0", "3,1", "3,2", "3,3"],
        ]

        self.columns = [
            ["0,0", "1,0", "2,0", "3,0"],
            ["0,1", "1,1", "2,1", "3,1"],
            ["0,2", "1,2", "2,2", "3,2"],
            ["0,3", "1,3", "2,3", "3,3"],
        ]

        return [
            [Cell(), Cell(), Cell(), Cell()],
            [Cell(), Cell(), Cell(), Cell()],
            [Cell(), Cell(), Cell(), Cell()],
            [Cell(), Cell(), Cell(), Cell()],
        ]

    def _mark_position(self, area, position, piece):
        try:
            area.remove(position)
            self.last_player = piece.color
        except ValueError:
            pass

    def check_winner(self, position, piece):
        for area in self.areas:
            self._mark_position(area, position, piece)

        for row in self.rows:
            self._mark_position(row, position, piece)

        for column in self.columns:
            self._mark_position(column, position, piece)

    def get_winner(self):
        for area in self.areas:
            if not len(area):
                return f"{self.last_player} you won!"

        for row in self.rows:
            if not len(row):
                return f"{self.last_player} you won!"

        for column in self.columns:
            if not len(column):
                return f"{self.last_player} you won!"

    def move_to(self, position, piece):
        row_str, col_str = position.split(",")
        row = int(row_str)
        col = int(col_str)
        if self.is_free(piece, row, col):
            self.grid[row][col] = Cell(piece=piece)
            self.check_winner(position, piece)
            return "Piece moved!"
        raise CannotMoveException(f"Cannot move {piece.type} {piece.color} there!")

    def is_free(self, piece, row, col):
        """
        Player cannot put a piece on a spot which is already occupied,
        regardless of the player who occupied the position.
        """
        if self.grid[row][col].piece.type:
            return False

        """
        A Player is not allowed to place a shape in the same row
        in which another Player has already put a piece of the same shape.
        """
        for cell in self.grid[row]:
            if cell.piece.color != piece.color and cell.piece.type == piece.type:
                return False

        """
        A Player is not allowed to place a shape in the same column
        in which another Player has already put a piece of the same shape.
        """
        for grid_row in self.grid:
            this_piece = grid_row[col].piece
            if this_piece.color != piece.color and this_piece.type == piece.type:
                return False

        return True

    def __getitem__(self, row):
        return self.grid[row]
