import pygame
from Constantes import *
from Funciones import *

pygame.init()

boton_suma = crear_elemento_juego("Texturas/mas.png",60,60,470,300)
boton_resta = crear_elemento_juego("Texturas/menos.png",60,60,50,300)
boton_volver = crear_elemento_juego("Texturas/textura_respuesta.jpg",100,40,10,10)


def administrar_botones(boton_suma:dict,boton_resta:dict,boton_volver:dict,datos_juego:dict,pos_mouse:tuple) -> str:
    ventana = "ajustes"
    
    if boton_suma["rectangulo"].collidepoint(pos_mouse):
        if datos_juego["volumen_musica"] <= 95:
            datos_juego["volumen_musica"] += 5
            SONIDO_ACIERTO.play()
        else:
            SONIDO_ERROR.play()
    elif boton_resta["rectangulo"].collidepoint(pos_mouse):
        if datos_juego["volumen_musica"] > 0:
            datos_juego["volumen_musica"] -= 5
            SONIDO_ACIERTO.play()
        else: 
            SONIDO_ERROR.play()
    elif boton_volver["rectangulo"].collidepoint(pos_mouse):
        SONIDO_ACIERTO.play()
        ventana = "menu"

    return ventana

def mostrar_ajustes(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_juego:dict) -> str:
    ventana = "ajustes"
    
    for evento in cola_eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            ventana = administrar_botones(boton_suma,boton_resta,boton_volver,datos_juego,evento.pos)
            
    
    pantalla.blit(FONDO_AJUSTES,(0,0))
    
    pantalla.blit(boton_suma["superficie"],boton_suma["rectangulo"])
    pantalla.blit(boton_resta["superficie"],boton_resta["rectangulo"])
    pantalla.blit(boton_volver["superficie"],boton_volver["rectangulo"])

    mostrar_texto(pantalla,"Volumen",(175,220),FUENTE_GEORGIA_50,COLOR_NEGRO)
    mostrar_texto(pantalla,f"{datos_juego["volumen_musica"]} %",(230,300),FUENTE_GEORGIA_50,COLOR_NEGRO)
    mostrar_texto(boton_volver["superficie"],"Volver",(5,5),FUENTE_GEORGIA_20,COLOR_BLANCO)

    return ventana
    

