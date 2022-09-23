class Sum:
    def __init__(self):
        while True:
            try:
                self.numero = int(input('Introduce el tamaño de la matriz: '))
                break
            except ValueError:
                print('Introduce un número.')
        self.matriz = []
        self.y = 1
    def sum(self):
        if self.y <= self.numero:
            self.matriz.append([self.y, self.y, self.y, self.y * 3])
            self.y += 1
            self.sum()
        else:
            print(self.matriz)