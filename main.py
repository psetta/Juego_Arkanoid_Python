import pygame
import pygame.gfxdraw

from pygame.locals import *
from Ventana import *
from Status import *
from Pelota import *
from Paleta import *
from Bloque import *


_alto_ventana = 650
_ancho_ventana = 600
_marco = 10
_ancho_paleta = 60
_alto_paleta = 16
_velocidad_paleta = 5
_velocidad_pelota = 5
_radio_pelota = 6
_ancho_bloque = 20
_alto_bloque = 10
_fps = 60
	
	
class Game:
	#self => None
	def __init__(self):
		pygame.init()
		
		self.fps = _fps
		
		self.ventana = Ventana(_ancho_ventana,
							   _alto_ventana,_marco)	
										   
		self.paleta = Paleta(int(self.ventana.ancho/2-_ancho_paleta/2),
							 int(self.ventana.alto-_alto_paleta*2),
							 _ancho_paleta,
							 _alto_paleta,
							 _velocidad_paleta)			
							 		
		self.pelota = Pelota(int(self.paleta.punto.x+self.paleta.ancho/2),
							 int(self.paleta.punto.y-_radio_pelota),
							 _radio_pelota,
							 _velocidad_pelota)
							
		self.status = Status(self.ventana.ancho_juego/4,
							 self.ventana.score_alto/2.2,
							 self.ventana.marco)
		
	#self => None
	def dibujar_todo(self):
		self.ventana.dibujar_fondo_juego()
		self.ventana.dibujar_marco()
		self.paleta.dibujar(self.ventana)
		self.pelota.dibujar(self.ventana)
		self.pelota.dibujar_sombras(self.ventana)
		self.status.dibujar(self.ventana)
		
	#self => None
	def movimiento_paleta(self):
		key_pressed = pygame.key.get_pressed()
		if key_pressed[K_LEFT] or key_pressed[K_a]:
			if self.paleta.colision_izq(self.ventana):
				self.paleta.punto.x = self.ventana.marco
			else:
				self.paleta.punto.x -= self.paleta.velocidad
		if key_pressed[K_RIGHT] or key_pressed[K_d]:
			if self.paleta.colision_der(self.ventana):
				self.paleta.punto.x = (self.ventana.ancho - 
					(self.ventana.marco + self.paleta.ancho))
			else:
				self.paleta.punto.x += self.paleta.velocidad
			
	#self => None
	def eventos(self):
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				pygame.display.quit()
				self.status.pygame_bucle = 0
				exit()
			if evento.type == pygame.KEYDOWN:
				if evento.key == pygame.K_SPACE:
					if self.status.jugando:
						self.pelota.pegada = False
		
	#self => None
	def start(self):
		while self.status.pygame_bucle:
			reloj = pygame.time.Clock()
			
			#Eventos
			self.eventos()
			
			#Movimiento
			self.paleta.movimiento(self.ventana)
			self.pelota.movimiento(self.ventana,self.paleta)
			self.pelota.movimiento(self.ventana,self.paleta)
			
			#Dibujado
			self.dibujar_todo()
			pygame.display.update()
					
			#FPS
			reloj.tick(self.fps)
	
if __name__ == "__main__":	
	game = Game()
	game.start()
