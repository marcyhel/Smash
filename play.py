import pygame
import random
import pygame as pg
class Player:
	def __init__(self,x,y,controle=""):
		self.posi=[x,y]
		self.altColi=30
		self.largColi=50
		self.alt=150
		self.larg=120
		self.coli=pygame.Rect(self.posi[0],self.posi[1],self.largColi,self.altColi)

		self.rectSprite=pygame.Rect(self.posi[0],self.posi[1],self.larg,self.alt)


		self.contSpriteIdle=7
		self.imageIdle = self.carregarSpriteSheet('images/gothicvania patreon collection/Ghost-Files/PNG/ghost-idle.png',self.contSpriteIdle,64,80)


		self.dir=0
		self.idSprite=0
		self.contSprite=random.randint(0,5)
		self.contfp=0
		self.controle=controle
		self.velocidade=2.5
		self.left=False
		self.rigth=False
		self.bottom=False
		self.top=False
	def move(self):
		if(self.left):
			self.posi[0]-=self.velocidade
		if(self.rigth):
			self.posi[0]+=self.velocidade
		if(self.top):
			self.posi[1]-=self.velocidade
		if(self.bottom):
			self.posi[1]+=self.velocidade
		

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
	def update(self):
		self.move()
		self.coli=pygame.Rect(self.posi[0],self.posi[1],self.largColi,self.altColi)

		self.rectSprite=pygame.Rect(self.posi[0],self.posi[1],self.larg,self.alt)
		if(self.contfp>=7):
			self.frameRate()
			self.contfp=0
			
		self.contfp+=1
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

	
	def render(self,screen):
		pygame.draw.rect(screen,(150,50,50), self.coli)
		#pygame.draw.rect(screen,(50,50,50), self.rectSprite)
		

		
		
		red = (0, 0, 0,0)
		size = (23, 187, 100, 20)
		surface = pygame.Surface((50, 25),pygame.SRCALPHA)
		surface.set_alpha(150) 
		surface.fill((20,20,20))
		surface.set_colorkey((150,150,150))
		ellipse=pygame.draw.ellipse(surface, red, size)
		screen.blit(surface, (self.posi[0], self.posi[1]+20))
		if(self.idSprite==0):
			
			self.renderiza(self.imageIdle,self.contSprite,screen,condicao=[[-35,-90],[0,0]])

