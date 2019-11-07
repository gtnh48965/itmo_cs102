import curses
import time

from life import GameOfLife
from ui import UI


class Console(UI):

    def __init__(self, life: GameOfLife) -> None:
        super().__init__(life)

    def draw_borders(self, screen) -> None:
        """ Отобразить рамку. """
        screen.border(0)

    def draw_grid(self, screen) -> None:
        """ Отобразить состояние клеток. """
        for row_ind, row in enumerate(self.life.curr_generation):
            for col_ind, cell in enumerate(row):
                if cell != 0:
                    try:
                        screen.addstr(row_ind + 1, col_ind + 1, '*')
                    except Exception as e:
                        print(row_ind, col_ind)

    def run(self) -> None:
        screen = curses.initscr()
        curses.curs_set(0)

        running = True
        while running:
            screen.clear()
            self.draw_borders(screen)
            self.draw_grid(screen)
            self.life.step()
            if self.life.is_max_generations_exceed:
                running = False
            screen.refresh()
            time.sleep(1 / 60)

        screen.getch()
        curses.endwin()


if __name__ == '__main__':
    game = GameOfLife((21, 80), max_generations=100)
    console = Console(game)
    console.run()
