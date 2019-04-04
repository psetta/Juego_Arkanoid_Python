class Punto:
	#self, numeric, numeric
	def __init__(self,x,y):
		self.x = x
		self.y = y
		
	#self, Punto => Punto
	def __add__(self,other):
		return Punto(self.x+other.x,self.y+other.y)
		
	#self, Punto => Punto
	def __sub__(self,other):
		return Punto(self.x-other.x,self.y-other.y)
		
	#self, Punto => Punto
	def __mul__(self,other):
		return Punto(self.x*other.x,self.y*other.y)
		
	#self => int
	def __len__(self):
		return 2
	
	#self => string	
	def __str__(self):
		return "Punto({0},{1})".format(self.x,self.y)
		
	#self => int
	def __getitem__(self,item):
		if item == 0:
			return self.x
		elif item == 1:
			return self.y
		else:
			raise IndexError()
