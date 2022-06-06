from interpreter import draw
from chessPictures import *

def func(a, b,c,d,e,f,g,h):
  return a+b+c+d+e+f+g+h
SQUAREN=SQUARE.copy()
Picture.negative(SQUAREN)
x = map(func, (SQUARE),(SQUAREN),(SQUARE),(SQUAREN),(SQUARE),(SQUAREN),(SQUARE),(SQUAREN))
tablero=Picture(list(x))
draw(tablero)