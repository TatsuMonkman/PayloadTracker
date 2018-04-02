from __future__ import print_function, division
from datetime import datetime, timedelta
import ephem
import astropy
from astropy import units as u
from astropy.coordinates import SkyCoord

#Define date and time delta values
utc_t = datetime.utcnow() #Time at start of routine
test_t = datetime.strptime('2005-03-22 02:27:59.652049', '%Y-%m-%d %H:%M:%S.%f') #return a datetime object, corresponding to date_string parsed according to format
d_t = timedelta(days = .2)

#Define TLE File
line1 = 'NOAA 14' #
line2 = '1 23455U 94089A   04366.74530554  .00000332  00000-0  20061-3 0  4198' #See TLE file notes
line3 = '2 23455  99.1151  46.1451 0010115 112.6215 247.6058 14.13524725515843'

NOAA14 = ephem.readtle(line1, line2, line3) #Object read into PyEphem
NOAA14.compute(test_t) #Compute NOAA14 position

m = ephem.Moon(test_t)
m.compute(test_t)
Mc = SkyCoord(str(m.ra)+' '+str(m.dec), unit=(u.hourangle, u.deg))

mra = []
mdeg = []

nra = []
ndeg = []

for i in range(int(29/.2)): #Moon iteration, range is number of datapoints
    dt1 = test_t + i*d_t
    m.compute(dt1)
    Mc = SkyCoord(str(m.ra) + ' ' + str(m.dec), unit = (u.hourangle, u.deg))
    print('Moon\t%s\t%s' % (Mc.ra.deg, Mc.dec.deg))
    mra.append(Mc.ra.deg)
    mdeg.append(Mc.dec.deg)


for i in range(int(29/.2)): #Satellite iteration
    dt1 = test_t + i*d_t
    NOAA14.compute(dt1)
    Nc = SkyCoord(str(NOAA14.ra) + ' ' + str(NOAA14.dec), unit = (u.hourangle, u.deg))
    print('NOAA14\t%s\t\t%s' % (Nc.ra.deg, Nc.dec.deg))
    ecl = ephem.Ecliptic(NOAA14)
    print('lon %s lat %s' % (ecl.lon, ecl.lat))
    nra.append(Nc.ra.deg)
    ndeg.append(Nc.dec.deg)

#Experimental Moon Phase test using PyAstronomy

import datetime
from PyAstronomy import pyasl
import numpy as np

#Convert calendar date to JD
#using the datetime package
jd = test_t
jd = pyasl.jdcnv(jd)
jd = np.arange(jd, jd+29,.2)
mp = pyasl.moonphase(jd)
phase = []

print("%15s %3s" % ("JD", "Phase")) #taken from http://www.hs.uni-hamburg.de/DE/Ins/Per/Czesla/PyA/PyA/pyaslDoc/aslDoc/moon.html
for i in range(jd.size):
    print("%15.4f  %3d%%" % (jd[i], mp[i]*100.))
    phase.append(mp[i]*100.)

import matplotlib.pyplot as plt

nx = nra
ny = ndeg
mx = mra
my = mdeg
px = phase
n = len(px)

plt.figure()
plt.plot(nx,ny,'ro')
plt.plot(mx,my,'bo')
plt.show()
plt.close()

plt.figure()
plt.plot(mx[i],my[i])
colors = plt.cm.viridis(np.linspace(0,1,n))

for i in range(len(mx)):
    plt.plot(mx[i],my[i], color=colors[i])

plt.show()
plt.close()

ecl = ephem.Ecliptic(NOAA14)
print('%s %s' % (ecl.lon, ecl.lat))
