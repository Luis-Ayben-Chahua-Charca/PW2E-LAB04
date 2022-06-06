from colors import *


class Picture:
  def __init__(self, img):
    self.img = img;

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  def verticalMirror(self):
    """ Devuelve el espejo vertical de la imagen """
    
    vertical = []
    for a in self.img:
        vertical.append(a[::-1])
    return vertical

  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen """
    return Picture(None)

  def negative(self):

        g=len(self)
        for a in range(g):
            i=self[a]
            l=list(i)
            for x in range(len(self[a])):
                if l[x]==".":
                    l[x]="@"
                    i="".join(l)
                if l[x]=="=":
                    l[x]="_"
                    i="".join(l)    
                if l[x]=="_":
                    l[x]="="
                    i="".join(l)     
                self[a]=i 

  def join(self, p):
    """ Devuelve una nueva figura poniendo la figura del argumento 
        al lado derecho de la figura actual """
    return Picture(None)

  def up(self, p):
    return Picture(None)

  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la
        figura actual """
    return Picture(None)
  
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    return Picture(None)

  def verticalRepeat(self, n):
    return Picture(None)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    return Picture(None)

def invertir(f,p):
        g=len(f)
        for a in range(g):
            i=f[a]
            l=list(i)
            for x in range(len(f[a])):
                if l[x]!="#"and l[x]!=" ":
                    l[x]=p
                    i="".join(l)
                f[a]=i 
