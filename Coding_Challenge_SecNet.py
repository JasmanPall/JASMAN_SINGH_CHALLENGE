import math

class Complex(object):
    def __init__(self, real_number, imaginary_part):
        self.real_number = real_number
        self.imaginary_part = imaginary_part
        pass

    def __add__(x, y):
        return Complex(x.real_number + y.real_number, x.imaginary_part + y.imaginary_part)

    def __sub__(x, y):
        return Complex(x.real_number - y.real_number, x.imaginary_part - y.imaginary_part)

    def __mul__(x, y):
        return Complex(x.real_number * y.real_number - x.imaginary_part * y.imaginary_part, x.imaginary_part * y.real_number + x.real_number * y.imaginary_part)

    def __truediv__(x, y):
        return Complex((x.real_number * y.real_number + x.imaginary_part * y.imaginary_part) / (y.real_number * y.real_number + y.imaginary_part * y.imaginary_part),(x.imaginary_part * y.real_number - x.real_number * y.imaginary_part) / (y.real_number * y.real_number + y.imaginary_part * y.imaginary_part))

    def mod(self):
        return Complex(math.sqrt(self.real_number * self.real_number + self.imaginary_part * self.imaginary_part), 0)

    def __str__(self):
        if (self.imaginary_part == 0):
            return "{0:.2f}".format(self.real_number) + '+0.00i'
        if (self.imaginary_part > 0):
            return "{0:.2f}".format(self.real_number) + '+' + "{0:.2f}".format(self.imaginary_part) + 'i'
        else:
            return "{0:.2f}".format(self.real_number) + '-' + "{0:.2f}".format(abs(self.imaginary_part)) + 'i'


if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')


#
# 0 9
# 9 0
#
# 9.00+9.00i
# -9.00+9.00i
# 0.00+81.00i
# 0.00+1.00i
# 9.00+0.00i
# 9.00+0.00i
#
# 42 -42
# 84 -84
# Expected Output
# Download
# 126.00-126.00i
# -42.00+42.00i
# 0.00-7056.00i
# 0.50+0.00i
# 59.40+0.00i
# 118.79+0.00i