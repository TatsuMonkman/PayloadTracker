#This script returns the integrated solar spectral irradiance for usage
#in the ROLO model. This script uses the Wherli spectrum to derive Irradiance
#from the ROLO calculated disk reflectance.

import numpy as np
import csv

wl = []
irr = []

with open('wl_PGIRO_ROLO_solspectr.dat','r') as f:
    reader = csv.reader(f)
    wl = list(reader)

with open('irr_PGIRO_ROLO_solspectr.dat','r') as f:
    reader = csv.reader(f)
    irr = list(reader)

wll = []
irrl = []

for i in range(len(wl)):
    wll += wl[i]
    irrl += irr[i]

print wll
print float(irrl[4])


a = np.asarray([wll,irrl])

with open('Clean_GIRO_Solspec.dat', 'w') as f:
    f.write('#wl(nm)\tirr(W/(nm*m^2))')
    for i in range(len(wll)):
        f.write(wll[i]+'\t'+irrl[i]+'\n')
