import curses
import time
from random import randint
from random import choice
import curses_tools
import asyncio
async def blink(canvas, row, column, t,symbol='*'):
  while True:
    canvas.addstr(row, column, symbol, curses.A_DIM)
    for i in range(t):
     await asyncio.sleep(0)
    canvas.addstr(row, column, symbol)
    for i in range(t):
     await asyncio.sleep(0)
    canvas.addstr(row, column, symbol, curses.A_BOLD)
    for i in range(t):
     await asyncio.sleep(0)
    canvas.addstr(row, column, symbol)
    for i in range(t):
     await asyncio.sleep(0)
async def fire(canvas, start_row, start_column, rows_speed=-0.3, columns_speed=0):
    row, column = start_row, start_column

    canvas.addstr(round(row), round(column), '*')
    await asyncio.sleep(0)

    canvas.addstr(round(row), round(column), 'O')
    await asyncio.sleep(0)
    canvas.addstr(round(row), round(column), ' ')

    row += rows_speed
    column += columns_speed

    symbol = '-' if columns_speed else '|'

    rows, columns = canvas.getmaxyx()
    max_row, max_column = rows - 1, columns - 1

    curses.beep()

    while 0 < row < max_row and 0 < column < max_column:
        canvas.addstr(round(row), round(column), symbol)
        await asyncio.sleep(0)
        canvas.addstr(round(row), round(column), ' ')
        row += rows_speed
        column += columns_speed
def draw(canvas):
 x= []
 y =[]
 char = ['*' , '+' , '^',':']
 max_row,max_column = canvas.getmaxyx()
 x = [randint(1, max_row-1) for i in range(100)]
 y = [randint(1,max_column-1) for i in range(100)]
 t = [randint(10,50) for i in range(100)]
 a =[blink(canvas,choice(x),choice(y),choice(t),choice(char)) for i in range(100)]
 cor = fire(canvas,20,30)
 corutine = curses_tools.anim_spaceship(canvas,curses_tools.text1,curses_tools.text2)
 while True:
  for i in a:
   try:
     i.send(None)
     corutine.send(None)
     canvas.refresh()
   except:
      break
  cor.send(None)
  canvas.refresh()
  time.sleep(0.1)
  
canvas = curses.initscr()
curses.curs_set(0)
curses.noecho()
canvas.border()
curses.cbreak()
canvas.keypad(True)
canvas.nodelay(True)
draw(canvas)
curses.endwin()