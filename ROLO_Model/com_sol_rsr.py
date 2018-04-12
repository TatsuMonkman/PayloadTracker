#This script multiplies the y-values of two trapazoidal files, returning
#a file of x, y values that matches the resolution of file2.
#Trapazoidal data sets are organized as follows:
#startwidth, endwidth, startheight, endheight, slope, y-intercept, area

def combine_spectra(file1, file2, name):
    import numpy as np

    with open(file1, 'r') as f:
        f2 = np.genfromtxt(f)
    with open(file2, 'r') as f:
        f1 = np.genfromtxt(f)
    prod = []
    for i in range(len(f1)):
        for j in range(len(f2)-1):
            if f1[i][0] == f2[j][0]:
                y = f1[i][2]*f2[j][2]
                if y < 0:
                    prod.append([f1[i][0],0.00])
                else:
                    prod.append([f1[i][0],y])
                pass
            elif f2[j][0] < f1[i][0] < f2[j+1][0]:
                y = (f2[j][4]*f1[i][0] + f2[j][5])*f1[i][2]
                if y < 0:
                    prod.append([f1[i][0],0.00])
                else:
                    prod.append([f1[i][0],y])
                pass
    with open(name + 'combined_spectrum.dat','w') as f:
        f.write('#wl\tirradiance*RSR\n')
        np.savetxt(f,prod)
