class memoria_estatica:
    def __init__(self):
        self.calificaciones=[]
        for i in range(5):
            elemento= input("Ingrese la calificación {}: ".format(i+1))
            self.calificaciones.append(elemento)
        print("Las calificaciones son: ", self.calificaciones)
memoria_estatica()