import pygame
import pygame.gfxdraw
from pygame.locals import *
import math

_alto_ventana = 500
_ancho_ventana = 500
_marco = 10
_ancho_paleta = 60
_alto_paleta = 15
_radio_bola = 6
_ancho_bloque = 20
_alto_bloque = 10

class Punto:
	def __init__(self,x,y):
		self.x = x
		self.y = y
		
	def __add__(self,other):
		return Punto(self.x+other.x,self.y+other.y)
		
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
		self.rect_fondo = pygame.Rect(marco,marco+score_alto,
								ancho-(marco*2),alto-(marco+score_alto))
		self.rect_marco_izq = pygame.Rect(0,score_alto+marco,
								marco,alto)
		self.rect_marco_der = pygame.Rect(ancho-marco,score_alto+marco,
								ancho,alto)
		self.rect_marco_top = pygame.Rect(0,score_alto+marco,
								ancho,marco)
									
	def dibujar_fondo(self):
		color = [100,100,140]
		pygame.draw.rect(self.pygame,color,self.rect_fondo)
		
	def dibujar_marco(self):
		color = [160,160,160]
		pygame.draw.rect(self.pygame,color,self.rect_marco_izq)
		pygame.draw.rect(self.pygame,color,self.rect_marco_der)
		pygame.draw.rect(self.pygame,color,self.rect_marco_top)
		
class Bola:
	_velocidad_total = 6
	velocidad_max_x = _velocidad_total-1
	velocidad = Punto(0,-_velocidad_total)
	pegada = True
	
	def __init__(self,x,y,radio):
		self.punto = Punto(x,y)
		self.radio = radio
		self.diametro = self.radio*2
		self.max_sombras = 10
		self.sombras = []
		
	def movimiento(self,ventana,paleta):
		if self.pegada:
			self.punto.x = int(paleta.punto.x+paleta.ancho/2)
			if self.sombras:
				self.sombras.pop()
		else:
			if self.colision_paleta(paleta):
				self.change_vel_x(paleta)
				self.change_vel_y()
			if self.colision_izq(ventana):
				self.velocidad.x = -self.velocidad.x
			if self.colision_der(ventana):
				self.velocidad.x = -self.velocidad.x
			if self.colision_top(ventana):
				self.velocidad.y = -self.velocidad.y
				
			self.sombras.insert(0,self.punto)
			if len(self.sombras) > self.max_sombras:
				self.sombras.pop()
				
			self.punto += self.velocidad
	
	def dibujar(self,ventana):
		color = [20,150,200]
		pygame.gfxdraw.aacircle(ventana.pygame,
								int(self.punto.x),
								int(self.punto.y),
								self.radio,
								color)
		pygame.gfxdraw.filled_circle(ventana.pygame,
								int(self.punto.x),
								int(self.punto.y),
								self.radio,
								color)
		
	def dibujar_sombras(self,ventana):
		alpha = 100
		for ps in self.sombras:
			color = [20,150,200,alpha]
			alpha = int(alpha/2)
			pygame.gfxdraw.aacircle(ventana.pygame,
								int(ps.x),
								int(ps.y),
								self.radio,
								color)
			pygame.gfxdraw.filled_circle(ventana.pygame,
								int(ps.x),
								int(ps.y),
								self.radio,
								color)
				
			
	def change_vel_x(self,paleta):
		choque_x = self.punto.x - paleta.punto.x
		self.velocidad.x = (self.velocidad.x*.5+
			((((choque_x * 100)/paleta.ancho) * 0.1)- self.velocidad_max_x)*.5)
		self.velocidad.x = max(-self.velocidad_max_x, self.velocidad.x)
		self.velocidad.x = min(self.velocidad_max_x, self.velocidad.x)
		
	def change_vel_y(self):
		self.velocidad.y = -(self._velocidad_total * (math.sin(
			math.radians(90 - math.degrees(math.asin(self.velocidad.x/float(
			self._velocidad_total)))))))
			
	def colision_izq(self,ventana):
		return self.punto.x-self.radio <= ventana.marco
		
	def colision_der(self,ventana):
		return self.punto.x+self.radio >= ventana.ancho-ventana.marco
		
	def colision_top(self,ventana):
		return self.punto.y-self.radio <= ventana.marco*2+ventana.score_alto
		
	def colision_paleta(self,paleta):
		return (self.punto.x+self.radio > paleta.punto.x and 
			self.punto.x-self.radio < paleta.punto.x+paleta.ancho and 
			self.punto.y+self.radio > paleta.punto.y and 
			self.punto.y-self.radio < paleta.punto.y+(paleta.alto/2))
		
	def colision(self,ventana,paleta):
		return any(self.colision_izq(ventana),
				   self.colision_der(ventana),
				   self.colision_top(ventana),
				   self.colision_paleta(paleta))
			
		
class Paleta:
	def __init__(self,x,y,ancho,alto,velocidad):
		self.punto = Punto(x,y)
		self.ancho = ancho
		self.alto = alto
		self.velocidad = velocidad
		self.bola_radio = int(alto/2)
		self.ancho_rect = self.ancho-(self.bola_radio*2+1)
		self.rect_pygame = pygame.Rect(x+self.bola_radio,y,
										self.ancho_rect,alto)
										
	def dibujar(self,ventana):
		color = [200,20,20]
		for i in range(2):
			pygame.gfxdraw.aacircle(ventana.pygame,
					int(self.punto.x+self.ancho_rect*i+
							self.bola_radio),
					int(self.punto.y+self.alto/2),
					self.bola_radio,
					color)
			pygame.gfxdraw.filled_circle(ventana.pygame,
					int(self.punto.x+self.ancho_rect*i+
							self.bola_radio)-1*i,
					int(self.punto.y+self.alto/2),
					self.bola_radio,
					color)
			
		color = [150,150,150]
		pygame.draw.rect(ventana.pygame,color,self.rect_pygame)
		for i in range(2):
			pygame.draw.line(ventana.pygame,
					[0,0,0],
					self.punto+Punto(
						self.bola_radio+i*self.ancho_rect,
						0),
					self.punto+Punto(
						self.bola_radio+i*self.ancho_rect,
						self.alto-1))
						
	def update_rect(self):
		self.rect_pygame = pygame.Rect(self.punto.x+self.bola_radio,
					self.punto.y,self.ancho_rect,self.alto)
					
	def colision_izq(self,ventana):
		return self.punto.x <= ventana.marco
		
	def colision_der(self,ventana):
		return (self.punto.x+self.ancho >= 
				ventana.ancho-ventana.marco)
		
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
		
	def dibujar_vidas(self,ventana):
		color = [200,30,30]
		font = pygame.font.SysFont("System", int(ventana.ancho/20))
		text_vidas = font.render(str(self.vidas)+"UP",1,color)
		ventana.pygame.blit(text_vidas,[int(ventana.ancho/8),ventana.marco])
		
	def dibujar(self,ventana):
		self.dibujar_score(ventana)
		self.dibujar_high_score(ventana)
		self.dibujar_vidas(ventana)
		
	
	
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
		self.bola = Bola(int(self.paleta.punto.x+self.paleta.ancho/2),
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
