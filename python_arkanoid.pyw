# -*- coding: utf-8 -*-

import pygame
import pygame.gfxdraw
from pygame.locals import *
import math

ANCHO_VENTANA = 500
ALTO_VENTANA = 400

ANCHO_PALETA = ANCHO_VENTANA / 10
ALTO_PALETA = ANCHO_PALETA / 5

LADO_BOLA = ALTO_PALETA

RADIO_CIRCULO = ALTO_PALETA/2

ANCHO_PALETA_TOTAL = ANCHO_PALETA + RADIO_CIRCULO*2

MARCO = 5

ANCHO_BLOQUE = (ANCHO_VENTANA-MARCO*2) / 10
ALTO_BLOQUE = ALTO_PALETA * 1.3

VELOCIDADE_PALETA = 6

VELOCIDADE_BOLA_TOTAL = 6
VELOCIDADE_MAX_BOLA_X = 5
VELOCIDADE_BOLA_X = 0
VELOCIDADE_BOLA_Y = -VELOCIDADE_BOLA_TOTAL

#DESPOIS DE UN CHOQUE COA PALETA CALCULAR DIRECCION.

def calc_vel_bola_x():
	VEL_Y = VELOCIDADE_BOLA_Y
	choque_altura = (punto_bola.x+LADO_BOLA) - punto_paleta.x
	VEL_X = (((choque_altura * 100)/ANCHO_PALETA_TOTAL) * 0.1) - VELOCIDADE_MAX_BOLA_X
	VEL_X = max(-VELOCIDADE_MAX_BOLA_X, VEL_X)
	VEL_X = min(VELOCIDADE_MAX_BOLA_X, VEL_X)
	return VEL_X

#CALCULAR VELOCIDADE_BOLA_Y EN FUNCION DA VELOCIDADE EN X.
	
def calc_vel_bola_y():
	return VELOCIDADE_BOLA_TOTAL * (math.sin(math.radians(90 - math.degrees(math.asin(VELOCIDADE_BOLA_X/float(VELOCIDADE_BOLA_TOTAL))))))

class punto:
	def __init__(self,x,y):
		self.x = x
		self.y = y
		
punto_paleta = punto((ANCHO_VENTANA/2-ANCHO_PALETA/2),ALTO_VENTANA-ALTO_PALETA*2)

punto_bola = punto((punto_paleta.x+ANCHO_PALETA/2-LADO_BOLA/2),(punto_paleta.y-LADO_BOLA))


pygame.init()

#CREAR LISTA DE BLOQUES

lista_bloques = []

def crear_lista_bloques():
	for i in range(MARCO,ANCHO_VENTANA-MARCO,ANCHO_BLOQUE):
		lista_bloques.append(pygame.Rect(i,ALTO_VENTANA/5,ANCHO_BLOQUE,ALTO_BLOQUE))
	for i in range(MARCO,ANCHO_VENTANA-MARCO,ANCHO_BLOQUE):
		lista_bloques.append(pygame.Rect(i,ALTO_VENTANA/5+ALTO_BLOQUE,ANCHO_BLOQUE,ALTO_BLOQUE))
	for i in range(MARCO,ANCHO_VENTANA-MARCO,ANCHO_BLOQUE):
		lista_bloques.append(pygame.Rect(i,ALTO_VENTANA/5+ALTO_BLOQUE*2,ANCHO_BLOQUE,ALTO_BLOQUE))
	for i in range(MARCO,ANCHO_VENTANA-MARCO,ANCHO_BLOQUE):
		lista_bloques.append(pygame.Rect(i,ALTO_VENTANA/5+ALTO_BLOQUE*3,ANCHO_BLOQUE,ALTO_BLOQUE))
	for i in range(MARCO,ANCHO_VENTANA-MARCO,ANCHO_BLOQUE):
		lista_bloques.append(pygame.Rect(i,ALTO_VENTANA/5+ALTO_BLOQUE*4,ANCHO_BLOQUE,ALTO_BLOQUE))
	for i in range(MARCO,ANCHO_VENTANA-MARCO,ANCHO_BLOQUE):
		lista_bloques.append(pygame.Rect(i,ALTO_VENTANA/5+ALTO_BLOQUE*5,ANCHO_BLOQUE,ALTO_BLOQUE))
	for i in range(MARCO,ANCHO_VENTANA-MARCO,ANCHO_BLOQUE):
		lista_bloques.append(pygame.Rect(i,ALTO_VENTANA/5+ALTO_BLOQUE*6,ANCHO_BLOQUE,ALTO_BLOQUE))
	for i in range(MARCO,ANCHO_VENTANA-MARCO,ANCHO_BLOQUE):
		lista_bloques.append(pygame.Rect(i,ALTO_VENTANA/5+ALTO_BLOQUE*8,ANCHO_BLOQUE,ALTO_BLOQUE))

crear_lista_bloques()

ventana = pygame.display.set_mode([ANCHO_VENTANA, ALTO_VENTANA])

font = pygame.font.SysFont("System", ANCHO_VENTANA/20)

pelota_pegada = True

vidas = 5

score = 0

game_over = False
victoria = False

ON = True

#BUCLE DO XOGO

while ON:

	reloj = pygame.time.Clock()
	
	#DEBUXADO:
	
	if game_over:
		ventana.fill([200,0,0])
	elif victoria:
		ventana.fill([0,200,0])
	else:
		ventana.fill([20,20,20])
	
	rect_xogo = pygame.Rect(MARCO, MARCO, ANCHO_VENTANA-(MARCO*2), ALTO_VENTANA-MARCO)
	
	#DEBUXADO PALETA
	
	pygame.draw.rect(ventana, [250,250,250], rect_xogo)
	
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
		
	if punto_bola.x < MARCO and VELOCIDADE_BOLA_X < 0:
		VELOCIDADE_BOLA_X = -VELOCIDADE_BOLA_X
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