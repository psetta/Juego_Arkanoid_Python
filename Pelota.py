import pygame
import math

from Punto import *

class Pelota:
	#self, int, int, int
	def __init__(self,x,y,radio,vel_total):
		self.velocidad_total = vel_total
		self.velocidad_max_x = self.velocidad_total-1
		self.velocidad = Punto(0,-self.velocidad_total)
		self.pegada = True
		self.punto = Punto(x,y)
		self.radio = radio
		self.diametro = self.radio*2
		self.max_sombras = 10
		self.sombras = []
		
	#self, Ventana, Paleta => None
	def movimiento(self,ventana,paleta):
		if self.pegada:
			self.punto.x = int(paleta.punto.x+paleta.ancho/2)
			if self.sombras:
				self.sombras.pop()
		else:
			if self.colision(ventana,paleta):
				if self.colision_paleta(paleta):
					self.change_vel_x(paleta)
					self.change_vel_y()
					self.punto.x += self.velocidad.x
					self.punto.y = paleta.punto.y-self.radio
				if self.colision_izq(ventana):
					self.velocidad.x = -self.velocidad.x
					self.punto.x += ventana.punto_i_juego.x-self.radio
					self.punto.y += self.velocidad.y
				if self.colision_der(ventana):
					self.velocidad.x = -self.velocidad.x
					self.punto.x = ventana.punto_f_juego.x-self.radio
					self.punto.y += self.velocidad.y
				if self.colision_top(ventana):
					self.velocidad.y = -self.velocidad.y
					self.punto.x += self.velocidad.x
					self.punto.y = ventana.punto_i_juego.y+self.radio
			else:
				self.punto += self.velocidad
			self.add_sombra()
				
	#self => None
	def add_sombra(self):	
		self.sombras.insert(0,self.punto)
		if len(self.sombras) > self.max_sombras:
			self.sombras.pop()
	
	#self, Ventana => None
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
		color = [180,180,200]
		pygame.gfxdraw.circle(ventana.pygame,
								int(self.punto.x),
								int(self.punto.y),
								self.radio,
								color)
	
	#self => Ventana => None	
	def dibujar_sombras(self,ventana):
		alpha = 80
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
				
	#self, Paleta => None		
	def change_vel_x(self,paleta):
		choque_x = (((self.punto.x-(paleta.punto.x+paleta.ancho/2))*100)/
					(paleta.ancho/2))
		self.velocidad.x = (self.velocidad.x*.4+
			((self.velocidad_max_x*choque_x)/100)*.6)
		self.velocidad.x = max(-self.velocidad_max_x, self.velocidad.x)
		self.velocidad.x = min(self.velocidad_max_x, self.velocidad.x)
		
	#self => None
	def change_vel_y(self):
		self.velocidad.y = -(self.velocidad_total * (math.sin(
			math.radians(90 - math.degrees(
				math.asin(self.velocidad.x/float(self.velocidad_total)))
			))))
			
	#self, Ventana => Boolean
	def colision_izq(self,ventana):
		punto_fut = self.punto+self.velocidad
		return punto_fut.x-self.radio < ventana.marco
		
	#self, Ventana => Boolean
	def colision_der(self,ventana):
		punto_fut = self.punto+self.velocidad
		return punto_fut.x+self.radio > ventana.ancho-ventana.marco
		
	#self, Ventana => Boolean
	def colision_top(self,ventana):
		punto_fut = self.punto+self.velocidad
		return punto_fut.y-self.radio < ventana.punto_i_juego.y
		
	#self, Paleta => Boolean
	def colision_paleta(self,paleta):
		punto_fut = self.punto+self.velocidad
		pelota_rect_mov = [
					min(self.punto.x,punto_fut.x),
					min(self.punto.y,punto_fut.y),
					max(self.punto.x,punto_fut.x),
					max(self.punto.y,punto_fut.y)]
		paleta_rect = [paleta.punto.x,
					   paleta.punto.y,
					   paleta.punto.x+paleta.ancho,
					   paleta.punto.y+paleta.alto/2]		  
		return  not any([paleta_rect[0] > pelota_rect_mov[2],
				 paleta_rect[2] < pelota_rect_mov[0],
				 paleta_rect[1] > pelota_rect_mov[3],
				 paleta_rect[3] < pelota_rect_mov[1]])		 
		
	#self, Ventana, Paleta => Boolean
	def colision(self,ventana,paleta):
		return any([self.colision_izq(ventana),
				   self.colision_der(ventana),
				   self.colision_top(ventana),
				   self.colision_paleta(paleta)])
