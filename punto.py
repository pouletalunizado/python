class Punto:
 	def __init__(self, x , y):
 		self.mover(x, y)
 	def mover(self, x, y):
 	    self.x = x
 	    self.y = y
punto =Punto(4, 2)
print (punto.x, punto.y)
