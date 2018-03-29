import numpy as np
import DiskE_Ref as lunar
import matplotlib.pyplot as plt




def plot2darray1( a, x, y, ymin, ymax):
    plt.plot()
    plt.semilogy( a[:,0], a[:,1])
#    plt.ylim( ymin, ymax)
    plt.title('Implemented ROLO Model ' + y + ' vs ' + x)
    plt.grid( True )
    plt.xlabel( x )
    plt.ylabel( y )
    plt.show()
    plt.close()

def plot2darray2( a, x, y, ymin, ymax):
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.semilogy(a[:,0], a[:,1], 'b')
    ax1.semilogy(-a[:,0], a[:,1], 'b')
    plt.title('Implemented ROLO Model ' + y + ' vs ' + x)
    ax1.grid( True )
    plt.xlabel( x )
    plt.ylabel( y )

    plt.show()

print('rrr')
for i in range(4,36):
    lunar.disk_e(0, 54.490, 6.39, -4.29, 138.143, i)
    #lunar.disk_(t, phase, oslon, olsat, sslat, wl)


model = []
print('hmmm')
for j in range(4,36):
    model.append(lunar.disk_e(0, 7, 0, 0, 7, j))
    #lunar.disk_(t, phase, oslon, olsat, sslat, wl)
m = np.asarray(model)
plot2darray1(m, 'Wavelength (nm)', 'Reflectance',0.06,.7)


model = []
for j in range(1,100):
    model.append([j] + [lunar.disk_e(0, j, 0, 0, 7, 15)[1]])
m = np.asarray(model)
print m
plot2darray2(m, 'Phase Anglee (deg)', 'Disk Reflectance', 0.09, 0.12)
