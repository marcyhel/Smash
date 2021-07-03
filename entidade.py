import pygame as pg
import pygame
class Entidade:
	def __init__(self,logic,x,y,altColi,largColi,alt,larg):
		self.posi=[x,y]
		self.logic=logic
		self.altColi=altColi
		self.largColi=largColi
		self.alt=alt
		self.larg=larg
		self.coli=pygame.Rect(self.posi[0],self.posi[1],self.largColi,self.altColi)
		self.rectSprite=pygame.Rect(self.posi[0],self.posi[1],self.larg,self.alt)
		self.rectSpriteReflexo=pygame.Rect(self.posi[0],self.posi[1],self.larg,self.alt/1.5)
		self.dir=0 
		self.controle=""
		self.showRect=False
	def palette_swap(self,surf, old_c, new_c):
		img_copy = pygame.Surface(surf.get_size())
		img_copy.fill(new_c)
		surf.set_colorkey(old_c)
		img_copy.blit(surf, (0, 0))
		return img_copy
	def changColor(self,image, color):
		colouredImage = pygame.Surface(image.get_size())
		colouredImage.fill(color)
		
		finalImage = image.copy()
		finalImage.blit(colouredImage, (0, 0), special_flags = pygame.BLEND_MULT)
		return finalImage
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
	def renderiza(self,spriteList,cont,screen,rect,condicao=[[0,0],[0,0]]):
		try:

			aux2=spriteList[cont]
			
			if(self.dir==0 ):
				screen.blit(aux2, (rect.left+condicao[0][0],rect.top+condicao[0][1]))
			if(self.dir==1):
				aux=pygame.transform.flip(aux2, True, False)
				screen.blit(aux, (rect.left+condicao[0][0],rect.top+condicao[0][1]))
			
		except:
			
			self.contSprite=0
			cont=0
			
			if(self.dir==0):
				screen.blit(aux2, (rect.left+condicao[0][0],rect.top+condicao[0][1]))
			if(self.dir==1):
				aux=pygame.transform.flip(aux2, True, False)
				screen.blit(aux, (rect.left+condicao[0][0],rect.top+condicao[0][1]))
		if(self.showRect):
			pygame.draw.rect(screen,(150,50,50), self.coli)
	def move(self):

		if(self.left):
			self.posi[0]-=self.velocidade
			self.dir=0
		if(self.rigth):
			self.posi[0]+=self.velocidade
			self.dir=1
		
		
		self.coli=pygame.Rect(self.posi[0],self.posi[1],self.largColi,self.altColi)
		for i in self.logic.play:
			if(i!=self):
				
				
				if(self.left):
					if(self.coli.colliderect(i.coli)):
						self.posi[0]+=self.velocidade
						
						self.coli=pygame.Rect(self.posi[0],self.posi[1],self.largColi,self.altColi)
				if(self.rigth):
					
					if(self.coli.colliderect(i.coli)):
						self.posi[0]-=self.velocidade
						
						self.coli=pygame.Rect(self.posi[0],self.posi[1],self.largColi,self.altColi)


		if(self.top):
			self.posi[1]-=self.velocidade
		if(self.bottom):
			self.posi[1]+=self.velocidade
				
		
		self.coli=pygame.Rect(self.posi[0],self.posi[1],self.largColi,self.altColi)
		for i in self.logic.play:
			if(i!=self):
				
				if(self.top):
					if(self.coli.colliderect(i.coli)):
						self.posi[1]+=self.velocidade
					
						self.coli=pygame.Rect(self.posi[0],self.posi[1],self.largColi,self.altColi)
					
					
				if(self.bottom):
					
					#self.bottom=False
					if(self.coli.colliderect(i.coli)):
						self.posi[1]-=self.velocidade
						
						self.coli=pygame.Rect(self.posi[0],self.posi[1],self.largColi,self.altColi)

		self.coli=pygame.Rect(self.posi[0],self.posi[1],self.largColi,self.altColi)
		
