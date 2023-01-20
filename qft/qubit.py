import math as mt
import numpy as np

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
    
    def R_gate(self, control, k):
        self.c1 = self.c1 * np.exp(2*mt.pi*1j/(2**k)*control.c1)

class Register:
    def __init__(self, coeffs):
        self.state = []
        for el in coeffs:
            self.state.append(Qubit(el[0], el[1]))
    
    def print(self):
        for i, el in enumerate(self.state):
            print("state ", i, ": ", el.c0, "|0> + (", el.c1, " |1>)")
    
    def add_qbit(self, coeff):
        self.state.append(Qubit(coeff[0], coeff[1]))
    
    