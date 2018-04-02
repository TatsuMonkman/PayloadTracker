from skyfield.sgp4lib import EarthSatellite
from skyfield.api import Topos, load
from skyfield import api

satellite = EarthSatellite("1 23455U 94089A   97320.90946019  .00000140  00000-0  10191-3 0  2621",
                           "2 23455  99.0090 272.6745 0008546 223.1686 136.8816 14.11711747148495", name = 'NOAA14')
ts = load.timescale()
t1 = ts.utc(1997, 11, 16, 21, 49, 38)
t2 = ts.utc(1997, 11, 16, 21, 49, 39)
print satellite,'\n'


geocentric = satellite.at(t1)
print(geocentric.position.km)
geocentric = satellite.at(t2)
print(geocentric.position.km)

bluffton = Topos('40.8939 N', '83.8917 W')
difference = satellite - bluffton
print(difference)

topocentric = difference.at(t1)

ra, dec, distance = topocentric.radec()



print(ra,dec,distance)

print(satellite.model.ecco)
print(satellite.epoch)
print(satellite.epoch.utc_jpl())








#THE BELOW WORKS

from skyfield.sgp4lib import EarthSatellite
from skyfield.api import Topos, load
from skyfield import api

satellite = EarthSatellite("1 23455U 94089A   97320.90946019  .00000140  00000-0  10191-3 0  2621",
                           "2 23455  99.0090 272.6745 0008546 223.1686 136.8816 14.11711747148495", name = 'NOAA14')
ts = load.timescale()

t3 = ts.utc(1997, 11, 16, 21, 49, 39)
t4 = ts.utc(1997, 11, 16, 21, 49, 40)

ICRF = satellite.at(t3) #THIS WORKS
print(ICRF.position.km)

ra, dec, distance = ICRF.radec() #THIS WORKS
print(ra,dec,distance)

ICRF = satellite.at(t4) #THIS WORKS
print(ICRF.position.km)

ra, dec, distance = ICRF.radec() #THIS WORKS
print(ra,dec,distance)
