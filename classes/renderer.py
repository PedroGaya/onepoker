import curses
from curses import wrapper

def render(stdscr):
    stdscr.clear()
    stdscr.refresh()
    stdscr.getch()

wrapper(render)