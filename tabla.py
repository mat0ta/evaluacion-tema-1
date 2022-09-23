class Tabla():
    def __init__(self):
        while True:
            try:
                self.arg_1 = int(input('Introduce el primer argumento [1-9]: '))
                self.arg_1_fix = self.arg_1
                self.arg_2 = int(input('Introduce el segundo argumento [1-9]: '))
                self.arg_2_fix = self.arg_2
                self.matrix = []
                self.count = 0
                if self.arg_1 < 1 or self.arg_1 > 9 or self.arg_2 < 1 or self.arg_2 > 9:
                    raise ValueError
                break
            except ValueError:
                print('Introduce un número del 1 al 9 porfavor.')

    def tabla(self):
        if self.arg_1 > 0:
            self.matrix.append([])
            self.arg_1 -= 1
            self.tabla()
        else:
            self.arg_1 = self.arg_1_fix
            if self.count < self.arg_2:
                self.matrix[self.arg_1 - 1].append(self.arg_1 * self.arg_2)
                self.arg_1 -= 1
                self.count += 1
                self.tabla()
            self.matrix[self.arg_1_fix - self.arg_1].append(' * ')