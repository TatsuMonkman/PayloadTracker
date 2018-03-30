import numpy as np
from DiskE_Ref import lunar
from find_traps import make_traps
from find_offset import offset
from integrated import integrate

#run ROLO over all wavelengths for observation date, selenographic coordinates
model = []
for j in range(4,36):
    model.append(lunar(0, 7, 0, 0, 7, j)) #date(JD seconds), phase(deg), observer slon (deg), observer slat (deg), sun slat (deg)
m3 = np.asarray(model)
with open('ROLO_Results.txt','w') as f:
    f.write('#Disk Reflectance Results\n#Wavelength\t\tReflectance\n')
    np.savetxt(f, m3)

#Trapazoidal integration of reference data (only need to do once for each data set)
#Naming reference data "reference data", needs to have wavelengths and reflectance in the first and second columns, respectively

ref_file = 'referencedata.txt'
ref = np.loadtxt( ref_file ) #load reference text
with open( 'trapazoid_' + ref_file, 'w') as f:
    f.write('#trapazoidal\n# startwidth \t\tendwidth \t\tstartheight \t\tendheight \t\tslope \t\t\ty-intercept \t\t\tarea\n')
    np.savetxt(f, make_traps(ref))


#Find ROLO model offset from reference data
traps = np.loadtxt('trapazoid_' + ref_file)
Rolo  = np.loadtxt('ROLO_Results.txt')

dy = []
avg = 0

for i in range(len(Rolo)):

    dy.append(offset( Rolo[i], traps))
    avg += offset( Rolo[i], traps)

os = avg / len(Rolo)

print('All offsets: ', dy, 'Average offset: ', os) #all offsets

integrate('referencedata.txt', os)
