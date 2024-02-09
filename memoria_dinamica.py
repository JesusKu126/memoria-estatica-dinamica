class memoria_dinamica:
    def __init__(self):
        self.frutas= ["Mango", "Manzana", "Banana", "Uvas"]
        print(self.frutas)
        self.frutas.remove("Mango")
        self.frutas.remove("Manzana")
        self.frutas.append("Sandia")
        print(self.frutas)
memoria_dinamica()