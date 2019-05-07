import pygame
from Punto import *

class Ventana:
	#self, int, int, float, float => None
	def __init__(self,ancho,alto,relacion_mj,relacion_fs):
		#medidas totales de la ventana
		self.rect = [ancho,alto]
		#relacion entre el ancho y la altura del juego
		self.relacion_mj = relacion_mj
		#relacion entre la altura del rectangulo de la fase y del status
		self.relacion_fs = relacion_fs
		#medidas del juego
		self.rect_juego = [int(self.rect[0]/relacion_mj),
							  self.rect[1]]
		#medidas del rectangulo del status
		self.rect_status = [self.rect_juego[0],
						    self.rect_juego[1]*relacion_fs]
		#medidas del rectangulo de la fase
		self.rect_fase = [self.rect_juego[0],
						  self.rect_juego[1]-self.rect_status[1]]
		#espacio
		self.espacio = [(self.rect[0]-self.rect_juego[0])/2,
						(self.rect[1]-self.rect_juego[1])/2]
		#pygame display
		self.pygame = pygame.display.set_mode(
					self.rect,
					pygame.RESIZABLE)
		#pygame rectangulo juego
		self.pygame_rect_juego = pygame.Rect(
				self.espacio[0],
				self.espacio[1],
				self.rect_juego[0],
				self.rect_juego[1])
		#pygame rectangulo fase
		self.pygame_rect_fase = pygame.Rect(
				self.espacio[0],
				self.espacio[1]+self.rect_status[1],
				self.rect_fase[0],
				self.rect_fase[1])
		#pygame rectangulo status
		self.pygame_rect_status = pygame.Rect(
				self.espacio[0],
				self.espacio[1],
				self.rect_status[0],
				self.rect_status[1])
				
	def dibujar_todo(self):
		self.dibujar_rect_fase()
		self.dibujar_rect_status()
		self.dibujar_rect_juego()
		
	#self => None
	def dibujar_rect_juego(self):
		color = [220,220,220]
		pygame.draw.rect(self.pygame,color,self.pygame_rect_juego,1)
		
	#self => None
	def dibujar_rect_fase(self):
		color = [180,220,180]
		pygame.draw.rect(self.pygame,color,self.pygame_rect_fase)
		
	#self => None
	def dibujar_rect_status(self):
		color = [220,180,180]
		pygame.draw.rect(self.pygame,color,self.pygame_rect_status)
		
	def resize(self):
		None
		
