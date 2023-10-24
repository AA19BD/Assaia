from dataclasses import dataclass
from enum import Enum


class ChipColor(Enum):
    """Enumeration representing the colors of chips on the game board."""

    YELLOW = 'Y'
    RED = 'R'
    EMPTY = ' '


@dataclass
class Connect4Game:
    """Represents the Connect 4 game board and game logic."""

    NUM_COLUMNS = 7
    NUM_ROWS = 6

    def __init__(self):
        """Initialize the game board with empty cells."""

        self.grid = [[ChipColor.EMPTY for _ in range(self.NUM_ROWS)] for _ in range(self.NUM_COLUMNS)]

    def drop_chip(self, column: int, player_color: ChipColor):
        """Drop a chip into the specified column on the board."""

        if column < 0 or column >= Connect4Game.NUM_COLUMNS:
            raise ValueError("Invalid column selection")

        for row in range(Connect4Game.NUM_ROWS - 1, -1, -1):
            if self.grid[column][row] == ChipColor.EMPTY:
                self.grid[column][row] = player_color
                return

        raise ValueError("Column is full, cannot drop a chip here")

    def check_for_win(self):
        """Check for a winning combination on the game board."""

        for row in range(Connect4Game.NUM_ROWS):
            for col in range(Connect4Game.NUM_COLUMNS):
                if self.grid[col][row] != ChipColor.EMPTY:
                    if self._check_win_in_direction(row, col, 1, 0) \
                            or self._check_win_in_direction(row, col, 0, 1) \
                            or self._check_win_in_direction(row, col, 1, 1) \
                            or self._check_win_in_direction(row, col, 1, -1):
                        return True
        return False

    def _check_win_in_direction(self, row: int, col: int, delta_row: int, delta_col: int):
        """Check for a winning combination in a specified direction from a given position."""

        color_to_match = self.grid[col][row]
        for _ in range(3):
            row += delta_row
            col += delta_col
            if (
                    row < 0
                    or row >= Connect4Game.NUM_ROWS
                    or col < 0
                    or col >= Connect4Game.NUM_COLUMNS
                    or self.grid[col][row] != color_to_match
            ):
                return False
        return True

    def display(self):
        """Display the current state of the game board."""

        for row in range(Connect4Game.NUM_ROWS):
            for col in range(Connect4Game.NUM_COLUMNS):
                print(self.grid[col][row].value, end=", ")
            print()
        print("0 1 2 3 4 5 6")
