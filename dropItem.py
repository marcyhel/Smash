import pygame
import random
import pygame as pg
from entidade import*

class DropItem(Entidade):
	def __init__(self,logic,x,y):
		super().__init__(logic,x,y,50,50,100,100)
		self.logic=logic
		self.posi=[x,y]
		self.contSpriteIdle=25
		self.alt=100
		self.larg=100
		self.imageIdle = self.carregarSpriteSheet('images/dropitem.png',self.contSpriteIdle,32,32)
		self.rectSprite=pygame.Rect(self.posi[0],self.posi[1],self.larg,self.alt)
		self.imageIdleReflexo =[]

		for i in self.imageIdle:
			aux2=pygame.transform.flip(i, False, True)
			aux2.set_alpha(50) 
			aux2=self.changColor(aux2,(25,2,25))
			aux2=pygame.transform.scale(aux2, (self.larg,int(self.alt/self.logic.reflexoAlt) ))
			self.imageIdleReflexo.append(aux2)

		self.controle='d'
		self.dir=0
		self.idSprite=0
		self.contSprite=0
		self.contfp=0
	def carregarSpriteSheet(self,diretorio,num,x,y):
		aux=[]
		img = pygame.image.load(diretorio)
		xx=0
		yy=0
		xa=x
		for i in range(num):
		
			aux2=img.subsurface( pygame.Rect(xx,yy,x,y) )
			
			
			aux2=pygame.transform.scale(aux2, (self.larg,self.alt ))
			aux.append(aux2)
			xx+=xa
			
		return aux
	def renderiza(self,spriteList,cont,screen,condicao=[[0,0],[0,0]]):
		try:

			aux2=spriteList[cont]
			
			if(self.dir==0):
				screen.blit(aux2, (self.rectSprite.left+condicao[0][0],self.rectSprite.top+condicao[0][1]))
			if(self.dir==1):
				aux=pygame.transform.flip(aux2, True, False)
				screen.blit(aux, (self.rectSprite.left+condicao[0][0],self.rectSprite.top+condicao[0][1]))
			
		except:
			
			self.contSprite=0
			cont=0
			
			if(self.dir==0):
				screen.blit(aux2, (self.rectSprite.left+condicao[0][0],self.rectSprite.top+condicao[0][1]))
			if(self.dir==1):
				aux=pygame.transform.flip(aux2, True, False)
				screen.blit(aux, (self.rectSprite.left+condicao[0][0],self.rectSprite.top+condicao[0][1]))
	def frameRate(self):
		#if(random.random()<=0.01):
		#	self.left=True
		#if(random.random()<=0.01):
		#	self.rigth=True
		#if(random.random()<=0.01):
		#	self.bottom=True
		#if(random.random()<=0.01):
		#	self.top=True
		#if(random.random()<=0.05):
		#	self.left=False
		#	self.rigth=False
		#	self.top=False
		#	self.bottom=False

		self.contSprite+=1
		if(self.idSprite==0):
			
			if(self.contSprite>=self.contSpriteIdle):
				self.contSprite=0
	def update(self):
		if(self.contfp>=4):
			self.frameRate()
			self.contfp=0
			
		self.contfp+=1
	def render(self,screen):
		if(self.idSprite==0):
			self.renderiza(self.imageIdleReflexo,self.contSprite,screen,condicao=[[-35,5],[0,0]])
			self.renderiza(self.imageIdle,self.contSprite,screen,condicao=[[-35,-90],[0,0]])