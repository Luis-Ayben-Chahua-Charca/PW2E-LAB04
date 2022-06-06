from interpreter import draw
from chessPictures import *

SQUAREB=SQUARE.copy()
Picture.negative(SQUAREB)

def func2(a,b,c,d,):
  return a+b+c+d

c1 = func2 ((SQUARE) , (SQUAREB) , (SQUARE) , (SQUAREB))
c2 = func2 ((SQUAREB) , (SQUARE) , (SQUAREB) , (SQUARE))

def func3 (a,b):
    return a+b+a+b+a+b+a+b

x = map(func3, (c1),(c2))
tablero=Picture(list(x))
draw(tablero)
    