import pygame
import pygame.gfxdraw

from pygame.locals import *
from Punto import *
from Ventana import *
from Status import *
from Pelota import *
from Paleta import *
from Bloque import *


_alto_ventana = 600
_ancho_ventana = 600
_marco = 10
_ancho_paleta = 60
_alto_paleta = 15
_radio_bola = 6
_ancho_bloque = 20
_alto_bloque = 10
	
	
class Game:
	def __init__(self):
		pygame.init()
		self.status = Status()
		self.ventana = Ventana(_ancho_ventana,_alto_ventana,_marco,
							   _alto_ventana/11)			   
		self.paleta = Paleta(int(self.ventana.ancho/2-_ancho_paleta/2),
							 int(self.ventana.alto-_alto_paleta*2),
							 _ancho_paleta,
							 _alto_paleta,
							 5)					
		self.bola = Pelota(int(self.paleta.punto.x+self.paleta.ancho/2),
						 int(self.paleta.punto.y-_radio_bola),
						 _radio_bola)
		
	def dibujar_todo(self):
		self.ventana.dibujar_fondo()
		self.ventana.dibujar_marco()
		self.paleta.dibujar(self.ventana)
		self.bola.dibujar(self.ventana)
		self.bola.dibujar_sombras(self.ventana)
		self.status.dibujar(self.ventana)
		
	def movimiento_paleta(self):
		key_pressed = pygame.key.get_pressed()
		if key_pressed[K_LEFT] or key_pressed[K_a]:
			if self.paleta.colision_izq(self.ventana):
				self.paleta.punto.x = self.ventana.marco
				self.paleta.update_rect()
			else:
				self.paleta.punto.x -= self.paleta.velocidad
				self.paleta.update_rect()
		if key_pressed[K_RIGHT] or key_pressed[K_d]:
			if self.paleta.colision_der(self.ventana):
				self.paleta.punto.x = (self.ventana.ancho - 
					(self.ventana.marco + self.paleta.ancho))
				self.paleta.update_rect()
			else:
				self.paleta.punto.x += self.paleta.velocidad
				self.paleta.update_rect()
			
	def movimiento_bola(self):
		if self.bola.pegada:
			self.bola.punto.x = int(self.paleta.punto.x+self.paleta.ancho/2)
		else:
			if self.bola.colision_paleta(self.paleta):
				self.bola.change_vel_x(self.paleta)
				self.bola.change_vel_y()
			if self.bola.colision_izq(self.ventana):
				self.bola.velocidad.x = -self.bola.velocidad.x
			if self.bola.colision_der(self.ventana):
				self.bola.velocidad.x = -self.bola.velocidad.x
			if self.bola.colision_top(self.ventana):
				self.bola.velocidad.y = -self.bola.velocidad.y
			self.bola.punto += self.bola.velocidad
			
	def eventos(self):
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				pygame.display.quit()
				self.status.pygame_bucle = 0
			if evento.type == pygame.KEYDOWN:
				if evento.key == pygame.K_SPACE:
					if self.status.jugando:
						self.bola.pegada = False
		
	def start(self):
		while self.status.pygame_bucle:
			reloj = pygame.time.Clock()
			
			self.dibujar_todo()
			
			pygame.display.update()
			
			self.movimiento_paleta()
			self.bola.movimiento(self.ventana,self.paleta)
			
			self.eventos()
					
			reloj.tick(60)
		
		print("Bye!")
			
			
"""
#CREAR LISTA DE BLOQUES

#lista_bloques = []

#def crear_lista_bloques():
#	for i in range(ventana.marco,ventana.ancho-ventana.marco,_ancho_bloque):
#		lista_bloques.append(pygame.Rect(i,ALTO_VENTANA/5,ANCHO_BLOQUE,ALTO_BLOQUE))

#crear_lista_bloques()

#BUCLE
while 0:

	reloj = pygame.time.Clock()
	
	#DEBUXADO PALETA
	
	pygame.draw.rect(ventana, [250,250,250], ventana.rect_pygame)
	
	pygame.gfxdraw.aacircle(ventana, punto_paleta.x, punto_paleta.y+ALTO_PALETA/2, RADIO_CIRCULO, [0,0,0])
	pygame.gfxdraw.filled_circle(ventana, punto_paleta.x, punto_paleta.y+RADIO_CIRCULO, ALTO_PALETA/2, [200,0,0])
	
	pygame.gfxdraw.aacircle(ventana, punto_paleta.x+ANCHO_PALETA, punto_paleta.y+ALTO_PALETA/2, ALTO_PALETA/2, [0,0,0])
	pygame.gfxdraw.filled_circle(ventana, punto_paleta.x+ANCHO_PALETA, punto_paleta.y+ALTO_PALETA/2, ALTO_PALETA/2, [200,0,0])
	
	rect_paleta = pygame.Rect(punto_paleta.x,punto_paleta.y,ANCHO_PALETA,ALTO_PALETA)
	
	pygame.draw.rect(ventana, [150,150,150], rect_paleta)
	pygame.draw.aaline(ventana, [40,40,40], [punto_paleta.x, punto_paleta.y], [punto_paleta.x+ANCHO_PALETA,punto_paleta.y])
	pygame.draw.aaline(ventana, [40,40,40], [punto_paleta.x, punto_paleta.y+ALTO_PALETA], [punto_paleta.x+ANCHO_PALETA,punto_paleta.y+ALTO_PALETA])
	
	#DEBUXADO BOLA
	
	rect_bola = pygame.Rect(punto_bola.x,punto_bola.y,LADO_BOLA,LADO_BOLA)
	
	pygame.gfxdraw.aacircle(ventana, int(punto_bola.x+LADO_BOLA/2), int(punto_bola.y+LADO_BOLA/2), LADO_BOLA/2, [0,0,0])
	pygame.gfxdraw.filled_circle(ventana, int(punto_bola.x+LADO_BOLA/2), int(punto_bola.y+LADO_BOLA/2), LADO_BOLA/2, [0,0,0])
	
	#DEBUXADO DOS BLOQUES:
	
	for i in lista_bloques:
		if i.y == ALTO_VENTANA/5 or i.y == ALTO_VENTANA/5+ALTO_BLOQUE*6:
			color = [160,160,160]
		elif i.y == ALTO_VENTANA/5+ALTO_BLOQUE:
			color = [220,0,0]
		elif i.y == ALTO_VENTANA/5+ALTO_BLOQUE*2:
			color = [220,220,0]
		elif i.y == ALTO_VENTANA/5+ALTO_BLOQUE*3:
			color = [0,0,220]
		elif i.y == ALTO_VENTANA/5+ALTO_BLOQUE*4:
			color = [0,220,0]
		elif i.y == ALTO_VENTANA/5+ALTO_BLOQUE*5:
			color = [220,0,220]
		elif i.y == ALTO_VENTANA/5+ALTO_BLOQUE*8:
			color = [0,200,200]
		pygame.draw.rect(ventana,color,i)
		pygame.draw.rect(ventana,[0,0,0],i,1)
		
	#DEBUXADO DA PUNTUACION E DAS VIDAS:
	
	text_score = font.render(("SCORE: "+str(score)),True,[0,0,0])
	ventana.blit(text_score,[MARCO,MARCO])
	text_vidas = font.render(("VIDAS: "+str(vidas)),True,[0,0,0])
	ventana.blit(text_vidas,[ANCHO_VENTANA-(MARCO+text_vidas.get_width()),MARCO])
	
	#TECLAS:
	
	tecla_pulsada = pygame.key.get_pressed()
	
	#MOVEMENTO:
	
	#MOV. PALETA
	
	if tecla_pulsada[K_LEFT]:
		punto_paleta.x -= VELOCIDADE_PALETA
	if tecla_pulsada[K_RIGHT]:
		punto_paleta.x += VELOCIDADE_PALETA
		
	punto_paleta.x = max(MARCO+RADIO_CIRCULO-1,punto_paleta.x)
	punto_paleta.x = min(ANCHO_VENTANA-(ANCHO_PALETA_TOTAL),punto_paleta.x)
	
	#MOV. PELOTA
	
	if pelota_pegada:
		punto_bola = punto((punto_paleta.x+ANCHO_PALETA/2-LADO_BOLA/2),(punto_paleta.y-LADO_BOLA))
	else:
		punto_bola.x += VELOCIDADE_BOLA_X
		punto_bola.y += VELOCIDADE_BOLA_Y
		
	#COLISIONS BOLA:
	
	#COL. MARCO
	
	if punto_bola.y < MARCO:
		VELOCIDADE_BOLA_Y = -VELOCIDADE_BOLA_Y
	elif punto_bola.x > ANCHO_VENTANA-(MARCO+LADO_BOLA) and VELOCIDADE_BOLA_X > 0:
		VELOCIDADE_BOLA_X = -VELOCIDADE_BOLA_X
	
	#COL. PALETA:
	
	if punto_bola.x > (rect_paleta.x-RADIO_CIRCULO)-LADO_BOLA and punto_bola.x < punto_paleta.x+ANCHO_PALETA+RADIO_CIRCULO and punto_bola.y >= punto_paleta.y-LADO_BOLA and punto_bola.y < punto_paleta.y and VELOCIDADE_BOLA_Y > 0:
		VELOCIDADE_BOLA_X = calc_vel_bola_x()
		VELOCIDADE_BOLA_Y = calc_vel_bola_y()
		VELOCIDADE_BOLA_Y = -VELOCIDADE_BOLA_Y
		
	#COL. BLOQUES:
	
	rect_bola_prox_mov = pygame.Rect(rect_bola.x+VELOCIDADE_BOLA_X,rect_bola.y+VELOCIDADE_BOLA_Y,LADO_BOLA,LADO_BOLA)
	
	if rect_bola_prox_mov.collidelistall(lista_bloques) and not pelota_pegada:
		lista_colisions = rect_bola_prox_mov.collidelistall(lista_bloques)
		ubicacion_rest = 0
		score = score + (len(lista_colisions) * 10)
		if score >= 800:
			victoria = True
			pelota_pegada = True
		for i in lista_colisions:
			del lista_bloques[i-ubicacion_rest]
			ubicacion_rest += 1
		VELOCIDADE_BOLA_Y = -VELOCIDADE_BOLA_Y
	
	#BOLA FORA:
	
	if punto_bola.y > ALTO_VENTANA*1.2:
		if not game_over:
			vidas -= 1
		if vidas <= 0:
			game_over = True
		if game_over or victoria:
			pelota_pegada = False
		else:
			pelota_pegada = True
		if game_over or victoria:
			punto_bola = punto(ANCHO_VENTANA,ALTO_VENTANA)
		else:
			punto_bola = punto((punto_paleta.x+ANCHO_PALETA/2-LADO_BOLA/2),(punto_paleta.y-LADO_BOLA))
	
	#UPDATE DA PANTALLA
	
	pygame.display.update()
	
	#EVENTOS
	
	for evento in pygame.event.get():
		if evento.type == pygame.KEYDOWN:
			if evento.key == pygame.K_SPACE and not game_over:
				if not victoria:
					pelota_pegada = False
			if evento.key == pygame.K_RETURN:
				if game_over:
					game_over = False
				if victoria:
					victoria = False
				lista_bloques = []
				crear_lista_bloques()
				score = 0
				vidas = 5
				pelota_pegada = True
		if evento.type == pygame.QUIT:
			pygame.display.quit()
			ON = False
			
	reloj.tick(60)
	
	"""
	
if __name__ == "__main__":	
	game = Game()
	game.start()
