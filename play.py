import pygame
import random
import pygame as pg
from entidade import*
class Player(Entidade):
	def __init__(self,logic,x,y,controle=""):
		super().__init__(logic,x,y,30,40,150,120)
		self.contSpriteIdle=7
		self.imageIdle = self.carregarSpriteSheet('images/gothicvania patreon collection/Ghost-Files/PNG/ghost-idle.png',self.contSpriteIdle,64,80)
		self.imageIdleReflexo =[]

		self.imageDireBotton =pygame.image.load("images/dire0.png")
		self.imageDireBotton=pygame.transform.scale(self.imageDireBotton, (int(self.larg/2),int(self.alt/2) ))
		self.imageDireBottonRight =pygame.image.load("images/dire1.png")
		self.imageDireBottonRight=pygame.transform.scale(self.imageDireBottonRight, (int(self.larg/2),int(self.alt/2) ))
		self.imageDireRight =pygame.image.load("images/dire2.png")
		self.imageDireRight=pygame.transform.scale(self.imageDireRight, (int(self.larg/2),int(self.alt/2) ))
		for i in self.imageIdle:
			aux2=pygame.transform.flip(i, False, True)
			aux2.set_alpha(50) 
			aux2=self.changColor(aux2,(25,2,25))
			aux2=pygame.transform.scale(aux2, (self.larg,int(self.alt/self.logic.reflexoAlt) ))
			self.imageIdleReflexo.append(aux2)

		self.dir=0
		self.dire=1
		self.idSprite=0
		self.contSprite=random.randint(0,5)
		self.contfp=0
		self.controle=controle
		self.velocidade=2.5
		self.left=False
		self.rigth=False
		self.bottom=False
		self.top=False
	
	
	def update(self):


		if(self.left==True):
			self.dire=0
		if(self.rigth==True):
			self.dire=4
		if(self.bottom==True):
			self.dire=2
		if(self.top==True):
			self.dire=6

		if(self.top==True and self. left==True):
			self.dire=7
		if(self.top==True and self. rigth==True):
			self.dire=5
		if(self.bottom==True and self. left==True):
			self.dire=1
		if(self.bottom==True and self. rigth==True):
			self.dire=3


		self.move()
		self.coli=pygame.Rect(self.posi[0],self.posi[1],self.largColi,self.altColi)

		self.rectSprite=pygame.Rect(self.posi[0],self.posi[1]-20,self.larg,self.alt)
		self.rectSpriteReflexo=pygame.Rect(self.posi[0],self.posi[1]-20,self.larg,self.alt/2)
		if(self.contfp>=7):

			self.frameRate()
			self.contfp=0
			
		self.contfp+=1
	def frameRate(self):
		self.contSprite+=1
		if(self.idSprite==0):
			
			if(self.contSprite>=self.contSpriteIdle):
				self.contSprite=0
		
	def render(self,screen):
		#pygame.draw.rect(screen,(150,50,50), self.coli)
		#pygame.draw.rect(screen,(50,50,50), self.rectSprite)
		

		
		#
		#red = (0, 0, 0,0)
		#size = (23, 187, 100, 20)
		#surface = pygame.Surface((50, 25),pygame.SRCALPHA)
		#surface.set_alpha(150) 
		#surface.fill((20,20,20))
		#surface.set_colorkey((150,150,150))
		#ellipse=pygame.draw.ellipse(surface, red, size)
		#screen.blit(surface, (self.posi[0], self.posi[1]+20))
		mo=5

		if(self.dire==0):
			screen.blit(pygame.transform.flip(self.imageDireRight, True, False), (self.rectSprite.left-mo,self.rectSprite.top))
		if(self.dire==1):
			screen.blit(pygame.transform.flip(self.imageDireBottonRight, True, False), (self.rectSprite.left-mo,self.rectSprite.top))

		if(self.dire==2):
			screen.blit(self.imageDireBotton, (self.rectSprite.left-mo,self.rectSprite.top))

		if(self.dire==3):
			screen.blit(self.imageDireBottonRight, (self.rectSprite.left-mo,self.rectSprite.top))
		if(self.dire==4):
			screen.blit(self.imageDireRight, (self.rectSprite.left-mo,self.rectSprite.top))
		if(self.dire==5):
			screen.blit(pygame.transform.flip(self.imageDireBottonRight, False, True), (self.rectSprite.left-mo,self.rectSprite.top))
		if(self.dire==6):
			screen.blit(pygame.transform.flip(self.imageDireBotton, False, True), (self.rectSprite.left-mo,self.rectSprite.top))
		if(self.dire==7):
			screen.blit(pygame.transform.flip(self.imageDireBottonRight, True, True), (self.rectSprite.left-mo,self.rectSprite.top))
		if(self.idSprite==0):
			self.renderiza(self.imageIdleReflexo,self.contSprite,screen,self.rectSprite,condicao=[[-40,20],[0,0]])
			self.renderiza(self.imageIdle,self.contSprite,screen,self.rectSprite,condicao=[[-40,-90],[0,0]])

