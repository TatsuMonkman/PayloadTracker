
#Run ROLO over all wavelengths for observation date, selenographic coordinates.
#Values in lunar are assigned as follows with long and lat
#in selenographic coordinates:
#lunar(date(JD seconds), phase(deg), observer slon (deg),
#observer slat (deg), sun slat (deg))

import numpy as np
from DiskE_Ref import lunar
from integration import integrate, make_traps, offset, trap_integrate


#First, this script runs ROLO over all ROLO wavelengths
model = []
for j in range(4,36):
    model.append(lunar(0, 7, 0, 0, 7, j))
m3 = np.asarray(model)
with open('ROLO_Results.txt','w') as f:
    f.write('#Disk Reflectance Results\n#Wavelength\t\tReflectance\n')
    np.savetxt(f, m3)


#The following block performs trapazoidal integration of reference data (the
#reference lunar spectrum that we are fitting to our ROLO results).
#I'm naming reference data "reference data" for now, but this needs to be
#more precise. The reference data needs to have wavelengths and reflectance
#in the first and second columns, respectively.

#Begin by loading and integrating the reference data
ref_file = 'referencedata.txt'
trap_integrate(ref_file)


#Find the offset of the ROLO model values from the trapazoidally
#integrated reference data.
traps = np.loadtxt('trapazoid_' + ref_file)
Rolo  = np.loadtxt('ROLO_Results.txt')

dy = []
avg = 0

for i in range(len(Rolo)):
    dy.append(offset( Rolo[i], traps))
    avg += offset(Rolo[i], traps)

os = avg / len(Rolo)

print('All offsets: ', dy, 'Average offset: ', os) #all offsets

integrate('referencedata.txt', os)
