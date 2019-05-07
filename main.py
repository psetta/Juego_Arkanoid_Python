import pygame
import pygame.gfxdraw

from pygame.locals import *
from Ventana import *
from Status import *
from Pelota import *
from Paleta import *
from Bloque import *
#from Fase import *

#CONSTANTES
	#ventana
_relacion_medidas_juego = 1.1 #altura = ancho*1.1
_ancho_ventana = 600
_min_ancho_ventana = 500
_alto_ventana = 600
_min_alto_ventana = 550
	#fase
_marco = 10
	#status
_relacion_altura_fase_score = 0.1
	#paleta
_ancho_paleta = 60
_alto_paleta = 16
_velocidad_paleta = 5
	#pelota
_velocidad_pelota = 5
_radio_pelota = 6
	#bloque
_ancho_bloque = 20
_alto_bloque = 10
	#fps
_fps = 60



	
	
class Game:
	#self => None
	def __init__(self):
		pygame.init()
		
		self.fps = _fps
		
		self.ventana = Ventana(_ancho_ventana,
							   _alto_ventana,
							   _relacion_medidas_juego,
							   _relacion_altura_fase_score)	
										   
		self.paleta = Paleta(int(self.ventana.rect[0]/2-_ancho_paleta/2),
							 int(self.ventana.rect[1]-_alto_paleta*2),
							 _ancho_paleta,
							 _alto_paleta,
							 _velocidad_paleta)			
							 		
		self.pelota = Pelota(int(self.paleta.punto.x+self.paleta.ancho/2),
							 int(self.paleta.punto.y-_radio_pelota),
							 _radio_pelota,
							 _velocidad_pelota)
							
		self.status = Status(self.ventana.rect_status)
		
	#self => None
	def dibujar_todo(self):
		#self.ventana.dibujar_fondo_juego()
		#self.ventana.dibujar_marco()
		self.ventana.dibujar_todo()
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
	def quit(self):
		pygame.display.quit()
		self.status.pygame_bucle = 0
		exit()
	
	#self => None
	def eventos(self):
		for evento in pygame.event.get():
			#EXIT
			if evento.type == pygame.QUIT:
				self.quit()
			#RESIZE
			if evento.type == pygame.VIDEORESIZE:
				None
			#TECLA ESPACIO
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
