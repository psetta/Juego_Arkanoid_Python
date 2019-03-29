import pygame

class Ventana:
	def __init__(self,ancho,alto,marco,score_alto):
		self.ancho = ancho
		self.alto = alto
		self.marco = marco
		self.score_alto = score_alto
		self.pygame = pygame.display.set_mode([ancho,alto],pygame.RESIZABLE)
		self.rect_fondo = pygame.Rect(
								self.marco,
								self.marco+score_alto,
								ancho-(marco*2),
								alto-(marco+score_alto))
		self.rect_marco_izq = pygame.Rect(
								0,
								self.score_alto+self.marco,
								self.marco,
								self.alto)
		self.rect_marco_der = pygame.Rect(
								self.ancho-self.marco,
								self.score_alto+self.marco,
								self.ancho,
								self.alto)
		self.rect_marco_top = pygame.Rect(
								0,
								self.score_alto+self.marco,
								self.ancho,
								self.marco)
									
	def dibujar_fondo(self):
		color = [100,100,140]
		pygame.draw.rect(self.pygame,color,self.rect_fondo)
		
		color_value_1 = 100
		color_value_2 = 140
		
		for y in range(int(self.alto/6),self.alto,int(self.alto/40)):
			rect = pygame.Rect(
						self.marco,
						self.marco+self.score_alto+y,
						self.ancho-(self.marco*2),
						self.alto-(self.marco+self.score_alto+y))
			color_value_1 = max(color_value_1 - 1,10)
			color_value_2 = max(color_value_2 - 1,50)
			color = [color_value_1,color_value_1,color_value_2]
			pygame.draw.rect(self.pygame,color,rect)
		
		color = [60,60,80]
		for i in range(10):
			pygame.draw.line(self.pygame,
				color,
				(self.marco,(self.marco*2+self.score_alto)+i*self.alto/10),
				((self.ancho-self.marco)-i*self.ancho/9,self.alto))
		for i in range(1,10):
			pygame.draw.line(self.pygame,
				color,
				(self.marco+i*self.ancho/9,self.marco*2+self.score_alto),
				(self.ancho-self.marco,self.alto-i*self.alto/10))
		for i in range(10):
			pygame.draw.line(self.pygame,
				color,
				(self.marco+i*self.ancho/9,self.alto),
				(self.ancho-self.marco,
					self.marco*2+self.score_alto+i*self.alto/10))
		for i in range(1,10):
			pygame.draw.line(self.pygame,
				color,
				(self.marco,self.alto-i*self.alto/10),
				((self.ancho-self.marco)-i*self.ancho/9,
					self.marco*2+self.score_alto))
		rect_alpha = pygame.Surface(
						(self.ancho-self.marco*2,
							self.alto-(self.marco*2+self.score_alto)),
						pygame.SRCALPHA, 32)
		rect_alpha.fill((100, 100, 140, 160))
		self.pygame.blit(rect_alpha, 
				(self.marco,self.marco*2+self.score_alto))
		
		
	def dibujar_marco(self):
		color = [160,160,160]
		pygame.draw.rect(self.pygame,color,self.rect_marco_izq)
		pygame.draw.rect(self.pygame,color,self.rect_marco_der)
		pygame.draw.rect(self.pygame,color,self.rect_marco_top)
