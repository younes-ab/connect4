from .game import Player


class DumbIA(Player):
    def play(self, grid) -> int:
        for line in range(grid.lines):
            for column in range(grid.columns):
                if grid[line][column].value == game.Cell.EMPTY:
                    return column
        # print(str(grid))
