import string
import range

if __name__ == "__main__":
    string = string.String()
    string.checkString()

    range1 = range.Range(-10, 0)
    range1.generate()
    range2 = range.Range(0, 50, True, 5)
    range2.generate()
    range3 = range.Range(0, 10)
    range3.generate()