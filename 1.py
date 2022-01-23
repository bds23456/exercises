import math
import numpy as np
import matplotlib.pyplot as plt

def main():
    x = 1, 10, 1000
    print (exr1(x))
    input() 

def exr1 (x):
    #Exercises #1 - Calculate log(x) to base (1+x^2)
    a = 1 / (np.sin(x) + 1)
    b = 1 / np.power(x, 15, dtype = np.float64)
    c = 1 + np.power(x, 2, dtype = np.float64)
    y = np.log( np.exp(a) / (5/4 + (b))) / np.log(c)
    return y


main()
