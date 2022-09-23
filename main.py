import sum
import string
import range
import tabla
from totareadme import readme
from pprint import pprint

if __name__ == "__main__":
    readme("C:/Users/marti/Documents/GitHub/evaluacion-tema-1")

    sum.Sum().sum()

    string = string.String()
    string.checkString()

    range1 = range.Range(-10, 0)
    range1.generate()
    range2 = range.Range(0, 50, True, 5)
    range2.generate()
    range3 = range.Range(0, 10)
    range3.generate()

    for s in tabla.Tabla().tabla():
        print(*s)