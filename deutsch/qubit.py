import math as mt

INV_SQRT2 = 1./mt.sqrt(2.)

class Qubit:
    def __init__(self, c0, c1):
        self.c0 = c0
        self.c1 = c1

    def XOR_gate(self, control):
        # Take control = 0 or 1
        self.c0 += control.c0
        self.c1 += control.c1
        self.c0 = self.c0 % 2
        self.c1 = self.c1 % 2

    def NOT_gate(self):
        tmp = self.c0
        self.c0 = self.c1 
        self.c1 = tmp 


    def H_gate(self):
        tmpc0 = (self.c0 + self.c1)*INV_SQRT2
        tmpc1 = (self.c0 - self.c1)*INV_SQRT2
        self.c0 = tmpc0
        self.c1 = tmpc1
        
    def AND_gate(self, control):
        if control.c1 == 1 and self.c1 == 1:
            return
        else:
            self.c0 = 1.
            self.c1 = 0.


    