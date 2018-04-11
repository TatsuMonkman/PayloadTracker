#This script tries its best to fit two data sets together using the
#A'=A*(a+b*l) scaling factor.
#For now I am going to try iterating between a and b values until I get the
#smallest final offset. I am going to try to keep all of my data as numpy
#arrays.
import numpy as np
import matplotlib.pyplot as plt

def initial_offset(m, r):
    #'m' is the calculated ROLO model reflectance values.
    #'r' is the trapazoidally integrated reference file
    #Find the offset between the reference spectrum values and the
    #ROLO model output.
    off = []
    for i in range(len(m)):
        for j in range(len(r)):
            if r[j][0] == m[i][0]:
                off.append([r[j][0],m[i][1],r[j][2],r[j][2]-m[i][1]])
            elif r[j][0] < m[i][0] < r[j+1][0]:
                M = r[j][4]
                b = r[j][5]
                x = m[i][0]
                y = M*x + b
                off.append([r[j][0],m[i][1],y,y-m[i][1]])
    return np.asarray(off)

def add_arbitrary_offset(o, a, b):
    #Add a user-specified offset to see what you get..
    norm = []
    for i in range(len(o)):
        scaled = (a + b*o[i][0])*o[i][2]
        norm.append([o[i][0], o[i][1], o[i][2], scaled])
    return np.asarray(norm)

def add_scalar_offset(o):
    #Add the average offset (scalar) to all reference values
    avgo = np.mean(o, axis=0)[3]
    print avgo
    norm = []
    for i in range(len(o)):
        norm.append([o[i][0], o[i][1], o[i][2] - avgo, o[i][3] - avgo])
    return np.asarray(norm)

def mult_scalar_offset(o):
    #Add a wavelength dependant offset s=b*lam
    print o
    avgo = o[:,3]/o[:,0]
    print avgo
    norm = []
    for i in range(len(o)):
        norm.append([o[i][0], o[i][1], o[i][2] - avgo[i], o[i][3] -avgo[i]])
    return np.asarray(norm)

ref = np.genfromtxt('trapazoid_mixed_spectrum.txt')
mod = np.genfromtxt('ROLO_Results.txt')

ioff = initial_offset(mod, ref)

print ioff
aff = add_scalar_offset(ioff)
aaff = mult_scalar_offset(aff)

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.scatter(ioff[:,0],ioff[:,1], s = 10, c = 'b', marker = 'o', label = 'Model')
ax1.plot(ioff[:,0],ioff[:,1], c = 'b')
ax1.scatter(ioff[:,0],ioff[:,2], s = 10, c = 'r', marker = 'o', label = 'Reference')
ax1.plot(ioff[:,0],ioff[:,2], c = 'r')
ax1.scatter(aff[:,0],aff[:,2], s = 10, c = 'm', marker = 'o', label = 'Linearly Shifted')
ax1.plot(aff[:,0],aff[:,2], c = 'm')

aroff = add_arbitrary_offset(ioff, 0.6, 0.00005)
print aroff

raroff = add_arbitrary_offset(ref, 0.6, 0.00005)
print raroff

ax1.scatter(raroff[:,0],raroff[:,3], s = 10, c = '0.75', marker = 'o', label = 'Manual Input Full Spec')
ax1.plot(raroff[:,0],raroff[:,3], c = '0.75')

ax1.scatter(aroff[:,0],aroff[:,3], s = 10, c = 'c', marker = 'o', label = 'Manual Input Convolution')
ax1.plot(aroff[:,0],aroff[:,3], c = 'c')

plt.xlabel('Wavelength (nm)')
plt.ylabel('Reflectance')

ax1.set_yscale('log')
plt.legend(loc = 'lower right')
plt.grid(True)
plt.show()

head = ('Dr. Stone needs to work on his methods sections\n#Wavelength,'
         + '\tModel,\tReference,\tCorrected')
np.savetxt('Stone_scaled.dat',raroff, fmt='%5f', header=head)
