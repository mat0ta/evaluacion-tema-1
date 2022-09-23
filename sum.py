class Sum:
    def __init__(self):
        self.matriz = []
        self.y = 1
    def sum(self):
        if self.y < 5:
            self.matriz.append([self.y, self.y, self.y, self.y * 3])
            self.y += 1
            self.sum()
        else:
            print(self.matriz)