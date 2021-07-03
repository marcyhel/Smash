import random
from entidade import*
class Pilar(Entidade):
	def __init__(self,logic,x,y,controle=""):
		super().__init__(logic,x,y,25,45,140,70)
		self.imageIdle = self.carregarSpriteSheet('images/pilar.png',1,32,64)


		aux2=pygame.transform.flip(self.imageIdle[0], False, True)
		aux2.set_alpha(50) 
		aux2=self.changColor(aux2,(25,2,25))
		aux2=pygame.transform.scale(aux2, (self.larg,int(self.alt/self.logic.reflexoAlt) ))
		self.imageIdleReflexo=[aux2]

	def update(self):
		pass

	def render(self,screen):
		self.renderiza(self.imageIdleReflexo,0,screen,self.rectSprite,condicao=[[-13,10],[0,0]])
		self.renderiza(self.imageIdle,0,screen,self.rectSprite,condicao=[[-13,-88],[0,0]])
		
		#pygame.draw.rect(screen,(150,50,50), self.coli)