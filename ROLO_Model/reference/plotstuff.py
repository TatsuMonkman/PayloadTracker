import numpy as np
import matplotlib.pyplot as plt

def plot_cols(file1, xcol1, ycol1, file2, xcol2, ycol2, file3, xcol3, ycol3,
              file4, xcol4, ycol4):

    a = np.genfromtxt(file1)
    b = np.genfromtxt(file2)
    c = np.genfromtxt(file3)
    d = np.genfromtxt(file4)

    fig = plt.figure()
    ax1 = fig.add_subplot(111)

#    ax1.scatter(a[:,0]*1000, a[:,1], s = 10, c = 'k', marker = 'o', label = 'Crystal')
#    ax1.plot(a[:,0], a[:,1], c = 'k')
    ax1.scatter(b[:,0], b[:,1], s = 10, c = 'b', marker = 'o', label = 'Soil')
    ax1.plot(b[:,0], b[:,1], c = 'b')
#    ax1.scatter(c[:,0]*1000, c[:,1], s = 10, c = 'b', marker = 'o', label = 'Breccia')
#    ax1.plot(c[:,0], c[:,1], c = 'b')
    ax1.scatter(d[:,0]*1000, d[:,1], s = 10, c = 'r', marker = 'o', label = 'Norite Powder')
    ax1.plot(d[:,0], d[:,1], c = 'r')

    ax1.scatter(b[:,0], (d[:,1]*0.05) + (b[:,1]*0.95), s = 10, c = 'm', marker = 'o', label = 'Mix')
    ax1.plot(b[:,0], (d[:,1]*0.05) + (b[:,1]*0.95), c = 'm')

    ax1.set_yscale('log')
    ax1.set_xlim([350,2500])

    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Reflectance')
    plt.legend(loc = 'lower right')
    plt.title('Reflectance vs Wavelength for Apollo Samples')
    plt.grid(True)
    plt.show()


plot_cols('67455_ls-CMP-25.dat', 0, 1, '62231_avg_scaled_std_text.txt',
           0, 1, '67455_ls-CMP-171.dat', 0, 1,'67455_ls-CMP-10.dat', 0, 1)
