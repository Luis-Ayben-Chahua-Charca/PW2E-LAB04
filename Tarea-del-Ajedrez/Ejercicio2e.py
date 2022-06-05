from interpreter import draw
from chessPictures import *
def func(a, b,c,d,e,f,g,h):
  return a+b+c+d+e+f+g+h
SQUAREN=SQUARE.copy()
negativo(SQUAREN,"=")
x = map(func, (SQUAREN),(SQUARE),(SQUAREN),(SQUARE),(SQUAREN),(SQUARE),(SQUAREN),(SQUARE))
tablero=Picture(list(x))
draw(tablero)