from interpreter import draw
from chessPictures import *
KNIGHTN=KNIGHT.copy()
invertir(KNIGHTN,"@")
x = KNIGHT+KNIGHTN
y= KNIGHTN+KNIGHT
def func(a, b,):
  return a+b
x = map(func, (x),(y))
tablero=Picture(list(x))
draw(tablero)
    