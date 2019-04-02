import pygame

from Punto import *

class Paleta:
	def __init__(self,x,y,ancho,alto,velocidad):
		self.punto = Punto(x,y)
		self.ancho = ancho
		self.alto = alto
		self.velocidad = velocidad
		self.ancho_rect_lat = ancho/6
		self.ancho_rect_lat_2 = self.ancho_rect_lat/3
		self.ancho_rect_central = (self.ancho-
				(self.ancho_rect_lat*2+self.ancho_rect_lat_2*2))
		self.rect_cent = pygame.Rect(
				self.ancho_rect_lat+self.ancho_rect_lat_2,
				0,
				self.ancho_rect_central,
				self.alto)
		self.rect_izq = pygame.Rect(
				self.ancho_rect_lat_2,
				0,
				self.ancho_rect_lat,
				self.alto)
		self.rect_der = pygame.Rect(
				self.ancho-(self.ancho_rect_lat+self.ancho_rect_lat_2),
				0,
				self.ancho_rect_lat,
				self.alto)
		self.rect_izq_2 = pygame.Rect(
				0,
				self.alto/2-self.alto/4,
				self.ancho_rect_lat_2,
				self.alto/2)
		self.rect_der_2 = pygame.Rect(
				self.ancho-self.ancho_rect_lat_2,
				self.alto/2-self.alto/4,
				self.ancho_rect_lat_2,
				self.alto/2)
		self.paleta_img = self.crear_paleta_img()
										
	def dibujar(self,ventana):
		ventana.pygame.blit(self.paleta_img,
				(self.punto.x,self.punto.y))
						
	def crear_paleta_img(self):
		paleta_img = pygame.Surface((self.ancho,self.alto),
									pygame.SRCALPHA,32)				
		color = [160,20,20]
		pygame.draw.rect(paleta_img,color,self.rect_izq)
		pygame.draw.rect(paleta_img,color,self.rect_der)
		color = [140,140,140]
		pygame.draw.rect(paleta_img,color,self.rect_izq,1)
		pygame.draw.rect(paleta_img,color,self.rect_der,1)
		color = [120,120,120]
		pygame.draw.rect(paleta_img,color,self.rect_cent)
		color = [140,140,140]
		pygame.draw.rect(paleta_img,color,self.rect_cent,1)
		pygame.draw.rect(paleta_img,color,self.rect_izq_2)
		pygame.draw.rect(paleta_img,color,self.rect_der_2)
		return paleta_img
					
	def colision_izq(self,ventana):
		return self.punto.x <= ventana.marco
		
	def colision_der(self,ventana):
		return (self.punto.x+self.ancho >= 
				ventana.ancho-ventana.marco)
