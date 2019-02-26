import pygame
import pygame.gfxdraw
from pygame.locals import *
import math

_alto_ventana = 500
_ancho_ventana = 500
_marco = 5
_ancho_paleta = 50
_alto_paleta = 15
_radio_bola = 6
_ancho_bloque = 20
_alto_bloque = 10

class Punto:
	def __init__(self,x,y):
		self.x = x
		self.y = y
		
	def __add__(self,other):
		return punto(self.x+other.x,self.y+other.y)
		
	def __len__(self):
		return 2
		
	def __getitem__(self,item):
		if item == 0:
			return self.x
		elif item == 1:
			return self.y
		else:
			raise IndexError()
			
class Ventana:
	def __init__(self,ancho,alto,marco,score_alto):
		self.ancho = ancho
		self.alto = alto
		self.marco = marco
		self.score_alto = score_alto
		self.pygame = pygame.display.set_mode([ancho,alto],pygame.RESIZABLE)
		self.rect_pygame = pygame.Rect(marco,marco+score_alto,
									   ancho-(marco*2),alto-(marco+score_alto))
		self.rect_pygame_score = pygame.Rect(marco,
											 marco,
											 ancho-(marco*2),
											 score_alto-marco)
		
class Bola:
	velocidad_total = 6
	velocidad_max_x = 5
	velocidad_x = 0
	velocidad_y = -velocidad_total
	pegada = True
	def __init__(self,x,y,radio):
		self.punto = Punto(x,y)
		self.radio = radio
		self.diametro = self.radio*2
		
	def update_vel_x(self,paleta):
		choque = self.punto.x+self.radio - paleta.punto.x
		self.velocidad_x = ((((choque * 100)/ANCHO_PALETA_TOTAL) * 0.1)
							- self.velocidad_max_x)
		self.velocidad_x = max(-self.velocidad_max_x, self.velocidad_x)
		self.velocidad_x = min(self.velocidad_max_x, self.velocidad_x)
		
	def update_vel_y():
		self.velocidad_y = (self.velocidad_total * (math.sin(
			math.radians(90 - math.degrees(math.asin(self.velocidad_x/float(
			self.velocidad_total)))))))
		
class Paleta:
	def __init__(self,x,y,ancho,alto,velocidad):
		self.punto = Punto(x,y)
		self.ancho = ancho
		self.alto = alto
		self.velocidad = velocidad
		self.rect_pygame = pygame.Rect(x,y,ancho,alto)
		
class Bloque:
	def __init__(self,x,y,ancho,alto):
		self.punto = Punto(x,y)
		self.ancho = ancho
		self.alto = alto
		
class Status:
	def __init__(self):
		self.vidas = 5
		self.score = 0
		self.game_over = 0
		self.win = 0
		self.pygame_bucle = 1
	
class Game:
	def __init__(self):
		pygame.init()
		self.status = Status()
		self.ventana = Ventana(_ancho_ventana,_alto_ventana,_marco,
							   _alto_ventana/15)			   
		self.paleta = Paleta(int(self.ventana.ancho/2-_ancho_paleta/2),
							 int(self.ventana.alto-_alto_paleta*2),
							 _ancho_paleta,
							 _alto_paleta,
							 5)					
		self.bola = Bola(int(self.paleta.punto.x+self.paleta.ancho/2),
						 int(self.paleta.punto.y-_radio_bola),
						 _radio_bola)
						 
		self.font = pygame.font.SysFont("System", int(self.ventana.ancho/20))
		
	def dibujar_relleno(self):
		if self.status.game_over:
			color = [200,0,0]
		elif self.status.win:
			color = [0,200,0]
		else:
			color = [15,15,15]
		self.ventana.pygame.fill(color)
		
	def dibujar_fondo(self):
		color = [250,250,250]
		pygame.draw.rect(self.ventana.pygame,color,self.ventana.rect_pygame)
		color = [230,230,230]
		pygame.draw.rect(self.ventana.pygame,color,self.ventana.rect_pygame_score)
		
	def dibujar_paleta(self):
		color = [150,150,150]
		pygame.draw.rect(self.ventana.pygame,color,self.paleta.rect_pygame)
		
	def dibujar_bola(self):
		color = [20,150,200]
		pygame.gfxdraw.filled_circle(self.ventana.pygame,
									 self.bola.punto.x,
									 self.bola.punto.y,
									 self.bola.radio,
									 color)
		color = [20,150,200]
		pygame.gfxdraw.aacircle(self.ventana.pygame,
								self.bola.punto.x,
								self.bola.punto.y,
								self.bola.radio,
								color)
								
	def dibujar_score(self):
		color = [15,15,15]
		text_score = self.font.render(("SCORE: "+str(self.status.score)),1,color)
		self.ventana.pygame.blit(text_score,[self.ventana.marco,self.ventana.marco])
		
	def dibujar_vidas(self):
		color = [15,15,15]
		text_vidas = self.font.render(("VIDAS: "+str(self.status.vidas)),1,color)
		self.ventana.pygame.blit(text_vidas,[self.ventana.ancho-
								(self.ventana.marco+text_vidas.get_width()),
								 self.ventana.marco])
		
	def dibujar_todo(self):
		self.dibujar_relleno()
		self.dibujar_fondo()
		self.dibujar_paleta()
		self.dibujar_bola()
		self.dibujar_score()
		self.dibujar_vidas()
		
	def tecla_pulsada(self):
		return pygame.key.get_pressed()
		
	def movimiento(self):
		if self.tecla_pulsada[K_LEFT]:
			self.paleta.punto.x -= paleta.velocidad
		
	if tecla_pulsada[K_LEFT]:
		punto_paleta.x -= VELOCIDADE_PALETA
	if tecla_pulsada[K_RIGHT]:
		punto_paleta.x += VELOCIDADE_PALETA
		
	def start(self):
		while self.status.pygame_bucle:
			reloj = pygame.time.Clock()
			
			self.dibujar_todo()
			
			pygame.display.update()
			
			for evento in pygame.event.get():
				if evento.type == pygame.QUIT:
					pygame.display.quit()
					self.status.pygame_bucle = 0
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
	
	"""
	
if __name__ == "__main__":	
	game = Game()
	game.start()