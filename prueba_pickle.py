import pickle
from winsound import MB_ICONASTERISK

class concursante():

    def __init__ (self, nombre, premio):

        self.nombre = nombre
        self.premio = premio

    def informacion(self):
        print(self.nombre, "gano", self.premio)

nom = input("ingresar nombre: ")
ape = input("Ingresar apellido: ")

nombre1 = concursante(nom, ape)
nombre1.informacion()
gano = []
gano.append(nombre1) 
print (gano)

fichero = open("datos_participantes", "wb")
pickle.dump(gano, fichero)
fichero.close()
del (fichero)


# gano_2 = pickle.load (open ("datos_participantes", "rb"))
# gano_2.append("moises perdio") 
# print(gano_2)





