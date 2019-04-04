import pygame

class Status:
	#self, int, int, int => None
	def __init__(self,label_ancho,label_alto,marco):
		self.label_ancho = label_ancho
		self.label_alto = label_alto
		self.font_size = int(min(label_alto*1.5,label_ancho*0.24))
		self.marco = marco
		self.vidas = 5
		self.score = 0
		self.high_score = 50000
		self.game_over = 0
		self.win = 0
		self.jugando = 1
		self.pygame_bucle = 1
		self.score_img = self.crear_score_img()
		self.hight_score_title_img = self.crear_high_score_title_img()
		self.hight_score_img = self.crear_high_score_img()
		self.vidas_img = self.crear_vidas_img()
		
	#self => pygame.Surface
	def crear_score_img(self):
		score_surface = pygame.Surface((
							self.label_ancho,
							self.label_alto))
		color = [200,200,200]
		font = pygame.font.SysFont("System", self.font_size)
		text = font.render(str(self.score),1,color)
		score_surface.blit(text,[
						self.label_ancho/2-text.get_width()/2,
						self.label_alto/2-text.get_height()/2])
		return score_surface
					
	#self => pygame.Surface	 
	def crear_high_score_title_img(self):
		hight_score_t_surface = pygame.Surface((
								self.label_ancho,
								self.label_alto))
		color = [200,30,30]
		font = pygame.font.SysFont("System", self.font_size)
		text = font.render("HIGH SCORE",1,color)
		hight_score_t_surface.blit(text,[
						self.label_ancho/2-text.get_width()/2,
						self.label_alto/2-text.get_height()/2])
		return hight_score_t_surface
		
	#self => pygame.Surface
	def crear_high_score_img(self):
		hight_score_surface = pygame.Surface((
								self.label_ancho,
								self.label_alto))
		color = [200,200,200]
		font = pygame.font.SysFont("System", self.font_size)
		text = font.render(str(self.high_score),1,color)
		hight_score_surface.blit(text,[
						self.label_ancho/2-text.get_width()/2,
						self.label_alto/2-text.get_height()/2])
		return hight_score_surface
		
	#self => pygame.Surface
	def crear_vidas_img(self):
		vidas_surface = pygame.Surface((
							self.label_ancho,
							self.label_alto))
		color = [200,30,30]
		font = pygame.font.SysFont("System", self.font_size)
		text = font.render(str(self.vidas)+"UP",1,color)
		vidas_surface.blit(text,[
						self.label_ancho/2-text.get_width()/2,
						self.label_alto/2-text.get_height()/2])
		return vidas_surface
		
	#self => None
	def dibujar_vidas(self,ventana):
		ventana.pygame.blit(self.vidas_img, (
				ventana.marco+self.label_ancho/4,
				ventana.marco))
				
	#self => None
	def dibujar_score(self,ventana):
		ventana.pygame.blit(self.score_img, (
				ventana.marco+self.label_ancho/4,
				ventana.marco+self.label_alto))
				
	#self => None
	def dibujar_high_score_title(self,ventana):
		ventana.pygame.blit(self.hight_score_title_img, (
				ventana.marco+self.label_ancho*1.5,
				ventana.marco))
	
	#self => None			
	def dibujar_high_score(self,ventana):
		ventana.pygame.blit(self.hight_score_img, (
				ventana.marco+self.label_ancho*1.5,
				ventana.marco+self.label_alto))
				
	#self => None	
	def dibujar(self,ventana):
		self.dibujar_vidas(ventana)
		self.dibujar_score(ventana)
		self.dibujar_high_score_title(ventana)
		self.dibujar_high_score(ventana)
