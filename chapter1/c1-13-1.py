
# 1.13.1: A Fraction Class

def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n


class Fraction:

    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    
    def __str__(self):
        return f'{self.num}/{self.den}'


    def show(self):
        print(''.join(str(self.num), '/', str(self.den)))

    
    def __add__(self, other):
        newnum = self.num * other.den + self.den * other.num
        newden = self.den * other.den
        common = gcd(newnum, newden)

        return Fraction(newnum // common, newden // common)

    
    def __sub__(self, other):
        newOther = Fraction(other.num * -1, other.den)
        
        return self.__add__(self, newOther)


    def __mul__(self, other):
        newnum = self.num * other.num
        newden = self.den * other.den

        return Fraction(newnum // common, newden // common)


    def __div__(self, other):
        newOther = Fraction(other.den, other.num)

        return self.__mul__(self, newOther)


    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        
        return firstnum == secondnum

    
    def __gt__(self, other):
        return (self.num / self.den) > (other.num / other.den)


    def __lt__(self, other):
        return (self.num / self.den) < (other.num / other.den)


