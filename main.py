import pygame
import random
import pygame as pg

import math
import json
import time
import copy 	
from play import *
from dropItem import *

dropItens=[]
play=[Player(200,200,controle="arrow"),Player(200,200,controle="wasd"),DropItem(300,300)]
for i in range(2):
	play.append(Player(random.randint(10,580),random.randint(10,580)))

def render(screen):
	
	for i in play:
		i.render(screen)
	for i in dropItens:
		i.render(screen)
def update():
	
	for i in range(len(play)):
		for j in range(len(play)):
			if(play[i].rectSprite.bottom<play[j].rectSprite.bottom):
				aux=play[i]
				play[i]=play[j]
				play[j]=aux
	for i in play:
		i.update()
	for i in dropItens:
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
			if event.type == pygame.KEYUP:
				if event.scancode == 79:
					for i in play:
						if(i.controle=="arrow"):
							i.rigth=False
							print("df")
				if event.scancode == 81:
					for i in play:
						if(i.controle=="arrow"):
							i.bottom=False
						
				if event.scancode == 80:
					for i in play:
						if(i.controle=="arrow"):
							i.left=False
				if event.scancode == 82:
					for i in play:
						if(i.controle=="arrow"):
							i.top=False




				if event.scancode == 7:
					for i in play:
						if(i.controle=="wasd"):
							i.rigth=False
							print("df")
				if event.scancode == 22:
					for i in play:
						if(i.controle=="wasd"):
							i.bottom=False
						
				if event.scancode == 4:
					for i in play:
						if(i.controle=="wasd"):
							i.left=False
				if event.scancode == 26:
					for i in play:
						if(i.controle=="wasd"):
							i.top=False
			if event.type == pygame.KEYDOWN:
				print(event)
				if event.scancode == 79:
					for i in play:
						if(i.controle=="arrow"):
							i.rigth=True
				if event.scancode == 81:
					for i in play:
						if(i.controle=="arrow"):
							i.bottom=True
						
				if event.scancode == 80:
					for i in play:
						if(i.controle=="arrow"):
							i.left=True
				if event.scancode == 82:
					for i in play:
						if(i.controle=="arrow"):
							i.top=True


				if event.scancode == 7:
					for i in play:
						if(i.controle=="wasd"):
							i.rigth=True
							print("df")
				if event.scancode == 22:
					for i in play:
						if(i.controle=="wasd"):
							i.bottom=True
						
				if event.scancode == 4:
					for i in play:
						if(i.controle=="wasd"):
							i.left=True
				if event.scancode == 26:
					for i in play:
						if(i.controle=="wasd"):
							i.top=True

		#pygame.draw.rect(screen,(100,150,50), pygame.Rect(dx, dy, 25, 25))
		pygame.display.flip()
		clock.tick(60)
		screen.fill((120,160,160))

		render(screen)
		update()
		fps = font.render("fps: "+str(int(clock.get_fps())), True, pg.Color('white'))
		screen.blit(fps, (50, 50))

			  
				