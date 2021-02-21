import numpy as np

#Bisseção
def bissecao(f, a, b, xtol=1e-8, ytol=1e-8):
    niters=0
    while abs(a-b)>xtol and abs(f((a+b)/2))>ytol:
        m = (a+b)/2
        if f(m)*f(a)<0:
            b = m
        else:
            a = m
        niters+=1
    m = (a+b)/2
    return m, niters