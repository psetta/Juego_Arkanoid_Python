import pygame

class Ventana:
	#self, int, int, int => None
	def __init__(self,ancho,alto,relacion,marco):
		#relacion entre el ancho y la altura del juego
		self.relacion = relacion
		#medidas del juego
		self.ancho = int(self.ancho_total/relacion)
		self.alto = self.alto_total
		#espacio
		self.espacio = Punto((self.ancho_total-self.ancho)/2,
							 (self.alto_total-self.alto)/2)
		#marco del rectangulo de la fase del juego
		self.marco = marco
		#altura del rectangulo de puntuación
		self.score_alto = self.alto/10
		#medidas del rectangulo de la fase del juego
		self.ancho_juego = self.ancho-self.marco*2
		self.alto_juego = self.alto-(self.score_alto+self.marco*2)
		self.punto_i_juego = Punto(self.marco,
								   self.score_alto+self.marco*2)
		self.punto_f_juego = Punto(self.ancho-self.marco,
								   self.alto)
		#pygame display
		self.pygame = pygame.display.set_mode(
					[self.ancho_total,self.alto_total],
					pygame.RESIZABLE)
		#pygame surface
		self.fondo_img = self.crear_fondo_juego()
		self.marco_img = self.crear_marco()
		
	#self => None
	def dibujar_vidas(self,ventana):
		ventana.pygame.blit(self.vidas_img, (
				ventana.espacio[0]+ventana.marco+self.label_ancho/4,
				ventana.espacio[1]+ventana.marco))
				
	#self => None
	def dibujar_score(self,ventana):
		ventana.pygame.blit(self.score_img, (
				ventana.espacio[0]+ventana.marco+self.label_ancho/4,
				ventana.espacio[1]+ventana.marco+self.label_alto))
				
	#self => None
	def dibujar_high_score_title(self,ventana):
		ventana.pygame.blit(self.hight_score_title_img, (
				ventana.espacio[0]+ventana.marco+self.label_ancho*1.5,
				ventana.espacio[1]+ventana.marco))
	
	#self => None			
	def dibujar_high_score(self,ventana):
		ventana.pygame.blit(self.hight_score_img, (
				ventana.espacio[0]+ventana.marco+self.label_ancho*1.5,
				ventana.espacio[1]+ventana.marco+self.label_alto))
				
	#self => None	
	def dibujar(self,ventana):
		self.dibujar_vidas(ventana)
		self.dibujar_score(ventana)
		self.dibujar_high_score_title(ventana)
		self.dibujar_high_score(ventana)
		
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
