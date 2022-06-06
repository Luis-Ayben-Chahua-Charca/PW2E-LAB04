from interpreter import draw
from chessPictures import *
def func(a, b,c,d):
  return a+b+c+d
x = map(func, (QUEEN),(QUEEN),(QUEEN),(QUEEN))
tablero=Picture(list(x))
draw(tablero)