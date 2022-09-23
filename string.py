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