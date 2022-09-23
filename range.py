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