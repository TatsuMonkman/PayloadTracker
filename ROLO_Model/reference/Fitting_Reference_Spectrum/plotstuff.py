import numpy as np
import matplotlib.pyplot as plt

def plot_cols(file2, xcol2, ycol2, file4, xcol4, ycol4, file5, xcol5, ycol5):

#    a = np.genfromtxt(file1)
    b = np.genfromtxt(file2)
#    c = np.genfromtxt(file3)
    d = np.genfromtxt(file4)
    e = np.genfromtxt(file5)

    fig = plt.figure()
    ax1 = fig.add_subplot(111)

#    ax1.scatter(a[:,0]*1000, a[:,1], s = 10, c = 'k', marker = 'o', label = 'Crystal')
#    ax1.plot(a[:,0], a[:,1], c = 'k')
    ax1.scatter(b[:,0], b[:,1], s = 10, c = 'b', marker = 'o', label = 'Soil')
    ax1.plot(b[:,0], b[:,1], c = 'b')
#    ax1.scatter(c[:,0]*1000, c[:,1], s = 10, c = 'b', marker = 'o', label = 'Breccia')
#    ax1.plot(c[:,0], c[:,1], c = 'b')
    ax1.scatter(d[:,0]*1000, d[:,1], s = 10, c = 'r', marker = 'o', label = 'Norite Powder')
    ax1.plot(d[:,0]*1000, d[:,1], c = 'r')
    ax1.scatter(e[:,0], e[:,1], s = 10, c = 'y', marker = 'o', label = ' ROLO Model')
    ax1.plot(e[:,0], e[:,1], c = 'y')

    ax1.scatter(b[:,0], (d[:,1]*0.05) + (b[:,1]*0.95), s = 10, c = 'm', marker = 'o', label = 'Mix')
    ax1.plot(b[:,0], (d[:,1]*0.05) + (b[:,1]*0.95), c = 'm')

    ax1.set_yscale('log')
    ax1.set_xlim([300,2500])
#    ax1.set_ylim([0,0.06])

    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Reflectance')
    plt.legend(loc = 'lower right')
    plt.title('Reflectance vs Wavelength for Apollo Samples')
    plt.grid(True)
    plt.show()


def plot_compare(file1, xcol1, ycol1, file2, xcol2, ycol2, file3, xcol3, ycol3):

    a = np.genfromtxt(file1)
    b = np.genfromtxt(file2)
    c = np.genfromtxt(file3)

    fig = plt.figure()
    ax1 = fig.add_subplot(111)

    ax1.scatter(a[:,0], a[:,1], s = 30, c = 'b', marker = 'x', label = 'My ROLO Implementation')
    ax1.plot(a[:,0], a[:,1], c = 'b')
    ax1.scatter(b[:,0], b[:,1], s = 20, c = 'r', marker = 'x', label = 'Stone\'s ROLO Implementation')
    ax1.plot(b[:,0], b[:,1], c = 'r')
    ax1.scatter(b[:,0], b[:,1]/b[:,2], s = 10, c = 'c', marker = 'x', label = 'Stone\'s unscaled ROLO results')
    ax1.plot(b[:,0], b[:,1]/b[:,2], c = 'c')

    ax1.set_yscale('log')
    ax1.set_xlim([300,2500])
#    ax1.set_ylim([0,0.06])

    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Reflectance')
    plt.legend(loc = 'lower right')
    plt.title('Comparison of Tatsu\'s and Stone\'s ROLO Implementations\n'
              + 'at lunar phase = 7deg, sat sublat/sublong = 0deg, solar sublong = 7deg')
    plt.grid(True)
    plt.show()

#plot_compare('VIIRS_2014_ROLO_Results.txt',0,1,'Aqua_2002_ROLO_Results.txt',0,1,
#             'Aqua_2002_ROLO_Results.txt',0,1)
plot_compare('ROLO_Results.txt',0,1,'Stone_ROLO_results.dat',0,1,
             'Aqua_2002_ROLO_Results.txt',0,1)
