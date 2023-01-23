import numpy as np
from library import INV_SQRT2, generate_coeff

class Qubit:
    def __init__(self, theta, phi=0.):
        self.theta = theta
        self.phi = phi
        self.c0 = np.cos(theta / 2.) + 0.j
        self.c1 = np.sin(theta / 2.) * np.exp(phi * 1.j)

    def coef_to_angles(self):
        self.theta = 2. * np.arccos(self.c0)
        self.phi = np.log(self.c1 / np.sin(self.theta / 2.)) / 1.j

    def angles_to_coef(self):
        self.c0 = np.cos(self.theta / 2.) + 0.j
        self.c1 = np.sin(self.theta / 2.) * np.exp(self.phi * 1.j)

    def H_gate(self):
        tmpc0 = (self.c0 + self.c1)*INV_SQRT2
        tmpc1 = (self.c0 - self.c1)*INV_SQRT2
        self.c0 = tmpc0
        self.c1 = tmpc1
        self.coef_to_angles()

    def R_gate(self, k, control):
        phase = 2. * np.pi / (2**k) * control.c1
        self.phi -= phase
        self.angles_to_coef()

    def print(self):
        print(self.c0, "|0> + ", self.c1, " |1>)")

class Register:
    def __init__(self, qubits):
        self.coeffs = []
        self.qubits = qubits
        for i in range(2 ** len(qubits)):
            coeff = 1. + 0j
            indexes = generate_coeff(i, len(qubits))
            for j in range(len(qubits)):
                if indexes[j] == 0:
                    coeff *= qubits[j].c0
                else:
                    coeff *= qubits[j].c1
            self.coeffs.append(coeff)
        
    def compute_coeffs(self):
        self.coeffs = []
        for i in range(2 ** len(self.qubits)):
            coeff = 1. + 0j
            indexes = generate_coeff(i, len(self.qubits))
            indexes = indexes[::-1]
            for j in range(len(self.qubits)):
                if indexes[j] == 0:
                    coeff *= self.qubits[j].c0
                else:
                    coeff *= self.qubits[j].c1
            self.coeffs.append(coeff)

    # def modify_qubit(self, index, qubit):
    def modify_qubit(self, index, qubit):
        self.qubits[index] = qubit
        self.compute_coeffs()

    def invert_qubits(self):
        qubits = self.qubits[::-1]
        self.qubits = qubits

    def print(self):
        print(self.coeffs)
    