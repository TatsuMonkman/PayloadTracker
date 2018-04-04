
#Run ROLO over all wavelengths for observation date, selenographic coordinates.
#Values in lunar are assigned as follows with long and lat
#in selenographic coordinates:
#lunar(date(JD seconds), phase(deg), observer slon (deg),
#observer slat (deg), sun slat (deg))

import numpy as np
import subprocess
from DiskE_Ref import lunar
from integration import add_offset, make_traps, offset, trap_integrate, trap_file


#This script runs ROLO over all ROLO wavelengths using lunar
#Saves results to ROLO_Results.txt
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
#
trap_file(ref_file, 0, 1)
trap_file('Solar_Spectrum.dat', 0, 1)
trap_file('RSR_estimate.dat', 0, 11)
subprocess.call('mv trapazoid_RSR_estimate.dat trapazoid_QER_RSR_estimate.dat', shell=True)
trap_file('RSR_estimate.dat', 0, 12)
subprocess.call('mv trapazoid_RSR_estimate.dat trapazoid_QEG_RSR_estimate.dat', shell=True)
trap_file('RSR_estimate.dat', 0, 13)
subprocess.call('mv trapazoid_RSR_estimate.dat trapazoid_QEB_RSR_estimate.dat', shell=True)
trap_file('RSR_estimate.dat', 0, 14)
subprocess.call('mv trapazoid_RSR_estimate.dat trapazoid_QEP_RSR_estimate.dat', shell=True)


trap_integrate('trapazoid_Solar_Spectrum.dat', 450, 500)
trap_integrate('trapazoid_' + ref_file, 450, 500)
trap_integrate('trapazoid_QER_RSR_estimate.dat', 450, 500)
trap_integrate('trapazoid_QEG_RSR_estimate.dat', 450, 500)
trap_integrate('trapazoid_QEB_RSR_estimate.dat', 450, 500)
trap_integrate('trapazoid_QEP_RSR_estimate.dat', 450, 500)

#Find the offset of the ROLO model values from the trapazoidally
#integrated reference data.
traps = np.loadtxt('trapazoid_' + ref_file)
Rolo  = np.loadtxt('ROLO_Results.txt')

dy = []
avg = 0

for i in range(len(Rolo)):
    dy.append(offset( Rolo[i], traps))
    avg += offset(Rolo[i], traps)

offset = avg / len(Rolo)

print('All offsets: ', dy, 'Average offset: ', offset) #all offsets

add_offset('referencedata.txt', offset)
