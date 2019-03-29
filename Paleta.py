import pygame

from Punto import *

class Paleta:
	def __init__(self,x,y,ancho,alto,velocidad):
		self.punto = Punto(x,y)
		self.ancho = ancho
		self.alto = alto
		self.alto_lateral = alto*1.1
		self.alto_lateral_2 = self.alto_lateral/2
		self.velocidad = velocidad
		self.ancho_rect_lateral = ancho/6
		self.ancho_rect_lateral_2 = self.ancho_rect_lateral/3
		self.ancho_rect_central = (self.ancho-
				(self.ancho_rect_lateral*2+self.ancho_rect_lateral_2*2))
		self.rect_cent = pygame.Rect(
				self.punto.x+self.ancho_rect_lateral+self.ancho_rect_lateral_2,
				self.punto.y,
				self.ancho_rect_central,
				self.alto)
		self.rect_izq = pygame.Rect(
				self.punto.x+self.ancho_rect_lateral_2,
				self.punto.y-(self.alto_lateral-self.alto)/2,
				self.ancho_rect_lateral,
				self.alto_lateral)
		self.rect_der = pygame.Rect(
				self.punto.x+self.ancho_rect_central+self.ancho_rect_lateral+
					self.ancho_rect_lateral_2,
				self.punto.y-(self.alto_lateral-self.alto)/2,
				self.ancho_rect_lateral,
				self.alto_lateral)
		self.rect_izq_2 = pygame.Rect(
				self.punto.x,
				self.punto.y+self.alto_lateral/4,
				self.ancho_rect_lateral_2,
				self.alto_lateral_2)
		self.rect_der_2 = pygame.Rect(
				self.punto.x+self.ancho-self.ancho_rect_lateral_2,
				self.punto.y+self.alto_lateral/4,
				self.ancho_rect_lateral_2,
				self.alto_lateral_2)
										
	def dibujar(self,ventana):
		color = [160,20,20]
		pygame.draw.rect(ventana.pygame,color,self.rect_izq)
		pygame.draw.rect(ventana.pygame,color,self.rect_der)
		color = [60,60,60]
		pygame.draw.rect(ventana.pygame,color,self.rect_izq,1)
		pygame.draw.rect(ventana.pygame,color,self.rect_der,1)
		color = [120,120,120]
		pygame.draw.rect(ventana.pygame,color,self.rect_cent)
		color = [60,60,60]
		pygame.draw.rect(ventana.pygame,color,self.rect_cent,1)
		pygame.draw.rect(ventana.pygame,color,self.rect_izq_2)
		pygame.draw.rect(ventana.pygame,color,self.rect_der_2)
						
	def update_rect(self):
		self.rect_cent = pygame.Rect(
				self.punto.x+self.ancho_rect_lateral+self.ancho_rect_lateral_2,
				self.punto.y,
				self.ancho_rect_central,
				self.alto)
		self.rect_izq = pygame.Rect(
				self.punto.x+self.ancho_rect_lateral_2,
				self.punto.y-(self.alto_lateral-self.alto)/2,
				self.ancho_rect_lateral,
				self.alto_lateral)
		self.rect_der = pygame.Rect(
				self.punto.x+self.ancho_rect_central+self.ancho_rect_lateral+
					self.ancho_rect_lateral_2,
				self.punto.y-(self.alto_lateral-self.alto)/2,
				self.ancho_rect_lateral,
				self.alto_lateral)
		self.rect_izq_2 = pygame.Rect(
				self.punto.x,
				self.punto.y+self.alto_lateral/4,
				self.ancho_rect_lateral_2,
				self.alto_lateral_2)
		self.rect_der_2 = pygame.Rect(
				self.punto.x+self.ancho-self.ancho_rect_lateral_2,
				self.punto.y+self.alto_lateral/4,
				self.ancho_rect_lateral_2,
				self.alto_lateral_2)
					
	def colision_izq(self,ventana):
		return self.punto.x <= ventana.marco
		
	def colision_der(self,ventana):
		return (self.punto.x+self.ancho >= 
				ventana.ancho-ventana.marco)
