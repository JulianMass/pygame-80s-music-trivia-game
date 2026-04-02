import pygame
pygame.init()

COLOR_BLANCO = (255,255,255)
COLOR_NEGRO = (0,0,0)
ANCHO = 600
ALTO = 600
PANTALLA = (ANCHO,ALTO)
FPS = 31

ANCHO_PREGUNTA = 370
ALTO_PREGUNTA = 150
ANCHO_RESPUESTA = 220
ALTO_RESPUESTA = 60
ANCHO_BOTON = 300
ALTO_BOTON = 60

TIEMPO_TOTAL = 30
CANTIDAD_VIDAS = 3
PUNTUACION_ACIERTO = 100
PUNTUACION_ERROR = 25


FUENTE_SISTEMA = pygame.font.SysFont("Georgia",25,True)
FUENTE_GEORGIA_20 = pygame.font.SysFont("Georgia",20)
FUENTE_GEORGIA_25 = pygame.font.SysFont("Georgia",25)
FUENTE_GEORGIA_30 = pygame.font.SysFont("Georgia",30)
FUENTE_GEORGIA_40 = pygame.font.SysFont("Georgia",40)
FUENTE_GEORGIA_50 = pygame.font.SysFont("Georgia",50)

SONIDO_ACIERTO = pygame.mixer.Sound("Sonidos/acierto.mp3")
SONIDO_ERROR = pygame.mixer.Sound("Sonidos/error.mp3")

FONDO_JUEGO = pygame.image.load("Texturas/fondo_juego.jpg")
FONDO_JUEGO = pygame.transform.scale(FONDO_JUEGO,PANTALLA)
FONDO_AJUSTES = pygame.image.load("Texturas/fondo_ajustes.jpg")
FONDO_AJUSTES = pygame.transform.scale(FONDO_AJUSTES, PANTALLA)
FONDO_TERMINADO = pygame.image.load("Texturas/fondo_terminado.jpg")
FONDO_TERMINADO = pygame.transform.scale(FONDO_TERMINADO, PANTALLA)
FONDO_RANKINGS = pygame.image.load("Texturas/fondo_rankings.jpg")
FONDO_RANKINGS = pygame.transform.scale(FONDO_RANKINGS, PANTALLA)

