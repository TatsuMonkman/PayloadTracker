#This script multiplies the RSR by the Solar spectral irradiance for each
#corresponding wavelenth band.

#Trapazoidal data sets are organized as follows:
#startwidth, endwidth, startheight, endheight, slope, y-intercept, area
import numpy as np

with open('trapazoid_Solar_Spectrum.dat', 'r') as f:
    sol = np.genfromtxt(f)

with open('RSR_estimate.dat', 'r') as f:
    rsr = np.genfromtxt(f)

prod = []

for i in range(len(rsr)):
    for j in range(len(sol)):
        if sol[j][0] == rsr[i][0]:
            y = sol[j][4]*rsr[i][0] + sol[j][5]
            prod.append([rsr[i][0],rsr[i][9]*y,rsr[i][10]*y,
                        rsr[i][11]*y,rsr[i][12]*y])
            pass
        elif sol[j][0] < rsr[i][0] < sol[j+1][0]:
            y = sol[j][4]*rsr[i][0] + sol[j][5]
            prod.append([rsr[i][0],rsr[i][9]*y,rsr[i][10]*y,
                        rsr[i][11]*y,rsr[i][12]*y])
            pass

#print sol[1]
#print prod[1]
#print prod[2]
#print prod[3]

with open('combined_spectrum.dat','w') as f:
    f.write('#wl\tirradiance*RSR\n')
    np.savetxt(f,prod)
