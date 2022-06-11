import random
#DATOS DE PREGUNTAS
preguntas1 = (("¿Colombia tiene costas qué océano(s)?", "A"), 
("¿Cuál es el rio más grande que nace en Colombia?", "B"),
("¿Cuál es la capital de Colombia?", "C"),
("¿Quién es el presidente de Colombia actualmente (2018-2022)?", "D"),
("¿En qué ciudad se celebra el carnaval más grande de Colombia?", "A")
)
opciones1 = (("Atlántico y Pacífico", "Atlántico", "Atlántico y Caribe", "Índico"),
("Nilo", "Magdalena", "Orinoco", "Amazonas"),
("Caracas", "Medellín", "Bogotá", "Bucaramanga"),
("Juan Manuel Santos", "Juan Guaido", "Alvaro Uribe", "Ivan Duque"),
("Barranquilla", "Mocoa", "Puerto Gaitán", "Maicao")
)
preguntas2 = (("¿Cuál es la capital del departamento del Meta?", "A"),
("¿Cuál es la capital del departamento del Quindío?", "B"),
("¿Cuál es la capital del departamento de Putumayo?", "C"),
("¿Cuál es la capital del departamento de Atlántico?", "D"),
("¿Cuál es la capital del departamento de Boyaca?", "A")
)
opciones2 = (("Villavicencio", "Cumaral", "Arauca", "Yopal"),
("Salento", "Armenia", "Santa Rosa de Cabal", "Yarumal"),
("Leticia", "Pasto", "Mocoa", "Palmira"),
("Santa Marta", "Cienaga", "Aguachica", "Barranquilla"),
("Tunja", "Duitama", "Paipa", "Malagá")
) 
preguntas3 = (("¿Cuál es la capital del departamento de Vaupés?", "A"),
("¿Cuál es la capital del departamento del Cauca?", "B"),
("¿En qué departamento de Colombia está el Desierto de la Tatacoa?", "C"),
("¿En qué departamento queda Caño Cristales?", "D"),
("¿En qué departamento queda el Santuario de las Lajas?", "A")
)
opciones3 = (("Mitú", "Leticia", "Puerto Inirida", "Yopal"),
("Mocoa", "Popayán", "Palmira", "Cali"),
("Risaralda", "Tolima", "Huila", "Guajira"),
("Caquetá", "Guainía", "Casanare", "Meta"),
("Nariño", "Putumayo", "Valle del Cauca", "Cauca")
)
preguntas4 = (("¿Cuál es la montaña más alta de Colombia?", "A"),
("¿Qué deporte olímpico le ha dado más medallas olímpicas (oro, plata y bronce) a Colombia?", "B"),
("¿En qué año ganó el nobel de literatura Gabriel García Márquez?", "C"),
("¿En qué año ocurrió la castastrofe de Armero?", "D"),
("¿Cuál es la flor nacional de colombia?", "A")
)
opciones4 = (("Sierra Nevada de Santa Marta", "Nevado del Ruiz", "Volcán Galeras", "Nevado del Cocuy"),
("BMX", "Halterofilia", "Boxeo", "Atletismo"),
("1995", "1990", "1982", "1992"),
("1995", "1980", "1990", "1985"),
("Una orquídea", "Una rosa", "Una margarita", "Un clavel")
)
preguntas5 = (("¿En qué rango de millones de habitantes está Colombia (2022)?", "A"),
("¿Cuántos millones de km2 tiene la superficie de Colombia?", "B"),
("¿En qué rango de millones de habitantes está el área metropolitana de Bogotá?", "C"),
("¿Cuántas universidades públicas tiene Colombia?", "D"),
("En Colombia, ¿Cuántos salarios mínimos gana un congresista?", "E")
)
opciones5 = (("50 -54", "40 - 44", "44 - 48", "54 - 58"),
("1,55", "1,15", "0,95", "1,85"),
("8,5 - 9,5", "9,5 - 10,5", "10,5 - 11,5", "11,5 - 12,5"),
("42", "24", "28", "32"),
("34", "24", "48", "30")
)
preguntas = (preguntas1, preguntas2, preguntas3, preguntas4, preguntas5)
opciones = (opciones1, opciones2, opciones3, opciones4, opciones5)

i=0
pregunta_azar = random.randint(0,3)
print(pregunta_azar)
print(f"Pregunta categoría {i+1}")
for j in range(4):
    print(opciones[i][pregunta_azar][j])
