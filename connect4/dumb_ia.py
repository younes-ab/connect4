from .game import Grid, Player


class DumbIA(Player):
    def play(self, grid: Grid) -> int:
        for line in range(grid.lines):
            for column in range(grid.columns):
                if grid[line][column].value == game.Cell.EMPTY:
                    return column
        # print(str(grid))

