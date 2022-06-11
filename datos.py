from Pregunta import Pregunta

mensaje_preguntas = [
"¿Colombia tiene costas qué océano(s)?\nA. Atlántico y Pacífico\nB. Atlántico\nC. Atlántico y Caribe\nD. Índico\n",
"¿Rio más grande que nace en Colombia?\nA. Nilo\nB. Magdalena\nC. Orinoco\nD. Amazonas\n",
"¿Capital de Colombia?\nA. Caracas\nB. Medellín\nC. Bogotá\nD. Bucaramanga\n",
"¿Presidente de Colombia (2018-2022)?\nA. Juan M. Santos\nB. Juan Guaido\nC. Alvaro Uribe\nD. Ivan Duque\n",
"¿Ciudad con carnaval más grande de Colombia?\nA. Barranquilla\nB. Mocoa\nC. Puerto Gaitán\nD. Maicao\n",
"¿Capital del departamento del Meta?\nA. Villavicencio\nB. Cumaral\nC. Arauca\nD. Yopal\n",
"¿Capital del departamento del Quindío?\nA. Salento\nB. Armenia\nC. Santa Rosa de Cabal\nD. Yarumal\n",
"¿Capital del departamento de Putumayo?\nA. Leticia\nB. Pasto\nC. Mocoa\nD. Palmira\n",
"¿Capital del departamento de Atlántico?\nA. Santa Marta\nB. Cienaga\nC. Aguachica\nD. Barranquilla\n",
"¿Capital del departamento de Boyaca?\nA. Tunja\nB. Duitama\nC. Paipa\nD. Malagá\n",
"¿Capital del departamento de Vaupés?\nA. Mitú\nB. Leticia\nC. Puerto Inirida\nD. Yopal\n",
"¿Capital del departamento del Cauca?\nA. Mocoa\nB. Popayán\nC. Palmira\nD. Cali\n",
"¿Departamento del Desierto de la Tatacoa?\nA. Risaralda\nB. Tolima\nC. Huila\nD. Guajira\n",
"¿Departamento de Caño Cristales?\nA. Caquetá\nB. Guainía\nC. Casanare\nD. Meta\n",
"¿Departamento del Santuario de las Lajas?\nA. Nariño\nB. Putumayo\nC. Valle del Cauca\nD. Cauca\n",
"¿Montaña más alta de Colombia?\nA. Sierra Nevada de Santa Marta\nB. Nevado del Ruiz\nC. Volcán Galeras\nD. Nevado del Cocuy\n",
"¿Deporte olímpico con más medallas olímpicas para Colombia?\nA. BMX\nB. Halterofilia\nC. Boxeo\nD. Atletismo\n",
"¿Año del nobel de Gabriel García Márquez?\nA. 1995\nB. 1990\nC. 1982\nD. 1992\n",
"¿Año de la castastrofe de Armero?\nA. 1995\nB. 1980\nC. 1990\nD. 1985\n",
"¿Flor nacional de colombia?\nA. Una orquídea\nB. Una rosa\nC. Una margarita\nD. Un clavel\n",
"¿Millones de habitantes en Colombia (2022)?\nA. 50 -54\nB. 40 - 44\nC. 44 - 48\nD. 54 - 58\n",
"¿Millones de km2 en Colombia?\nA. 1,55\nB. 1,15\nC. 0,95\nD. 1,85\n",
"¿Millones de habitantes en el área metro. de Bogotá?\nA. 8,5 - 9,5\nB. 9,5 - 10,5\nC. 10,5 - 11,5\nD. 11,5 - 12,5\n",
"¿Universidades públicas en Colombia?\nA. 42\nB. 24\nC. 28\nD. 32\n",
"En Colombia, ¿Cuántos salarios mínimos gana un congresista?\nA. 34\nB. 24\nC. 48\nD. 30\n"
]

preguntas = [
    Pregunta(mensaje_preguntas[0], "A"),
    Pregunta(mensaje_preguntas[1], "B"),
    Pregunta(mensaje_preguntas[2], "C"),
    Pregunta(mensaje_preguntas[3], "D"),
    Pregunta(mensaje_preguntas[4], "A"),
    Pregunta(mensaje_preguntas[5], "A"),
    Pregunta(mensaje_preguntas[6], "B"),
    Pregunta(mensaje_preguntas[7], "C"),
    Pregunta(mensaje_preguntas[8], "D"),
    Pregunta(mensaje_preguntas[9], "A"),
    Pregunta(mensaje_preguntas[10], "A"),
    Pregunta(mensaje_preguntas[11], "B"),
    Pregunta(mensaje_preguntas[12], "C"),
    Pregunta(mensaje_preguntas[13], "D"),
    Pregunta(mensaje_preguntas[14], "A"),
    Pregunta(mensaje_preguntas[15], "A"),
    Pregunta(mensaje_preguntas[16], "B"),
    Pregunta(mensaje_preguntas[17], "C"),
    Pregunta(mensaje_preguntas[18], "D"),
    Pregunta(mensaje_preguntas[19], "A"),
    Pregunta(mensaje_preguntas[20], "A"),
    Pregunta(mensaje_preguntas[21], "B"),
    Pregunta(mensaje_preguntas[22], "C"),
    Pregunta(mensaje_preguntas[23], "D"),
    Pregunta(mensaje_preguntas[24], "A")
]

def juego_nuevo(preguntas):
    puntaje = 0
    for pregunta in preguntas:
        print(pregunta.mensaje)
        respuesta = input("Respuesta :")
        if respuesta.upper() == pregunta.respuesta:
            puntaje += 1
    print(str(puntaje))

juego_nuevo(preguntas)