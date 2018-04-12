import numpy as np
import matplotlib.pyplot as plt

def plot_compare(file1, xcol1, ycol1):

    a = np.genfromtxt(file1)

    fig = plt.figure()
    ax1 = fig.add_subplot(111)

    ax1.scatter(a[:,0], a[:,1], s = 30, c = 'b', marker = 'x', label = 'My ROLO Implementation')
    ax1.plot(a[:,0], a[:,1], c = 'b')

    ax1.set_yscale('log')
    ax1.set_xlim([300,2500])

    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Reflectance')
    plt.legend(loc = 'lower right')
    plt.title('My ROLO Model Implementation')
    plt.grid(True)
    plt.show()
