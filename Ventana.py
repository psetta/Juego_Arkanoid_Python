import pygame

class Ventana:
	def __init__(self,ancho,alto,marco):
		self.ancho = ancho
		self.alto = alto
		self.marco = marco
		self.score_alto = self.alto/10
		self.ancho_juego = self.ancho-self.marco*2
		self.alto_juego = self.alto-(self.score_alto+self.marco*2)
		self.pygame = pygame.display.set_mode([ancho,alto],pygame.RESIZABLE)
		self.rect_fondo = pygame.Rect(
								0,
								0,
								ancho-(self.marco*2),
								alto-(self.marco+self.score_alto))
		self.rect_marco_izq = pygame.Rect(
								0,
								0,
								self.marco,
								self.alto)
		self.rect_marco_der = pygame.Rect(
								self.ancho-self.marco,
								0,
								self.ancho,
								self.alto)
		self.rect_marco_top = pygame.Rect(
								0,
								0,
								self.ancho,
								self.marco)
		self.fondo_img = self.crear_fondo_juego()
		self.marco_img = self.crear_marco() 
		
	def dibujar_fondo_juego(self):
		self.pygame.blit(self.fondo_img, 
				(self.marco,self.marco*2+self.score_alto))
									
	def crear_fondo_juego(self):
		fondo = pygame.Surface((
						int(self.ancho_juego),
						int(self.alto_juego)+1))
				
		#Fondo Degradado
		num_rect = 50
		color_value_1 = 100
		color_value_2 = 140
		nivel_degradado = 1
		for y in range(0,self.alto,int(self.alto/num_rect)):
			rect = pygame.Rect(
						0,
						y,
						self.ancho_juego,
						self.alto_juego-y)
			color_value_1 = max(color_value_1 - nivel_degradado,60)
			color_value_2 = max(color_value_2 - nivel_degradado,80)
			color = [color_value_1,color_value_1,color_value_2]
			pygame.draw.rect(fondo,color,rect)
		
		#Lineas
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
				
		#Alpha
		rect_alpha = pygame.Surface(
						(self.ancho_juego,self.alto_juego),
						pygame.SRCALPHA, 32)
		rect_alpha.fill((100, 100, 140, 160))
		fondo.blit(rect_alpha, (0,0))
		
		return fondo
		
	def dibujar_marco(self):
			self.pygame.blit(self.marco_img, 
				(0,self.marco+self.score_alto))
		
	def crear_marco(self):
		marco_img = pygame.Surface(
						(self.ancho,self.alto-self.score_alto),
						pygame.SRCALPHA, 32)
		color = [120,120,120]
		pygame.draw.rect(marco_img,color,self.rect_marco_izq)
		pygame.draw.rect(marco_img,color,self.rect_marco_der)
		pygame.draw.rect(marco_img,color,self.rect_marco_top)
		color = [140,140,140]
		pygame.draw.line(marco_img,
						color,
						(self.marco,self.marco),
						(self.marco,self.alto-self.score_alto))
		pygame.draw.line(marco_img,
						color,
						(self.ancho-self.marco,self.marco),
						(self.ancho-self.marco,self.alto-self.score_alto))
		pygame.draw.line(marco_img,
						color,
						(self.marco,self.marco),
						(self.ancho-self.marco,self.marco))
		return marco_img
		
