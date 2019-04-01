import pygame

class Ventana:
	def __init__(self,ancho,alto,marco,score_alto):
		self.ancho = ancho
		self.alto = alto
		self.marco = marco
		self.score_alto = score_alto
		self.ancho_juego = self.ancho-self.marco*2
		self.alto_juego = self.alto-(self.score_alto+self.marco*2)
		self.pygame = pygame.display.set_mode([ancho,alto],pygame.RESIZABLE)
		self.rect_fondo = pygame.Rect(
								0,
								0,
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
		self.fondo = self.crear_fondo()
		
	def dibujar_fondo(self):
		self.pygame.blit(self.fondo, 
				(self.marco,self.marco*2+self.score_alto))
									
	def crear_fondo(self):
		fondo = pygame.Surface((
						int(self.ancho_juego),
						int(self.alto_juego)))
		color = [100,100,140]
		pygame.draw.rect(fondo,color,self.rect_fondo)
				
		color_value_1 = 100
		color_value_2 = 140
		"""
		for y in range(0,self.alto,int(self.alto/40)):
			rect = pygame.Rect(
						0,
						0,
						self.ancho-(self.marco*2),
						self.alto-(self.marco*2+self.score_alto+y))
			color_value_1 = max(color_value_1 - 1,10)
			color_value_2 = max(color_value_2 - 1,50)
			color = [color_value_1,color_value_1,color_value_2]
			pygame.draw.rect(fondo,color,rect)
		"""
		color = [60,60,80]
		nlineas = 10
		for i in range(nlineas):
			pygame.draw.line(
				fondo,
				color,
				(0,i*self.alto_juego/nlineas),
				(self.ancho_juego-i*self.ancho_juego/nlineas,self.alto_juego))
		for i in range(1,nlineas):
			pygame.draw.line(
				fondo,
				color,
				(i*self.ancho_juego/nlineas,0),
				(self.ancho_juego,self.alto_juego-i*self.alto_juego/nlineas))
		for i in range(nlineas):
			pygame.draw.line(
				fondo,
				color,
				(i*self.ancho_juego/nlineas,self.alto_juego),
				(self.ancho_juego,i*self.alto_juego/nlineas))
		for i in range(1,nlineas):
			pygame.draw.line(
				fondo,
				color,
				(0,self.alto_juego-i*self.alto_juego/nlineas),
				(self.ancho_juego-i*self.ancho_juego/nlineas,0))
		rect_alpha = pygame.Surface(
						(self.ancho_juego,self.alto_juego),
						pygame.SRCALPHA, 32)
		rect_alpha.fill((100, 100, 140, 160))
		fondo.blit(rect_alpha, (0,0))
		return fondo
		
	def dibujar_marco(self):
		color = [160,160,160]
		pygame.draw.rect(self.pygame,color,self.rect_marco_izq)
		pygame.draw.rect(self.pygame,color,self.rect_marco_der)
		pygame.draw.rect(self.pygame,color,self.rect_marco_top)
