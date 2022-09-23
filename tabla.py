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
                self.created = False
                if self.arg_1 < 1 or self.arg_1 > 9 or self.arg_2 < 1 or self.arg_2 > 9:
                    raise ValueError
                break
            except ValueError:
                print('Introduce un número del 1 al 9 porfavor.')

    def tabla(self):
        if self.arg_1 > 0 and self.created == False:
            self.matrix.append([])
            self.arg_1 -= 1
            self.tabla()
        else:
            self.created = True
            if self.count == 0:
                self.arg_1 = self.arg_1_fix
            if self.count < self.arg_2 and self.arg_1 > 0:
                self.matrix[self.arg_1_fix - self.arg_1].append(' * ')
                self.count += 1
                self.tabla()
            else:
                self.count = 0
                self.arg_1 -= 1
                self.tabla()
        print(self.matrix)