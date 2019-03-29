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
