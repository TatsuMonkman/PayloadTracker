import numpy as np

def plot_sets(a,b,c,d,e):
    import matplotlib.pyplot as plt
    import numpy as np

    fig = plt.figure()
    ax1 = fig.add_subplot(111)
#    ax1.scatter(a[:,0],a[:,2], s = 10, c = 'r', marker = 'o', label = 'r combined')
#    ax1.scatter(b[:,0],b[:,2], s = 10, c = 'g', marker = 'o', label = 'g combined')
#    ax1.scatter(c[:,0],c[:,2], s = 10, c = 'b', marker = 'o', label = 'b combined')
#    ax1.scatter(d[:,0],d[:,2], s = 10, c = '0.75', marker = 'o', label = 'p combined')
    ax1.scatter(e[:,0],e[:,2], s = 10, c = 'y', marker = 'o', label = 'ROLO Model')

#    ax1.plot(a[:,0],a[:,2], c = 'r')
#    ax1.plot(b[:,0],b[:,2], c = 'g')
#    ax1.plot(c[:,0],c[:,2], c = 'b')
#    ax1.plot(d[:,0],d[:,2], c = '0.75')
    ax1.plot(e[:,0],e[:,2], c = 'y')
    ax1.set_yscale('log')

    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Reflectance')
    plt.legend(loc = 'upper left')
    plt.title('Reflectance vs Wavelength')
    plt.xlim(xmin = 300, xmax = 1050)
    plt.grid(True)
    plt.show()



#with open('trapazoid_r_AkSolRSR_combined_spectrum.dat','r') as f:
#    r_trap = np.genfromtxt(f)

#with open('trapazoid_b_AkSolRSR_combined_spectrum.dat','r') as f:
#    b_trap = np.genfromtxt(f)

#with open('trapazoid_g_AkSolRSR_combined_spectrum.dat','r') as f:
#    g_trap = np.genfromtxt(f)

#with open('trapazoid_p_AkSolRSR_combined_spectrum.dat','r') as f:
#    p_trap = np.genfromtxt(f)

#with open('trapazoid_ROLO_Results.dat', 'r') as f:
#    ROLO_trap = np.genfromtxt(f)

#plot_sets(r_trap,b_trap,g_trap,p_trap,ROLO_trap)
