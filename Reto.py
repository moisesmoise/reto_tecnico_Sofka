from datos import preguntas
from datos import premios_rondas
from Pregunta import Pregunta
import random


def juego_nuevo(preguntas):
    print("""Bienvenido a ¿Quién quiere ser millonario? versión Colombia
    Si respondes bien, ganas y vas acumulando dinero
    Si respondes mal o algo que no te piden
    Sales del juego y pierdes el acumulado
    En cualquier momento puedes retirarte y llevarte el acumulado
    """)
    puntaje = 0
    for i in range(5):
        # se usa libreria random para seleccionar un pregunta de cada categoria
        # categoria 1 [0,4], categoria 2 [5,9], categoria 3 [10, 14], etc
        k = (i*5) + random.randint(0,4)
        f = preguntas[k]
        print(f.mensaje)
        # Se crea loop while asegurar que el participante de una respuesta si/no
        m = 0
        while m == 0:
            continuar = input("Deseas continuar y responder? (si o no): ")
            if any(continuar.lower() == f for f in ["si", "s", 1]):
                m = 1
            elif any(continuar.lower() == f for f in ["no", "n", 0]):
                print("Te quedaste con lo que has ganado hasta ahora")
                m = 1
                return puntaje
            else:
                print("Por favor introduce si o no")
        respuesta = input("Su respuesta es (A, B, C o D): ")
        if respuesta.upper() == f.respuesta:
            if i == 4:
                print("Ganaste ¿Quién Quiere ser Millonario? Colombia")
            else:
                print("Pasaste a la siguiente categoria")
            print(f"Y ganaste {premios_rondas[i]}\n")
            puntaje = puntaje + 1
            
        else:
            print("Perdiste")
            break
    return puntaje

def premios(ronda):
    ganancia = 0
    for i in range(ronda):
        ganancia = ganancia + premios_rondas[i]
    print (f"En total has ganado $ {ganancia}")
    return ganancia    

def datos_participante():
    nombre = input("Cómo te llamas?: ")
    return nombre

gano = juego_nuevo(preguntas)
dinero_final = premios(gano)
datos = datos_participante()

print(f"{datos} ganó $ {dinero_final}")
