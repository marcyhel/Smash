import pygame
import random
import pygame as pg

import math
import json
import time
import copy 	
from play import *
from dropItem import *
from tile import *
from pilar import *

class Logica:
	def __init__(self):
		self.reflexoAlt=2
		self.chao=[]
		self.play=[Player(self,200,200,controle="arrow"),Player(self,250,200,controle="wasd"),DropItem(self,300,300),Pilar(self,325,297),Pilar(self,100,400)]
		for i in range(2):
			self.play.append(Player(self,random.randint(10,580),random.randint(10,580)))


		x=150
		y=250

		for i in range(2):
			#self.chao.append(Tile(self,110*(i+1),100+i))
			for j in range(4):
				if(j%2==0):
					self.chao.append(Tile(self,x+115*(i+1),y+28*(j+1)+i))
				else:
					
					self.chao.append(Tile(self,x+60+115*(i+1),y+28*(j+1)+i))

	def render(self,screen):
		for i in self.chao:
			i.render(screen)
		for i in self.play:
			i.render(screen)

	def update(self):
		for i in range(len(self.play)):
			for j in range(len(self.play)):
				if(self.play[i].rectSprite.bottom<self.play[j].rectSprite.bottom):
					aux=self.play[i]
					self.play[i]=self.play[j]
					self.play[j]=aux
		for i in range(len(self.chao)):
			for j in range(len(self.chao)):
				if(self.chao[i].rectSprite.bottom<self.chao[j].rectSprite.bottom):
					aux=self.chao[i]
					self.chao[i]=self.chao[j]
					self.chao[j]=aux
		for i in self.play:
			i.update()
		for i in self.chao:
			i.update()

logica=Logica()

def render(screen):
	
	logica.render(screen)
	
def update():
	logica.update()
	
	
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
					for i in logica.play:
						if(i.controle=="arrow"):
							i.rigth=False
							
				if event.scancode == 81:
					for i in logica.play:
						if(i.controle=="arrow"):
							i.bottom=False
						
				if event.scancode == 80:
					for i in logica.play:
						if(i.controle=="arrow"):
							i.left=False
				if event.scancode == 82:
					for i in logica.play:
						if(i.controle=="arrow"):
							i.top=False




				if event.scancode == 7:
					for i in logica.play:
						if(i.controle=="wasd"):
							i.rigth=False
						
				if event.scancode == 22:
					for i in logica.play:
						if(i.controle=="wasd"):
							i.bottom=False
						
				if event.scancode == 4:
					for i in logica.play:
						if(i.controle=="wasd"):
							i.left=False
				if event.scancode == 26:
					for i in logica.play:
						if(i.controle=="wasd"):
							i.top=False
			if event.type == pygame.KEYDOWN:
				#print(event)
				if event.scancode == 79:
					for i in logica.play:
						if(i.controle=="arrow"):
							i.rigth=True
				if event.scancode == 81:
					for i in logica.play:
						if(i.controle=="arrow"):
							i.bottom=True
						
				if event.scancode == 80:
					for i in logica.play:
						if(i.controle=="arrow"):
							i.left=True
				if event.scancode == 82:
					for i in logica.play:
						if(i.controle=="arrow"):
							i.top=True


				if event.scancode == 7:
					for i in logica.play:
						if(i.controle=="wasd"):
							i.rigth=True
							print("df")
				if event.scancode == 22:
					for i in logica.play:
						if(i.controle=="wasd"):
							i.bottom=True
						
				if event.scancode == 4:
					for i in logica.play:
						if(i.controle=="wasd"):
							i.left=True
				if event.scancode == 26:
					for i in logica.play:
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

			  
				