class cancion(object):
	titulo		= None
	interprete 	= None
	ubicacion 	= None
	def __init__(self, t:str,i:str,u:str):
		self.titulo 	= t
		self.interprete = i
		self.ubicacion	= u

	def obtenerTitulo(self):
		return self.titulo

	def obtenerInterprete(self):
		return self.interprete

	def obtenerUbicacion(self):
		return self.ubicacion

	def aString(self):
		return self.titulo + " - " + self.interprete