import pygame as pg

from reproductor import *
from cancion import *
from ajustes import *

def escribir_texto(surf,text,size,x,y):
	'''
	Funcion que escribe el texto en la pantalla de la interfaz
	Variables:
		surf: superficie donde será escrito el texto.
		text: string con el texto que sera escrito.
		size: tamaño de la letra.
		x	: ubicacion horizontal del texto.
		y	: ubicacion vertical del texto.
	'''
	font = pg.font.Font('binchrt.ttf',size) # Fuente que es utilizada para mostrar el texto.
	text_surface = font.render(text, True, BLACK) # Texto renderizado.
	text_rect = text_surface.get_rect() # Rectangulo del texto renderizado.
	text_rect.midtop = (x,y) # Ubicacion del texto en la pantalla.
	surf.blit(text_surface,text_rect) # Muestra en pantalla el texto.

def pantalla_inicio(c):
	'''
	Funcion que genera la pantalla de inicio del administrador de musica
	Variables:
		c: Cancion con la que se inicia la reproducción
	'''
	screen = pg.display.set_mode((ANCHO,ALTO)) # Se inicia la ventana del reproductor
	clock = pg.time.Clock() # Se inicia el reloj de Pygame
	screen.fill(GREY) # Rellena la pantalla con el color especificado
	
	# Impresion de texto en pantalla con la función escribir_texto()
	escribir_texto(screen,"1. Cargar Lista de reproduccion",(ALTO/20),ANCHO/2,ALTO-((8*ALTO)/10))
	escribir_texto(screen,"2. Mostrar Lista de reproduccion",(ALTO/20),ANCHO/2,ALTO-((7*ALTO)/10))
	escribir_texto(screen,"3. Eliminar Canción",(ALTO/20),ANCHO/2,ALTO-((6*ALTO)/10))
	escribir_texto(screen,"4. Reproducir",(ALTO/20),ANCHO/2,ALTO-((5*ALTO)/10))
	escribir_texto(screen,"5. Pausar",(ALTO/20),ANCHO/2,ALTO-((4*ALTO)/10))
	escribir_texto(screen,"6. Parar",(ALTO/20),ANCHO/2,ALTO-((3*ALTO)/10))
	escribir_texto(screen,"7. Próxima canción",(ALTO/20),ANCHO/2,ALTO-((2*ALTO)/10))
	escribir_texto(screen,"8. Salir del administrador de música",(ALTO/20),ANCHO/2,ALTO-(ALTO/10))
	escribir_texto(screen,"Titulo: " + c.titulo,(ALTO/20),ANCHO/4,ALTO-((9*ALTO)/10))
	escribir_texto(screen,"Interprete: " + c.interprete,(ALTO/20),(3*ANCHO)/4,ALTO-((9*ALTO)/10))

	pg.display.flip() # Se "voltea la pantalla" y se muestra la información nueva.

def esperar_tecla():
	'''
	Función que espera que se presione una tecla y devuelve el identificador de la misma.
	'''
	pg.event.wait() # Se activa el "event listener" de Pygame
	waiting = True # Variable de ejecución
	key = None # Variable donde se almacenará el identificador de la tecla
	while waiting:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				# Si se presiona la "x" de la ventana, se cierra el programa.
				waiting = False
				pg.quit()
			if event.type == pg.KEYUP:
				# Si se presiona una tecla, se cierra la ejecucion y sale el identificador.
				waiting = False
				key = event.key

	return key

c = cancion("Easy to love","Billie Holyday","/home/miguelp/pygame/ProyAlgos/src/Easy To Love.mp3")
r = reproductor(c)
while True:
	# Ciclo de ejecución del programa
	pantalla_inicio(r.actual)
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
	else:
		pass