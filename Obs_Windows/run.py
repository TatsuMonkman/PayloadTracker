#GOAL: an array with columns: datetime, Sat position, Moon position, Sat in eclipse? (Y/N), Moon shot possible?

import numpy as np
import subprocess
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


def monthrun(tle, line1, line2, line3, tle_date, tdelta):

    #Add time block to date to test future windows
    tle_date = tle_date + timedelta(weeks=tdelta, hours=0,
                                    minutes = 7, seconds=16)
    #dt is the run time (minutes)
    dt = 40320
    #st is the step time (minutes)
    st = 10

    print('Finding Observation times between ' + tle_date.isoformat(' ')
          + ' and ' + (tle_date + timedelta(minutes = dt)).isoformat(' ')
          + '\n')
    FindWindows(line1,line2, line3, tle_date, 0, dt, st, 'month')

    #Add the ephemeride file to history for future reference.
    subprocess.call('cp ' + line1 + '_month_etimes.dat ./history/' + line1
                    + '_month_etimes_' + tle_date.isoformat('-')[0:9] + '_to_'
                    + (tle_date + timedelta(minutes = dt)).isoformat('-')[0:9]
                    + '.dat', shell = True)
    #Add the ephemeride file to local directory. The file is named using the
    #TLE id name + _month_etimes_.dat
    subprocess.call('cp ' + line1 + '_month_etimes.dat ./history/' + line1
                    + '_month_etimes_' + '.dat', shell = True)

    with open('obs_times.txt','r') as f:
        obs = np.loadtxt(f)
    with open('noobs_times.txt', 'r') as f:
        nobs = np.loadtxt(f)
    with open('all_times.txt', 'r') as f:
        aobs = np.loadtxt(f)

    if len(obs) == 0:
        print('\nNo observation windows found between '
              + tle_date.isoformat(' ') + 'UST and '
              + (tle_date + timedelta(minutes = dt)).isoformat(' ')
              + 'UST at ' + str(st) + ' min step intervals\n\n')
        return 'NA'
    else:
        plot_2sets(obs,nobs)


def dayrun(tle, line1, line2, line3, tle_date, tdelta):

    #Add time block to future date
    tle_date = tle_date + timedelta(weeks=tdelta, minutes=0, seconds=0)
    dt = 24*60
    st = 1

    print('Finding Observation times between ' + tle_date.isoformat(' ')
          + ' and ' + (tle_date + timedelta(minutes = dt)).isoformat(' ')
          + '\n')

    FindWindows(line1,line2, line3, tle_date, 0, dt, st, 'day')

    subprocess.call('cp day_etimes.dat ' + line1 + '_day_etimes_'
                    + tle_date.isoformat('-')[0:9] + '_to_'
                    + (tle_date + timedelta(minutes = dt)).isoformat('-')[0:9]
                    + '.dat', shell = True)

    with open('obs_times.txt','r') as f:
        obs = np.loadtxt(f)
    with open('noobs_times.txt', 'r') as f:
        nobs = np.loadtxt(f)
    with open('all_times.txt', 'r') as f:
        aobs = np.loadtxt(f)

    if len(obs) == 0:
        print('\nNo observation windows found between '
              + tle_date.isoformat(' ') + 'UST and '
              + (tle_date + timedelta(minutes = dt)).isoformat(' ')
              + 'UST at ' + str(st) + ' min step intervals\n\n')
        return 'NA'
    else:
        plot_2sets(obs,nobs)



def check(file):
    print file
    rtle = read(file)
    rline1 = rtle[1][0] #TLE 'title'
    rline2 = rtle[1][1] #TLE line 1
    rline3 = rtle[1][2] #TLE line 2
    rtle_date = rtle[0] #Date/time of TLE (Assumed UTC, post 2000)
    rtle_date = rtle_date + timedelta(weeks = 3)

    #d1 and d2 are the start and stop times of the current 24hour mission plan
    d1 = rtle_date + timedelta(minutes = 10)
    d2 = rtle_date + timedelta(hours = 23, minutes = 55)
    print('Searching for obs times between '
          + d1.strftime('%H:%M:%S, %B %d, %Y') + ' and '
          + d2.strftime('%H:%M:%S, %B %d, %Y'))

    #i and j are flags to signify whether observations are possible
    i = 0
    j = 0

    #Ephemerides with correct observation geometry for the current month
    #are stored in good_month_etimes.dat
    with open('good_month_etimes.dat','r') as f:
        for line in f:
            line = line.split()
            gtime = datetime.strptime(line[1]+line[2], '%Y/%m/%d%H:%M:%S')
            if d2 < gtime:
                break
            elif d1 < gtime < d2:
                print('Obstime available:',
                      gtime.strftime('%H:%M:%S, %B %d, %Y'))
                i = 1
                pass
            else:
                pass
        if i == 1:
            raw_input('\nObs times within 24 hours found.'
            +' Calculating 24 hour window. Continue? ')
            o = dayrun(rtle, rline1, rline2, rline3, rtle_date, 0)
            return

        if i == 0:
            print('\nNo Obs times available between '
                  + d1.strftime('%H:%M:%S, %B %d, %Y') + ' and '
                  + d2.strftime('%H:%M:%S, %B %d, %Y') + '\n')
            raw_input('Checking current month-long window.'
                      + ' Continue? ')
            for line in f:
                line = line.split()
                gtime = datetime.strptime(line[1]+line[2], '%Y/%m/%d%H:%M:%S')
                if d2 < gtime:
                    print('Obstime available at '
                          + gtime.strftime('%H:%M:%S, %B %d, %Y'))
                    j = 1
                    pass
        if j == 1:
            raw_input('\nObs times found later this month.')
            pass
    if j == 0:
        raw_input('No obs times found later this month. Calculating over next '
                  + 'four week period. Continue? ')
        monthrun(rtle, rline1, rline2, rline3, rtle_date, 0)


tlefile = raw_input('Enter a TLE file for satellite position\nEnter'
                    + ' \'test\' for reference/testtle.tle\nTLE: ')

#check(tlefile)

rtle = read(tlefile)
rline1 = rtle[1][0] #TLE 'title'
rline2 = rtle[1][1] #TLE line 1
rline3 = rtle[1][2] #TLE line 2
rtle_date = rtle[0] #Date/time of TLE (Assumed UTC, post 2000)

#o = dayrun(rtle, rline1, rline2, rline3, rtle_date, 0)
monthrun(rtle, rline1, rline2, rline3, rtle_date, 0)
