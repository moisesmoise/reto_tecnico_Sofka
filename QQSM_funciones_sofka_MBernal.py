import random
import pickle

#FUNCIONES DEL JUEGO CONCURSO DE PREGUNTAS

def nuevo_juego():
    print("""Bienvenido a ¿Quién quiere ser millonario? versión Colombia
    Si respondes bien, ganas y vas acumulando dinero
    Si respondes mal o algo que no te piden
    Sales del juego y pierdes el acumulado
    """)    
    categorias_ganadas = 0
    for i in range(5):
        pregunta_azar = random.randint(0,3)
        print(f"Pregunta categoría {i+1}")
        print(preguntas[i][pregunta_azar][0])
        for j in range(4):
            print(opciones[i][pregunta_azar][j])
        k = 0
        while k == 0:
            continuar = input("Deseas continuar y responder? (si o no): ")
            if any(continuar.lower() == f for f in ["si", "s", 1]):
                k = 1
            elif any(continuar.lower() == f for f in ["no", "n", 0]):
                print("Te quedaste con lo que has ganado hasta ahora")
                k = 1
                return categorias_ganadas
            else:
                print("Por favor introduce si o no")

        respuesta = input("Su respuesta es (A, B, C o D): ")
        if respuesta.upper() == preguntas[i][pregunta_azar][1]:
            if i == 4:
                print("Ganaste ¿Quién Quiere ser Millonario? Colombia")
            else:
                print("Pasaste a la siguiente categoria")
            print(f"Y ganaste {premios_rondas[i]}")
            categorias_ganadas = categorias_ganadas + 1
            
        else:
            print("Perdiste")
            break
    return categorias_ganadas    

def premios(ronda):
    ganancia = 0
    for i in range(ronda):
        ganancia = ganancia + premios_rondas[i]
    print (f"En total has ganado $ {ganancia}")
    return ganancia    

def datos_participante():
    nombre = input("Cómo te llamas?: ")
    return nombre
    
def guardar_info(parti_guardado, prem_guardado):
    puesto_datos = parti_guardado + prem_guardado
    pickle_ent = open("Datos.participantes", "rb")
    dict_participantes = {}
    dict_participantes [parti_guardado] = prem_guardado



#DATOS DE PREGUNTAS
preguntas1 = (("¿Colombia tiene costas qué océano(s)?", "A"), 
("¿Cuál es el rio más grande que nace en Colombia?", "B"),
("¿Cuál es la capital de Colombia?", "C"),
("¿Quién es el presidente de Colombia actualmente (2018-2022)?", "D"),
("¿En qué ciudad se celebra el carnaval más grande de Colombia?", "A")
)
opciones1 = (("A. Atlántico y Pacífico", "B. Atlántico", "C. Atlántico y Caribe", "D. Índico"),
("A. Nilo", "B. Magdalena", "C. Orinoco", "D. Amazonas"),
("A. Caracas", "B. Medellín", "C. Bogotá", "D. Bucaramanga"),
("A. Juan Manuel Santos", "B. Juan Guaido", "C. Alvaro Uribe", "D. Ivan Duque"),
("A. Barranquilla", "B. Mocoa", "C. Puerto Gaitán", "D. Maicao")
)
preguntas2 = (("¿Cuál es la capital del departamento del Meta?", "A"),
("¿Cuál es la capital del departamento del Quindío?", "B"),
("¿Cuál es la capital del departamento de Putumayo?", "C"),
("¿Cuál es la capital del departamento de Atlántico?", "D"),
("¿Cuál es la capital del departamento de Boyaca?", "A")
)
opciones2 = (("A. Villavicencio", "B. Cumaral", "C. Arauca", "D. Yopal"),
("A. Salento", "B. Armenia", "C. Santa Rosa de Cabal", "D. Yarumal"),
("A. Leticia", "B. Pasto", "C. Mocoa", "D. Palmira"),
("A. Santa Marta", "B. Cienaga", "C. Aguachica", "D. Barranquilla"),
("A. Tunja", "B. Duitama", "C. Paipa", "D. Malagá")
) 
preguntas3 = (("¿Cuál es la capital del departamento de Vaupés?", "A"),
("¿Cuál es la capital del departamento del Cauca?", "B"),
("¿En qué departamento de Colombia está el Desierto de la Tatacoa?", "C"),
("¿En qué departamento queda Caño Cristales?", "D"),
("¿En qué departamento queda el Santuario de las Lajas?", "A")
)
opciones3 = (("A. Mitú", "B. Leticia", "C. Puerto Inirida", "D. Yopal"),
("A. Mocoa", "B. Popayán", "C. Palmira", "D. Cali"),
("A. Risaralda", "B. Tolima", "C. Huila", "D. Guajira"),
("A. Caquetá", "B. Guainía", "C. Casanare", "D. Meta"),
("A. Nariño", "B. Putumayo", "C. Valle del Cauca", "D. Cauca")
)
preguntas4 = (("¿Cuál es la montaña más alta de Colombia?", "A"),
("¿Qué deporte olímpico le ha dado más medallas olímpicas (oro, plata y bronce) a Colombia?", "B"),
("¿En qué año ganó el nobel de literatura Gabriel García Márquez?", "C"),
("¿En qué año ocurrió la castastrofe de Armero?", "D"),
("¿Cuál es la flor nacional de colombia?", "A")
)
opciones4 = (("A. Sierra Nevada de Santa Marta", "B. Nevado del Ruiz", "C. Volcán Galeras", "D. Nevado del Cocuy"),
("A. BMX", "B. Halterofilia", "C. Boxeo", "D. Atletismo"),
("A. 1995", "B. 1990", "C. 1982", "D. 1992"),
("A. 1995", "B. 1980", "C. 1990", "D. 1985"),
("A. Una orquídea", "B. Una rosa", "C. Una margarita", "D. Un clavel")
)
preguntas5 = (("¿En qué rango de millones de habitantes está Colombia (2022)?", "A"),
("¿Cuántos millones de km2 tiene la superficie de Colombia?", "B"),
("¿En qué rango de millones de habitantes está el área metropolitana de Bogotá?", "C"),
("¿Cuántas universidades públicas tiene Colombia?", "D"),
("En Colombia, ¿Cuántos salarios mínimos gana un congresista?", "E")
)
opciones5 = (("A. 50 -54", "B. 40 - 44", "C. 44 - 48", "D. 54 - 58"),
("A. 1,55", "B. 1,15", "C. 0,95", "D. 1,85"),
("A. 8,5 - 9,5", "B. 9,5 - 10,5", "C. 10,5 - 11,5", "D. 11,5 - 12,5"),
("A. 42", "B. 24", "C. 28", "D. 32"),
("A. 34", "B. 24", "C. 48", "D. 30")
)
preguntas = (preguntas1, preguntas2, preguntas3, preguntas4, preguntas5)
opciones = (opciones1, opciones2, opciones3, opciones4, opciones5)

#DATOS DE PREMIOS
premios_rondas = (10000, 50000, 150000, 500000, 1000000)

#PROGRAMA
 
participante = 0
participantes = []

gano = nuevo_juego()
dinero_final = premios(gano)
datos = datos_participante()

print(f"{datos} ganó $ {dinero_final}")

