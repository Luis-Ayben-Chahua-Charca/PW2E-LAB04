from operator import truediv
from turtle import color
import pygame ,sys
pygame.init()
size=(600,400)
color=("blue")
screen =pygame.display.set_mode(size)
while True:
	for event in pygame.event.get():
		if event.type== pygame.QUIT:
			sys.exit()