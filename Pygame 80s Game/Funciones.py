from Constantes import *
import os
import random
import csv

def crear_datos_juego() -> dict:
    datos_juego = {
        "nombre": "",
        "tiempo_restante": TIEMPO_TOTAL,
        "puntuacion": 0,
        "cantidad_vidas": CANTIDAD_VIDAS,
        "i_pregunta": 0,
        "volumen_musica": 100,
        "racha": 0,
        "comodines": {       
            "bomba": True,
            "x2": True,
            "doble_chance": True,
            "pasar": True
        },
        "x2_activo": False,           
        "doble_chance_activo": False,
        "saltar_pregunta": False
    }

    return datos_juego

def mostrar_texto(surface, text, pos, font, color=pygame.Color('white')):
    words = [word.split(' ') for word in text.splitlines()]  
    space = font.size(' ')[0]  
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, True, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  
                y += word_height  
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  
        y += word_height  


def crear_elemento_juego(textura:str,ancho_elemento:int,alto_elemento:int,pos_x:int,pos_y:int) -> dict | None:
    if os.path.exists(textura):
        elemento_juego = {}
        elemento_juego["superficie"] = pygame.image.load(textura)
        elemento_juego["superficie"] = pygame.transform.scale(elemento_juego["superficie"],(ancho_elemento,alto_elemento))
        elemento_juego["rectangulo"] = pygame.rect.Rect(pos_x,pos_y,ancho_elemento,alto_elemento)
    else:
        elemento_juego = None
    
    return elemento_juego


def obtener_pregunta_actual(datos_juego:dict,lista_preguntas:list) -> dict | None:
    if type(lista_preguntas) == list and len(lista_preguntas) > 0 and type(datos_juego) == dict and datos_juego.get("i_pregunta") != None:
        indice = datos_juego.get("i_pregunta")
        pregunta = lista_preguntas[indice]
    else:
        pregunta = None
    
    return pregunta

def mostrar_datos_juego(pantalla:pygame.Surface,datos_juego:dict) -> bool:
    if type(datos_juego) == dict:
        mostrar_texto(pantalla,f"Tiempo: {datos_juego.get("tiempo_restante")} segundos",(10,10),FUENTE_GEORGIA_20)
        mostrar_texto(pantalla,f"Puntuacion: {datos_juego.get("puntuacion")}",(10,40),FUENTE_GEORGIA_20)
        mostrar_texto(pantalla,f"Vidas: {datos_juego.get("cantidad_vidas")}",(10,70),FUENTE_GEORGIA_20)
        retorno = True
    else:
        retorno = False
        
    return retorno

def mezclar_lista(lista_preguntas:list) -> bool:
    if type(lista_preguntas) == list and len(lista_preguntas) > 0:
        retorno = True
        random.shuffle(lista_preguntas)
    else:
        retorno = False
    
    return retorno

def verificar_indice(datos_juego:dict,lista_preguntas:list) -> bool:
    if type(datos_juego) == dict and datos_juego.get("i_pregunta") != None:
        retorno = True
        if datos_juego["i_pregunta"] == len(lista_preguntas):
            datos_juego["i_pregunta"] = 0
            mezclar_lista(lista_preguntas)    
    else:
        retorno = False
        
    return retorno

def pasar_pregunta(datos_juego:dict,lista_preguntas:list) -> bool:
    if type(datos_juego) == dict and datos_juego.get("i_pregunta") != None:
        retorno = True
        datos_juego["i_pregunta"] += 1
        verificar_indice(datos_juego,lista_preguntas)
    else:
        retorno = False
        
    return retorno

def crear_lista_respuestas(cantidad_respuestas:int,textura:str,ancho:int,alto:int,x:int,y:int) -> list | None:
    if os.path.exists(textura):
        lista_respuestas = []

        for i in range (cantidad_respuestas):
            cuadro_respuesta = crear_elemento_juego(textura,ancho,alto,x,y)
            lista_respuestas.append(cuadro_respuesta)
            y += (alto + 20)
    else:
        lista_respuestas = None
    
    return lista_respuestas

def verificar_respuesta(pregunta_actual:dict,datos_juego:dict,respuesta:int,sonido_acierto:pygame.mixer.Sound,sonido_error:pygame.mixer.Sound) -> bool:
    if type(pregunta_actual) == dict and pregunta_actual.get("respuesta_correcta") != None:
        retorno = True
        
        if pregunta_actual.get("respuesta_correcta") == respuesta:
            modificar_puntuacion(datos_juego,100)
            sonido_acierto.play()
        else:
            modificar_puntuacion(datos_juego,-50)
            modificar_vida(datos_juego,-1)
            sonido_error.play()
    else:
        retorno = False
        
    return retorno

def modificar_vida(datos_juego:dict,incremento:int) -> bool:
    if type(datos_juego) == dict and datos_juego.get("cantidad_vidas") != None:
        retorno = True
        datos_juego["cantidad_vidas"] += incremento
    else:
        retorno = False
        
    return retorno
    
def modificar_puntuacion(datos_juego:dict,incremento:int) -> bool:
    if type(datos_juego) == dict and datos_juego.get("puntuacion") != None:
        retorno = True
        datos_juego["puntuacion"] += incremento
    else:
        retorno = False
        
    return retorno

def responder_pregunta(lista_preguntas:list,lista_respuestas:list,sonido_acierto:pygame.mixer.Sound,sonido_error:pygame.mixer.Sound,pos_mouse:tuple,pregunta_actual:dict,datos_juego:dict) -> bool:
        retorno = False
        for i in range(len(lista_respuestas)):
            if lista_respuestas[i]["rectangulo"].collidepoint(pos_mouse):
                respuesta = i + 1
                verificar_respuesta(pregunta_actual,datos_juego,respuesta,sonido_acierto,sonido_error)
                
                if pregunta_actual["respuesta_correcta"] == respuesta:
                    datos_juego["racha"] += 1

                    if datos_juego["racha"] >= 5:
                        datos_juego["cantidad_vidas"] += 1 
                        datos_juego["racha"] = 0  
                else:
                    datos_juego["racha"] = 0

                pasar_pregunta(datos_juego,lista_preguntas)
                retorno = True

        return retorno

def dibujar_pantalla(pantalla:pygame.Surface,datos_juego:dict,cuadro_pregunta:dict,lista_respuestas:dict,pregunta_actual:dict) -> None:
    if type(datos_juego) == dict and type(cuadro_pregunta) == dict:
        pantalla.blit(FONDO_JUEGO, (0, 0))
        mostrar_datos_juego(pantalla,datos_juego)

        mostrar_texto(cuadro_pregunta["superficie"],f"{pregunta_actual["descripcion"]}",(20,20),FUENTE_GEORGIA_25)
        pantalla.blit(cuadro_pregunta["superficie"],cuadro_pregunta["rectangulo"])

        for i in range(len(lista_respuestas)):
            mostrar_texto(lista_respuestas[i]["superficie"],f"{pregunta_actual.get(f"respuesta_{i+1}")}",(25,10),FUENTE_GEORGIA_20,COLOR_BLANCO)
            pantalla.blit(lista_respuestas[i]["superficie"],lista_respuestas[i]["rectangulo"])


def reiniciar_estadisticas(datos_juego:dict) -> bool:
    if type(datos_juego) == dict:
        retorno = True
        datos_juego.update({
            "tiempo_restante": TIEMPO_TOTAL,
            "puntuacion": 0,
            "cantidad_vidas": CANTIDAD_VIDAS,
            "racha": 0,  
            "comodines": {       
                "bomba": True,
                "x2": True,
                "doble_chance": True,
                "pasar": True
            },
            "x2_activo": False,           
            "doble_chance_activo": False,
            "saltar_pregunta": False
        })
    else:
        retorno = False
        
    return retorno


def leer_preguntas_csv(nombre_archivo="preguntas.csv"):
    lista_preguntas = []
    with open(nombre_archivo, mode="r", encoding="utf-8") as archivo:
        reader = csv.DictReader(archivo)
        for fila in reader:
            fila["respuesta_correcta"] = int(fila["respuesta_correcta"])
            lista_preguntas.append(fila)
    return lista_preguntas

def iniciar_musica(ruta_archivo:str,volumen:int):
    pygame.mixer.init()
    pygame.mixer.music.load(ruta_archivo)
    pygame.mixer.music.set_volume(volumen/ 100)
    pygame.mixer.music.play(-1,start=1.8)


def dibujar_comodines(pantalla:pygame.Surface,botones_comodines:list) -> None:
    for boton in botones_comodines:
        pantalla.blit(boton["superficie"], boton["rectangulo"])


def usar_bomba(pregunta_actual: dict, lista_respuestas: list) -> None:
    correcta = pregunta_actual["respuesta_correcta"] - 1  
    indices = list(range(len(lista_respuestas)))  
    indices.remove(correcta)  

    eliminar = random.sample(indices, 2) 
    eliminar.sort(reverse=True)
    for i in eliminar:
        del lista_respuestas[i] 


def usar_comodin_x2(datos_juego: dict) -> None:
    if datos_juego["comodines"]["x2"]:
        datos_juego["puntuacion"] *= 2  
        datos_juego["comodines"]["x2"] = False 

def usar_comodin_doble_chance(datos_juego: dict) -> None:
    if datos_juego["comodines"]["doble_chance"]:
        datos_juego["comodines"]["doble_chance"] = False  
        datos_juego["doble_chance_activo"] = True 

def usar_comodin_pasar(datos_juego: dict, lista_preguntas: list) -> None:
    if datos_juego["comodines"]["pasar"]:
        datos_juego["comodines"]["pasar"] = False  
        datos_juego["i_pregunta"] += 1  
        if datos_juego["i_pregunta"] >= len(lista_preguntas):
            datos_juego["i_pregunta"] = 0


