i = input
ir = raw_input
o = open
    
class R:
    def __init__(self, p, q):
        self.p = p
        self.q = q
        self.__div__ = self.div
        self.__trueDiv__ = self.div
        self.__floorDiv__ = self.div
    def div(self, R2):
        return R(self.p*R2.q, self.q*R2.p)
    def __add__(self, R2):
        return R((self.p*R2.q + R2.p*self.q), self.q * R2.q)        
    def __sub__(self, R2):
        return R((self.p*R2.q - R2.p*self.q), self.q * R2.q)
    def __mul__(self, R2):
        return R(self.p*R2.p, self.q*R2.q)
    def __str__(self):
        return str(self.p) + '/' + str(self.q)
    def __repr__(self):
        return self.__str__()

def GetRationalNumbers():
    rawR1 = map(int, ir('Enter R1: ').split('/'))
    R1 = R(rawR1[0], rawR1[1])
    rawR2 = map(int, ir('Enter R2: ').split('/'))
    R2 = R(rawR2[0], rawR2[1])
    return [R1, R2]
    
def add():
    R1, R2 = GetRationalNumbers()
    print R1 + R2
def subtract():
    R1, R2 = GetRationalNumbers()
    print R1 - R2
def multiply():
    R1, R2 = GetRationalNumbers()
    print R1 * R2
def divide():
    R1, R2 = GetRationalNumbers()
    print R1 / R2

def menu():
    functs = {
        1: add,
        2: subtract,
        3: multiply,
        4: divide
    }
    print '1. Add\n2. Subtract\n3. Multiply\n4. Divide'
    functs[i("Do something: ")]()
    
menu()