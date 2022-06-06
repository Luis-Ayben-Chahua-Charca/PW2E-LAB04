from interpreter import draw
from chessPictures import *

KNIGHTB=KNIGHT.copy()
Picture.negative(KNIGHTB,)

aux= knight.verticalMirror() 
KNIGHTI = aux.copy()

KNIGHTBI = KNIGHTI.copy()
Picture.negative(KNIGHTBI)

x = KNIGHT+KNIGHTBI
y = KNIGHTB + KNIGHTI

def func(a, b,):
  return a+b
x = map(func, (x),(y))
tablero=Picture(list(x))
draw(tablero)
    