import numpy as np
from DiskE_Ref import lunar
from find_traps import make_traps
from find_offset import offset
from integrated import integrate

#Run ROLO over all wavelengths for observation date, selenographic coordinates.
#Values in lunar are assigned as follows with long and lat
#in selenographic coordinates:
#lunar(date(JD seconds), phase(deg), observer slon (deg),
#observer slat (deg), sun slat (deg))

model = []
for j in range(4,36):
    model.append(lunar(0, 7, 0, 0, 7, j))

m3 = np.asarray(model)

with open('ROLO_Results.txt','w') as f:
    f.write('#Disk Reflectance Results\n#Wavelength\t\tReflectance\n')
    np.savetxt(f, m3)

#The following block performs trapazoidal integration of reference data.
#Naming reference data "reference data",
#needs to have wavelengths and reflectance
#in the first and second columns, respectively

ref_file = 'referencedata.txt'

#load reference text
ref = np.loadtxt( ref_file )
with open('trapazoid_' + ref_file, 'w') as f:
    f.write('#trapazoidal\n# startwidth \t\tendwidth \t\tstartheight
            + '\t\tendheight \t\tslope \t\t\ty-intercept \t\t\tarea\n')
    np.savetxt(f, make_traps(ref))


#Find the offset of the ROLO model values from the trapazoidally
#integrated reference data
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
