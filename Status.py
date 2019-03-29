import pygame

class Status:
	def __init__(self):
		self.vidas = 5
		self.score = 0
		self.high_score = 50000
		self.game_over = 0
		self.win = 0
		self.jugando = 1
		self.pygame_bucle = 1
		
	def dibujar_score(self,ventana):
		color = [200,200,200]
		font = pygame.font.SysFont("System", int(ventana.ancho/20))
		text_score = font.render(str(self.score),1,color)
		ventana.pygame.blit(text_score,[
						int(ventana.ancho/8)+text_score.get_width(),
						ventana.marco+text_score.get_height()])
								 
	def dibujar_high_score(self,ventana):
		color = [200,30,30]
		font = pygame.font.SysFont("System", int(ventana.ancho/20))
		text_score = font.render("HIGH SCORE",1,color)
		ventana.pygame.blit(text_score,[int(ventana.ancho/2.5),ventana.marco])
		color = [200,200,200]
		text_score_n = font.render(str(self.high_score),1,color)
		ventana.pygame.blit(text_score_n,[
						int(ventana.ancho/2.5)+text_score.get_width()/4,
						ventana.marco+text_score.get_height()])
		
	def dibujar_vidas(self,ventana):
		color = [200,30,30]
		font = pygame.font.SysFont("System", int(ventana.ancho/20))
		text_vidas = font.render(str(self.vidas)+"UP",1,color)
		ventana.pygame.blit(text_vidas,[int(ventana.ancho/8),ventana.marco])
		
	def dibujar(self,ventana):
		self.dibujar_score(ventana)
		self.dibujar_high_score(ventana)
		self.dibujar_vidas(ventana)
