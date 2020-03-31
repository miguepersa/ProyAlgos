import pygame as pg

from reproductor import *
from cancion import *
from ajustes import *

def escribir_texto(surf,text,size,x,y):
	font = pg.font.Font('binchrt.ttf',size)
	text_surface = font.render(text, True, BLACK)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x,y)
	surf.blit(text_surface,text_rect)

def pantalla_inicio(c):
	screen = pg.display.set_mode((ANCHO,ALTO))
	clock = pg.time.Clock()
	screen.fill(GREY)
	
	escribir_texto(screen,"1. Cargar Lista de reproduccion",30,ANCHO/2,ALTO-480)
	escribir_texto(screen,"2. Mostrar Lista de reproduccion",30,ANCHO/2,ALTO-420)
	escribir_texto(screen,"3. Eliminar Canción",30,ANCHO/2,ALTO-360)
	escribir_texto(screen,"4. Reproducir",30,ANCHO/2,ALTO-300)
	escribir_texto(screen,"5. Pausar",30,ANCHO/2,ALTO-240)
	escribir_texto(screen,"6. Parar",30,ANCHO/2,ALTO-180)
	escribir_texto(screen,"7. Próxima canción",30,ANCHO/2,ALTO-120)
	escribir_texto(screen,"8. Salir del administrador de música",30,ANCHO/2,ALTO-60)
	escribir_texto(screen,"Titulo: " + c.titulo,30,ANCHO/4,ALTO-540)
	escribir_texto(screen,"Interprete: " + c.interprete,30,(3*ANCHO)/4,ALTO-540)

	pg.display.flip()

def esperar_tecla():
	pg.event.wait()
	waiting = True
	key = None
	while waiting:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				waiting = False
				pg.quit()
			if event.type == pg.KEYUP:
				waiting = False
				key = event.key

	return key

c = cancion("Easy to love","Billie Holyday","/home/miguelp/pygame/ProyAlgos/src/Easy To Love.mp3")
r = reproductor(c)
while True:
	pantalla_inicio(c)
	key = esperar_tecla()
	if key == pg.K_1:
		pass
	elif key == pg.K_2:
		pass
	elif key == pg.K_3:
		pass
	elif key == pg.K_4:
		r.reproducir()
	elif key == pg.K_5:
		r.pausa()
	elif key == pg.K_6:
		r.parar()
	elif key == pg.K_7:
		pass
	elif key == pg.K_8:
		pg.quit()
		break