def plot_sets(a,b,c,d):
    import matplotlib.pyplot as plt
    import numpy as np

    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.scatter(a[0,:],a[15,:], s = 10, c = 'k', marker = 'o', label = 'Telescope Throughput')
    ax1.scatter(b[:,0],b[:,5], s = 10, c = 'r', marker = 'o', label = 'QE Red')
    ax1.scatter(b[:,0],b[:,6], s = 10, c = 'g', marker = 'o', label = 'QE Green')
    ax1.scatter(b[:,0],b[:,7], s = 10, c = 'b', marker = 'o', label = 'QE Blue')
    ax1.scatter(b[:,0],b[:,8], s = 10, c = '0.85', marker = 'o', label = 'QE Pan')
    ax1.scatter(c[:,0],c[:,1]/100, s = 10, c = '0.75', marker = 's', label = 'Scout Filter')

    ax1.plot(a[0,:],a[15,:], c = 'k')
    ax1.plot(b[:,0],b[:,5], c = 'r')
    ax1.plot(b[:,0],b[:,6], c = 'g')
    ax1.plot(b[:,0],b[:,7], c = 'b')
    ax1.plot(b[:,0],b[:,8], c = '.85')
    ax1.plot(c[:,0],c[:,1]/100, c = '0.75')

    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Throughput')
    plt.legend(loc = 'upper left')
    plt.title('Throughput vs Wavelength')

    plt.grid(True)
    plt.show()

def plot_rsrs(r):
    import matplotlib.pyplot as plt
    import numpy as np

    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.scatter(r[:,0],r[:,11], s = 10, c = 'r', marker = 's', label = 'QE Red')
    ax1.scatter(r[:,0],r[:,12], s = 10, c = 'g', marker = 's', label = 'QE Green')
    ax1.scatter(r[:,0],r[:,13], s = 10, c = 'b', marker = 's', label = 'QE Blue')
    ax1.scatter(r[:,0],r[:,14], s = 10, c = 'k', marker = 's', label = 'QE Pan')

    ax1.plot(r[:,0],r[:,11], c = 'r')
    ax1.plot(r[:,0],r[:,12], c = 'g')
    ax1.plot(r[:,0],r[:,13], c = 'b')
    ax1.plot(r[:,0],r[:,14], c = 'k')

    plt.xlabel('Wavelength (nm)')
    plt.ylabel('RSR')
    plt.legend(loc = 'upper right')
    plt.title('RSR vs Wavelength')

    plt.grid(True)
    plt.show()

#plot_2sets(obs,nobs)

import numpy as np

with open('KE_Throughput_estimate.dat','r') as f:
    Tel = np.genfromtxt(f)

with open('KE_QE_SparseCFA.dat','r') as f:
    QE = np.genfromtxt(f)

with open('Scout_Filter.dat','r') as f:
    Scout = np.genfromtxt(f)

with open('RSR_estimate.dat','r') as f:
    RSR = np.genfromtxt(f)


print RSR
print RSR[0]

plot_sets(Tel,QE,Scout,RSR)
plot_rsrs(RSR)
