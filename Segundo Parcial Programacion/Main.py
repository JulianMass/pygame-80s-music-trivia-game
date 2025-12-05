import pygame
from Constantes import *
from Funciones import *
from Menu import *
from Juego import *
from Rankings import *
from Ajustes import *
from Terminado import *
import random


pygame.init
pygame.display.set_caption("Preguntados de los 80")
icono = pygame.image.load("Texturas\icono.png")
pygame.display.set_icon(icono)

pantalla = pygame.display.set_mode(PANTALLA)
datos_juego = crear_datos_juego()
reloj = pygame.time.Clock()
ventana_actual = "menu"
bandera_juego = False
lista_rankings = []

evento_1_s = pygame.USEREVENT
pygame.time.set_timer(evento_1_s,1000)

cuadro_pregunta = crear_elemento_juego("Texturas/textura_pregunta.jpg",ANCHO_PREGUNTA,ALTO_PREGUNTA,120,100)
pregunta_actual = obtener_pregunta_actual(datos_juego,lista_preguntas)
lista_respuestas = crear_lista_respuestas(4,"Texturas/textura_respuesta.jpg",ANCHO_RESPUESTA,ALTO_RESPUESTA,195,275)


while True:
    reloj.tick(FPS)
    cola_eventos = pygame.event.get()

    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            ventana_actual= "salir"

    if ventana_actual == "menu":
        reiniciar_estadisticas(datos_juego)
        ventana_actual = mostrar_menu(pantalla,cola_eventos)

    elif ventana_actual == "jugar":
        if bandera_juego == False:
            iniciar_musica("Sonidos/Queen_Bohemian_Rhapsody.mp3",datos_juego.get("volumen_musica",0))
            random.shuffle(lista_preguntas)
            bandera_juego = True
        ventana_actual = mostrar_juego(pantalla,cola_eventos,datos_juego,cuadro_pregunta,lista_respuestas,pregunta_actual)

    elif ventana_actual == "ajustes":
        ventana_actual = mostrar_ajustes(pantalla,cola_eventos,datos_juego)

    elif ventana_actual == "rankings":
        ventana_actual = mostrar_rankings(pantalla,cola_eventos,lista_rankings)

    elif ventana_actual == "terminado":
        if bandera_juego == True:
            pygame.mixer.music.stop()
            bandera_juego = False
        ventana_actual = mostrar_game_over(pantalla,datos_juego,cola_eventos,lista_rankings)

    elif ventana_actual == "salir":
        break

    pygame.display.flip()

pygame.quit()



