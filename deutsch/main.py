from qubit import Qubit
import math as mt

INV_SQRT2 = 1./mt.sqrt(2.)

initial = [Qubit(1,0),Qubit(INV_SQRT2, -INV_SQRT2)]

def summ(n1, n2):
    return (n1 + n2) % 2

def operator_f(control):
    func = [1,0]
    control.c0 *= (-1)**func[0]
    control.c1 *= (-1)**func[1]
    return control


initial[0].H_gate()
print(initial[0].c0, initial[0].c1)
initial[0] = operator_f(initial[0])
print(initial[0].c0, initial[0].c1)
initial[0].H_gate()

print(initial[0].c0, initial[0].c1)