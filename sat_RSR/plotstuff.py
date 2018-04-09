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

    tr = np.genfromtxt('trapazoid_r_RSR_estimate.dat')
    tg = np.genfromtxt('trapazoid_g_RSR_estimate.dat')
    tb = np.genfromtxt('trapazoid_b_RSR_estimate.dat')
    tp = np.genfromtxt('trapazoid_p_RSR_estimate.dat')

    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.scatter(r[:,0],r[:,9], s = 10, c = 'r', marker = 's', label = 'QE Red')
    ax1.scatter(r[:,0],r[:,10], s = 10, c = 'g', marker = 's', label = 'QE Green')
    ax1.scatter(r[:,0],r[:,11], s = 10, c = 'b', marker = 's', label = 'QE Blue')
    ax1.scatter(r[:,0],r[:,12], s = 10, c = '0.75', marker = 's', label = 'QE Pan')

    ax1.fill(tr[:,0], tr[:,2], c = 'r', alpha=0.3)
    ax1.fill(tg[:,0], tg[:,2], c = 'g', alpha=0.3)
    ax1.fill(tb[:,0], tb[:,2], c = 'b', alpha=0.3)
    ax1.fill(tp[:,0], tp[:,2], c = '0.75', alpha=0.3)

    ax1.plot(r[:,0],r[:,9], c = 'r')
    ax1.plot(r[:,0],r[:,10], c = 'g')
    ax1.plot(r[:,0],r[:,11], c = 'b')
    ax1.plot(r[:,0],r[:,12], c = '0.75')

    plt.xlabel('Wavelength (nm)')
    plt.ylabel('RSR')
    plt.legend(loc = 'upper right')
    plt.title('RSR vs Wavelength')

    plt.grid(True)
    plt.show()

def plot_sol(s,xmn,xmx, xlabel,ylabel,it):
    import matplotlib.pyplot as plt
    import numpy as np

    ited = np.genfromtxt(it)

    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.scatter(s[:,0],s[:,1], s = 10, c = 'y', marker = 's', label = ylabel)

    ax1.fill(ited[:,0],ited[:,2], 'y', alpha=0.3)
    ax1.plot(s[:,0],s[:,1], c = 'y')
#    ax1.plot(it[:,0],it[:,2], c = 'y')

    plt.xlim(xmin = xmn, xmax = xmx)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend(loc = 'upper right')
    plt.title(ylabel + ' vs ' + xlabel)

    plt.grid(True)
    plt.show()


def plot_solxrsr(r,xmn,xmx, xlabel,ylabel):
    import matplotlib.pyplot as plt
    import numpy as np

    tr = np.genfromtxt('trapazoid_r_combined_spectrum.dat')
    tg = np.genfromtxt('trapazoid_g_combined_spectrum.dat')
    tb = np.genfromtxt('trapazoid_b_combined_spectrum.dat')
    tp = np.genfromtxt('trapazoid_p_combined_spectrum.dat')

    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.scatter(r[:,0],r[:,1], s = 10, c = 'r', marker = 's', label = 'R')
    ax1.scatter(r[:,0],r[:,2], s = 10, c = 'g', marker = 's', label = 'G')
    ax1.scatter(r[:,0],r[:,3], s = 10, c = 'b', marker = 's', label = 'B')
    ax1.scatter(r[:,0],r[:,4], s = 10, c = '0.75', marker = 's', label = 'P')

    ax1.plot(r[:,0],r[:,1], c = 'r')
    ax1.plot(r[:,0],r[:,2], c = 'g')
    ax1.plot(r[:,0],r[:,3], c = 'b')
    ax1.plot(r[:,0],r[:,4], c = '0.75')

    ax1.fill(tr[:,0], tr[:,2], c = 'r', alpha=0.3)
    ax1.fill(tg[:,0], tg[:,2], c = 'g', alpha=0.3)
    ax1.fill(tb[:,0], tb[:,2], c = 'b', alpha=0.3)
    ax1.fill(tp[:,0], tp[:,2], c = '0.75', alpha=0.3)

    plt.xlim(xmin = xmn, xmax = xmx)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend(loc = 'upper right')
    plt.title(ylabel + ' vs ' + xlabel)

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

with open('Solar_Spectrum.dat','r') as f:
    Sol = np.genfromtxt(f)

with open('combined_spectrum.dat','r') as f:
    com = np.genfromtxt(f)


plot_sets(Tel,QE,Scout,RSR)
plot_rsrs(RSR)
plot_sol(Sol,190,2000,'Wavelength (nm)','Solar Irradiance (W/(nm*m^2))','trapazoid_Solar_Spectrum.dat')
plot_solxrsr(com,190,1000,'Wavelength (nm)','Irradiance * RSR (W/(nm*m^2))')
