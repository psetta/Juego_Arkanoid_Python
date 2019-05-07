import pygame

class Status:
	#self, int, int, int => None
	def __init__(self,rect):
		#medidas del rectangulo del status
		self.rect = rect
		#medidas de los letreros 
		self.rect_label = [x/3 for x in rect]
		self.font_size = int(min(self.rect_label[0]*0.24,
								 self.rect_label[1]*1.5))
		#margen de los letreros
		self.margin_label = [self.rect[0]/8,
							 self.rect[1]/6]
		#estadisticas
		self.vidas = 5
		self.score = 0
		self.high_score = 50000
		#estado del juego
		self.game_over = 0
		self.win = 0
		self.jugando = 1
		self.pygame_bucle = 1
		#pygame surfaces
		self.score_img = self.crear_score_img()
		self.hight_score_title_img = self.crear_high_score_title_img()
		self.hight_score_img = self.crear_high_score_img()
		self.vidas_img = self.crear_vidas_img()
		
	#self => None
	def dibujar_vidas(self,ventana):
		ventana.pygame.blit(self.vidas_img, (
				ventana.espacio[0]+self.margin_label[0],
				ventana.espacio[1]+self.margin_label[1]))
				
	#self => None
	def dibujar_score(self,ventana):
		ventana.pygame.blit(self.score_img, (
				ventana.espacio[0]+self.margin_label[0],
				ventana.espacio[1]+self.margin_label[1]+self.rect_label[1]))
				
	#self => None
	def dibujar_high_score_title(self,ventana):
		ventana.pygame.blit(self.hight_score_title_img, (
				(ventana.espacio[0]+(self.rect[0]-
						(self.margin_label[0]+self.rect_label[0]))),
				ventana.espacio[1]+self.margin_label[1]))
	
	#self => None			
	def dibujar_high_score(self,ventana):
		ventana.pygame.blit(self.hight_score_img, (
				(ventana.espacio[0]+(self.rect[0]-
						(self.margin_label[0]+self.rect_label[0]))),
				ventana.espacio[1]+self.margin_label[1]+self.rect_label[1]))
				
	#self => None	
	def dibujar(self,ventana):
		self.dibujar_vidas(ventana)
		self.dibujar_score(ventana)
		self.dibujar_high_score_title(ventana)
		self.dibujar_high_score(ventana)
		
	#self => pygame.Surface
	def crear_score_img(self):
		color = [200,200,200]
		font = pygame.font.SysFont("System", self.font_size)
		text_surface = font.render(str(self.score),1,color)
		return self.crear_label_texto(text_surface)
					
	#self => pygame.Surface	 
	def crear_high_score_title_img(self):
		color = [200,30,30]
		font = pygame.font.SysFont("System", self.font_size)
		text_surface = font.render("HIGH SCORE",1,color)
		return self.crear_label_texto(text_surface)
		
	#self => pygame.Surface
	def crear_high_score_img(self):
		color = [200,200,200]
		font = pygame.font.SysFont("System", self.font_size)
		text_surface = font.render(str(self.high_score),1,color)
		return self.crear_label_texto(text_surface)
		
	#self => pygame.Surface
	def crear_vidas_img(self):
		color = [200,30,30]
		font = pygame.font.SysFont("System", self.font_size)
		text_surface = font.render(str(self.vidas)+"UP",1,color)
		return self.crear_label_texto(text_surface)
		
	#self, pygame.Surface => pygame.Surface
	def crear_label_texto(self,text_surface):
		label_surface = pygame.Surface(self.rect_label)
		label_surface.blit(text_surface,[
						self.rect_label[0]/2-text_surface.get_width()/2,
						self.rect_label[1]/2-text_surface.get_height()/2])
		return label_surface
