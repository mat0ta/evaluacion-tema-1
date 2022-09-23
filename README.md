<h1 align="center">EVALUACION-TEMA-1</h1>

En este [repositorio](https://github.com/mat0ta/evaluacion-tema-1) quedan resueltos los ejercicios la tarea de esta semana. Puedes encontrar otros proyectos y tareas en mi perfil de GitHub: [mat0ta](https://github.com/mat0ta).

<h2>Ejercicio 1</h2>

La siguiente matriz (o lista con listas anidadas) debe cumplir una condición, y es que en cada fila el cuarto elemento siempre debe ser el resultado de sumar los tres primeros. óEres capaz de modificar las sumas incorrectas utilizando la tócnica del slicing?

El código empleado para crear dicho algoritmo es el siguiente:

```py

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

```

<h2>Ejercicio 2</h2>

Utilizando operadores lógicos, determina si una cadena de texto introducida por el usuario tiene una longitud mayor o igual que 3 y a su vez es menor que 10 (es suficiene con mostrar True o False).

El código empleado para crear dicho algoritmo es el siguiente:

```py

class String():
    def __init__(self):
        self.string = input("Introduce una palabra: ")
        self.counter = 0
        self.word = ""
    def checkString(self):
        if self.string != self.word:
            self.word += self.string[self.counter]
            self.counter += 1
            self.checkString()
        else:
            if self.counter >= 3 and self.counter < 10:
                print(True)
            else:
                print(False)

```

<h2>Ejercicio 3</h2>

Utilizando la función range() y la conversión a listas genera las siguientes listas dinómicamente:

El código empleado para crear dicho algoritmo es el siguiente:

```py

class Range():
    def __init__(self, start, end, is_skiping = False, step = 0):
        self.start = start
        self.end = end + 1
        self.is_skiping = is_skiping
        self.step = step
        self.matrix = []
    def generate(self):
        if not self.is_skiping:
            if self.start < self.end:
                self.matrix.append(self.start)
                self.start += 1
                self.generate()
            else:
                if self.end != self.start:
                    self.matrix.append(self.start)
                    self.start += 1
                    self.generate()
                print(self.matrix)
        else:
            if self.start % self.step == 0:
                self.matrix.append(self.start)
                self.start += 1
                self.generate()
            elif self.start != self.end:
                self.start += 1
                self.generate()
            else:
                print(self.matrix)
        if len(self.matrix) == self.end - 1:
            print(self.matrix)

```

<h2>Ejercicio 4</h2>

Crea un script llamado tabla.py que realice las siguientes tareas:

El código empleado para crear dicho algoritmo es el siguiente:

```py

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
            if self.count < self.arg_2 + self.count:
                self.matrix[self.count].append(' * ')
                self.arg_2 -= 1
                self.tabla()
            elif self.arg_1 > 1:
                self.count += 1
                self.arg_1 -= 1
                self.arg_2 = self.arg_2_fix
                self.tabla()
        return(self.matrix)

```

<h2>Ejercicio codewars</h2>

Resuelve y entrega este training de CodeWars

El código empleado para crear dicho algoritmo es el siguiente:

```py

def string_to_array(s):
    # your code here
    return(s.split(" "))

```

