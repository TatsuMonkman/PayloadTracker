#PyEphem Test
#PyEphem SGP4 test
#Geographic point beneath satellite:
#sublat - Latitude (+N)
#sublong - Longitude (+E)
#Ultimately want to read in TLE and date file
#Ephem: Dates are ALWAYS UTC

import ephem
import astropy
from astropy import units as u
from astropy.coordinates import SkyCoord


dt = '2005-03-22 07:27:59.652049' #datetime yyyy/mm/dd Hr:Min:Sec

#Define TLE File
line1 = 'NOAA 14' #
line2 = '1 23455U 94089A   04366.74530554  .00000332  00000-0  20061-3 0  4198' #See TLE file notes
line3 = '2 23455  99.1151  46.1451 0010115 112.6215 247.6058 14.13524725515843'

NOAA14 = ephem.readtle(line1, line2, line3)
NOAA14.compute(dt)

m = ephem.Moon(dt)
m.compute(dt)

print('NOAA14\tRA,\t\tDEC,\t\tElevation,\tEclipsed? \n \t%s \t%s \t%s \t%s' % (NOAA14.ra, NOAA14.dec, NOAA14.elevation, NOAA14.eclipsed))
print('Moon\tRA\t\tDEC\n\t%s\t%s\n' % (m.ra, m.dec))

Nc = SkyCoord(str(NOAA14.ra)+' '+str(NOAA14.dec), unit=(u.hourangle, u.deg))
Mc = SkyCoord(str(m.ra)+' '+str(m.dec), unit=(u.hourangle, u.deg))


print('NOAA14\t%s\t\t%s' % (Nc.ra.deg, Nc.dec.deg))
print('Moon\t%s\t%s' % (Mc.ra.deg, Mc.dec.deg))


#Extrapolate forward in time
from datetime import datetime, timedelta

utcnow = datetime.utcnow()
hour = timedelta(hours = 1)
day = timedelta(days = 1.1)

print(utcnow + 5*hour)
print(utcnow + 5*day)

datetime.strptime('2005-03-22 02:27:59.652049', '%Y-%m-%d %H:%M:%S.%f') #return a datetime object, corresponding to date_string parsed according to format


#NOAA14 Test
