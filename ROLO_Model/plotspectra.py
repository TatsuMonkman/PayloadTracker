import numpy as np

def plot_sets(a,b,c,d):
    import matplotlib.pyplot as plt
    import numpy as np

    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.scatter(a[:,0],a[:,6], s = 10, c = 'r', marker = 'o', label = 'Reference Lunar Albedo')
    ax1.scatter(b[:,0],b[:,6], s = 10, c = 'g', marker = 'o', label = 'Solar Irradiance')
    ax1.scatter(c[:,0],c[:,6], s = 10, c = 'b', marker = 'o', label = 'RSR')
    ax1.scatter(d[:,0],d[:,6], s = 10, c = 'm', marker = 'o', label = 'Solar/RSR Combined')

    ax1.plot(a[:,0],a[:,6], c = 'r')
    ax1.plot(b[:,0],b[:,6], c = 'g')
    ax1.plot(c[:,0],c[:,6], c = 'b')
    ax1.plot(d[:,0],d[:,6], c = 'm')

    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Quantities')
    plt.legend(loc = 'upper left')
    plt.title('Quantities vs Wavelength')
    plt.xlim(xmin = 300, xmax = 1050)
    plt.ylim(ymin = 0, ymax = 1000)
    plt.grid(True)
    plt.show()



with open('trapazoid_referencedata.txt','r') as f:
    ref = np.genfromtxt(f)

with open('trapazoid_Solar_Spectrum.dat','r') as f:
    sol = np.genfromtxt(f)

with open('trapazoid_RSR_estimate.dat','r') as f:
    rsr = np.genfromtxt(f)

with open('trapazoid_Combined_Spectrum.dat','r') as f:
    com = np.genfromtxt(f)
    
print sol[0]
print ref[0]
print rsr[0]
print com[0]
plot_sets(ref,sol,rsr,com)
