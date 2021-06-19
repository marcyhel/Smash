import pygame
import random
import pygame as pg

import math
import json
import time
import copy 	
from play import *

play=[Player(200,200)]
for i in range(20):
	play.append(Player(random.randint(10,580),random.randint(10,580)))

def render(screen):
	for i in play:
		i.render(screen)
def update():
	
	for i in range(len(play)):
		for j in range(len(play)):
			if(play[i].posi[1]<play[j].posi[1]):
				aux=play[i]
				play[i]=play[j]
				play[j]=aux
	for i in play:
		i.update()
pygame.init()	
screen = pygame.display.set_mode((800, 600), 0, 32)
font = pg.font.Font(None, 30)
done = False
clock = pygame.time.Clock()
while not done:
		
				
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
			
			

		#pygame.draw.rect(screen,(100,150,50), pygame.Rect(dx, dy, 25, 25))
		pygame.display.flip()
		clock.tick(60)
		screen.fill((150,190,190))

		render(screen)
		update()
		fps = font.render("fps: "+str(int(clock.get_fps())), True, pg.Color('white'))
		screen.blit(fps, (50, 50))

			  
				