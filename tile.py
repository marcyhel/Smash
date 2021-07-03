import random
from entidade import*
class Tile(Entidade):
	def __init__(self,logic,x,y,controle=""):
		super().__init__(logic,x,y,50,50,120,120)
		self.imageIdle = self.carregarSpriteSheet('images/tile'+str(random.randint(0,2))+'.png',1,64,64)


	def update(self):
		self.coli=pygame.Rect(self.posi[0],self.posi[1],0,0)

	def render(self,screen):
		self.renderiza(self.imageIdle,0,screen,self.rectSprite,condicao=[[-35,-90],[0,0]])