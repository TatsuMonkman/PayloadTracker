#Run ROLO over all wavelengths for observation date, selenographic coordinates.
#Values in lunar are assigned as follows with long and lat
#in selenographic coordinates:
import numpy as np
import subprocess
from DiskE_Ref import lunar
from integration import make_traps, trap_integrate, trap_file
from plotstuff import plot_cols

#This script runs ROLO over all ROLO wavelengths using lunar
#Saves results to ROLO_Results.txt
#lunar(date(JD seconds), phase(deg), observer sublongitude (deg),
#observer sublatitude (deg), sun sublongitude(deg), ROLO wavelength band)
model = []
for j in range(4,36):
    model.append(lunar(0, 7, 0, 0, 7, j))
m3 = np.asarray(model)
with open('ROLO_Results.txt','w') as f:
    f.write('#Disk Reflectance Results\n#Wavelength\t\tReflectance\n')
    np.savetxt(f, m3, fmt='%4f')

#The following block performs trapazoidal integration of reference data (the
#reference lunar spectrum that we are fitting to our ROLO results).
#I'm naming reference data "reference data" for now, but this needs to be
#more precise. The reference data needs to have wavelengths and reflectance
#in the first and second columns, respectively.

#Begin by loading and integrating the reference data
ref_file = 'ROLO_Results.txt'
trap_file(ref_file, 'trapazoid_' + ref_file, 0, 1)
trap_integrate('trapazoid_' + ref_file, 350, 800)
