import math as mt
import numpy as np

INV_SQRT2 = 1./mt.sqrt(2.)

def generate_coeff(num):
    coeffs = []
    for i in range(n-1,-1,-1):
        coeffs.append([num // (2 ** i)])
        num -= (num // (2 ** i)) * (2 ** i)

    coeffs = coeffs[::-1]
    return coeffs

def mmul(a, b):
    # a (n, m), b(n) -> c(m)
    n = len(a)
    m = len(a[0])
    c = []
    for i in range(m):
        summ = 0
        for j in range(n):
            summ += a(i,j) * b(j)
        c.append(summ)
    return c

def product(q1, q2):
    return [q1.c0 * q2.c0, q1.c0 * q2.c1, q1.c1 * q2.c0, q1.c1 * q2.c1]

class Qubit:
    def __init__(self, theta, phi):
        self.theta = theta
        self.phi = phi
        self.c0 = np.cos(theta / 2.) + 0.j
        self.c1 = np.sin(theta / 2.) * np.exp(phi * 1.j)

    def XOR_gate(self, control):
        # Take control = 0 or 1
        # self.c0 += control.c0
        # self.c1 += control.c1
        # self.c0 = self.c0 % 2
        # self.c1 = self.c1 % 2
        xor = [
            [1,0,0,0],
            [0,1,0,0],
            [0,0,0,1],
            [0,0,1,0]
        ]
        tmp = product(self, control)
        tmp = mmul(xor, tmp)
        return tmp

    def NOT_gate(self):
        tmp = self.c0
        self.c0 = self.c1 
        self.c1 = tmp
    
    def coef_to_angle(self):
        self.theta = self.c1 * np.pi
    
    def angle_to_coef(self):
        self.c1 = self.theta / np.pi * np.exp(self.phi * 1.j)
        self.c0 = np.sqrt(1 - self.c1 ** 2)

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
        phase = 2. * mt.pi / (2**k) * control.c1
        self.c1 = self.c1 * np.exp(1.j * phase)

class Register:
    def __init__(self, coeffs):
        self.state = []
        for el in coeffs:
            self.state.append(Qubit(el[0], el[1]))
        self.tot_coef = 0


    def print(self):
        for i, el in enumerate(self.state):
            print("state ", i, ": ", el.c0, "|0> + (", el.c1, " |1>)")
    
    def add_qbit(self, coeff):
        self.state.append(Qubit(coeff[0], coeff[1]))

    def reverse(self):
        tmp = self.state[::-1]
        self.state = tmp
    