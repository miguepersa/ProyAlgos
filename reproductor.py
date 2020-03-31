import pygame as pg

class reproductor(object):
	def __init__(self,c):
		pg.init()
		pg.mixer.init()
		# pg.display.set_caption(TITULO)
		self.actual = c
		self.playing = False
		self.paused	= False
		pg.mixer.music.load(c.ubicacion)

	def cargarCancion(self,c):
		self.actual = c
		pg.mixer.music.load(c.ubicacion)

	def reproducir(self):
		if not self.paused:	
			pg.mixer.music.play()
			self.playing = True
		else:
			pg.mixer.music.unpause()
			self.paused = False
			self.playing = True

	def parar(self):
		pg.mixer.music.stop()
		self.playing = False

	def pausa(self):
		pg.mixer.music.pause()
		self.playing = False
		self.paused = True

	def estaTocandoCancion(self):
		return self.playing