import pygame
import math

from Punto import *

class Pelota:
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
		color = [180,180,200]
		pygame.gfxdraw.circle(ventana.pygame,
								int(self.punto.x),
								int(self.punto.y),
								self.radio,
								color)
		
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
