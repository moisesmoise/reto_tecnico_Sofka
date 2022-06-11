from datos import preguntas
from Pregunta import Pregunta

def juego_nuevo(preguntas):
    puntaje = 0
    for pregunta in preguntas:
        print(pregunta.mensaje)
        respuesta = input("Respuesta :")
        if respuesta.upper() == pregunta.respuesta:
            puntaje += 1
    print(str(puntaje))

juego_nuevo(preguntas)