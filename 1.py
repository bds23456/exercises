import math
from mpl_toolkits.mplot3d import axes3d
import numpy as np
import matplotlib.pyplot as plt

def main():
    print("Это программа выполнения упражнений по работе с библиотеками" +"\n" +
        "NumPy, MatPlotLib, mpl_toolkits.mplot3d. " + "\n" +
        "Вы можете выбрать реализацию одного из следующих упражнений:"
        "1. Расчет логарифма по основанию (1+х^2) от выражения " +
        "е^(1/(sin(x)+1) / (5/4 + 1/x^15)" + "\n" +
        "2. Построение графика функции x^2" + "\n" +
        "3. Построение графика диаграммы " + "\n" +
        "4. Построение 3D-графика функции z = x^2 - y^2 " + "\n" +
        "5. Построение графика функции y(x)=x^2-x-6 с нахождением корней" + "\n\n" +
        "Введите 0 для выхода"+ "\n")
    answer = int(input("Что выберем? "))
    menu(answer)
  
    #input()

def exr1 (x):
    #Exercises #1 - Calculate log(x) to base (1+x^2)
    a = 1 / (np.sin(x) + 1)
    b = 1 / np.power(x, 15, dtype = np.float64)
    c = 1 + np.power(x, 2, dtype = np.float64)
    y = np.log( np.exp(a) / (5/4 + (b))) / np.log(c)
    return y

def plot_1_x():
    #Example #1 - plotting x cubed 
    x = np.arange(-10, 10.01, 0.001)
    plt.figure(figsize=(6, 3))
    plt.plot(x, x**2)
    #plt.axis('equal')
    plt.xlabel(r'$x$')
    plt.ylabel(r'$f(x)$')
    plt.title(r'$f(x)=x^2$')
    plt.grid(True)
    plt.show()

def plot_2_diagram():
    #Example #2 - plotting circle diagram
    data = [31, 25, 18, 12, 14]
    plt.figure(num=1, figsize=(6, 6))
    plt.axes(aspect=1)
    plt.title('Plot 3', size=14)
    plt.pie(data, labels=('Group 1', 'Group 2', 'Group 3', 'Group 4', 'Group 5'))
    plt.show()

def plot_3_3Daxis():
    #Example #3 - plotting 3D function X^2-Y^2
    ax = axes3d.Axes3D(plt.figure())
    i = np.arange(-1, 1, 0.01)
    X, Y = np.meshgrid(i, i)
    Z = X**2 - Y**2
    ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
    plt.show()

def plot_4_x():
    #Exercises #2 - plotting x^2-x-6 and find solutions
    x = np.arange(-3.5, 4.51, 0.01)
    t = np.arange(-2, -1, 1)
    y = np.arange(3, 4, 1)
    plt.plot(x, x**2-x-6, t, t+2, 'ro', y, y-3, 'ro')
    plt.xlabel(r'$x$')
    plt.ylabel(r'$f(x)$')
    plt.title(r'$f(x)=x^2-x-6$')
    plt.grid(True)
    sp = plt.subplot(111)
    sp.spines['left'].set_position('zero')
    sp.spines['bottom'].set_position('zero')
    plt.show()

def menu(answer):
    if answer == 0:
        return
    elif answer == 1 :
        x = float(input("Введите х = "))
        print (exr1(x))
    elif answer == 2 :
        plot_1_x()
    elif answer == 3 :
        plot_2_diagram()
    elif answer == 4 :
        plot_3_3Daxis()
    elif answer == 5 :
        plot_4_x()   
    else :
        print("Невозможное значение ")

main()
