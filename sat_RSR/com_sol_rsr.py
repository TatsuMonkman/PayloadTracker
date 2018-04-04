import numpy as np

with open('trapazoid_Solar_Spectrum.dat', 'r') as f:
    sol = np.genfromtxt(f)

with open('RSR_spec.dat', 'r') as f:
    rsr = np.genfromtxt(f)

print sol
print rsr

prod = []


for i in range(len(rsr)):
    for j in range(len(sol)):
        if sol[j][0] <= rsr[i][0] <= sol[j+1][0]:
            y = sol[j][4]*rsr[i][0] + sol[j][5]
            prod.append([rsr[i][0],rsr[i][1],sol[j][0],sol[j][2],
                        sol[j][4],y,rsr[i][1]*y])

print np.asarray(prod)
#print sol[1]
#print prod[1]
#print prod[2]
#print prod[3]

with open('combined_spectrum.dat','w') as f:
    f.write('#wl\tirradiance*RSR\n')
    for i in range(len(prod)):
        f.write(str(prod[i][0]) + '\t' + str(prod[i][6]) + '\n')
