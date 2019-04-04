from Punto import *

class Bloque:
	#self, int, int, int, int => None
	def __init__(self,x,y,ancho,alto):
		self.punto = Punto(x,y)
		self.ancho = ancho
		self.alto = alto
