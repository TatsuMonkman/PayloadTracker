#GOAL: an array with columns: datetime, Sat position, Moon position, Sat in eclipse? (Y/N), Moon shot possible?

import numpy as np
from datetime import datetime, timedelta
from readtle import read
from Obs_Windows import compute_ephem, FindWindows
from plotstuff import plot_2sets

#Correct TLE format for reading by PyEphem:
#line1 = 'NOAA14'
#line2 = '1 23455U 94089A   95203.26064305  .00000019  00000-0  34607-4 0  2610'
#line3 = '2 23455  98.9054 145.5029 0010414  92.4952 267.7414 14.11522321 28769'
#Beware: newline strings often screw up TLE file readers
#Read reads the tle file and returns a tuple with (time and [lines]):

tle = read('testtle.tle')
line1 = tle[1][0] #TLE 'title'
line2 = tle[1][1] #TLE line 1
line3 = tle[1][2] #TLE line 2
tle_date = tle[0] #Date/time of TLE (Assumed UTC)



#Add time block to future date
tle_date = tle_date + timedelta(weeks = 1)
dt = 40320
st = 10

print('Finding Observation times between ' + tle_date.isoformat(' ') + ' and '
      + (tle_date + timedelta(minutes = dt)).isoformat(' ') + '\n')

FindWindows(line1,line2, line3, tle_date, 0, dt, st)


with open('obs_times.txt','r') as f:
    obs = np.loadtxt(f)
with open('noobs_times.txt', 'r') as f:
    nobs = np.loadtxt(f)
with open('all_times.txt', 'r') as f:
    aobs = np.loadtxt(f)

if len(obs) == 0:
    print('\nNo observation windows found between ' + tle_date.isoformat(' ')
          + 'UST and ' + (tle_date + timedelta(minutes = dt)).isoformat(' ')
          + 'UST at ' + str(st) + ' min step intervals\n\n')
    pass
else:
    plot_2sets(obs,nobs)
