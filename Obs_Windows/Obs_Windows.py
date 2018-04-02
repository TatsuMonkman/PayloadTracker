#GOAL: an array with columns: datetime, Sat position, Moon position, Sat in eclipse? (Y/N), Moon shot possible?

def compute_ephem(line1, line2, line3, time, time_step):
    import numpy as np
    from datetime import datetime, timedelta
    import math
    import ephem
    from astropy import units as u
    from astropy.coordinates import SkyCoord

    dt = time + timedelta(minutes = time_step)

    #Compute satellite and moon ephemerides
    sat_ephem = ephem.readtle(line1, line2, line3)
    sat_ephem.compute(dt)
    m = ephem.Moon(dt)
    m.compute(dt)
    su = ephem.Sun(dt)
    su.compute(dt)

    #Convert ephemeris to degrees
    Sc = SkyCoord(str(sat_ephem.ra) + ' ' + str(sat_ephem.dec),
                  unit=(u.hourangle, u.deg))
    Mc = SkyCoord(str(m.ra) + ' ' + str(m.dec), unit=(u.hourangle, u.deg))
    Suc = SkyCoord(str(su.ra) + ' ' + str(su.dec), unit=(u.hourangle, u.deg))

    #Compute lunar phase in absolute phase angle (radians)
    dtime = ephem.Date(dt)
    nnm = ephem.next_new_moon    (dtime)
    pnm = ephem.previous_new_moon(dtime)
    lunation=(dtime-pnm)/(nnm-pnm)
    mp = abs(lunation - 0.5)*2*math.pi

    #Determine if satellite is in eclipse
    if sat_ephem.eclipsed == False:
        e = 0
    if sat_ephem.eclipsed == True:
        e = 1

    return([dtime, Sc.ra.deg, Sc.dec.deg, sat_ephem.elevation, e,
            Mc.ra.deg, Mc.dec.deg, Suc.ra.deg, Suc.dec.deg, mp])



def FindWindows(name, tle1, tle2, date, start, stop, minstep):
    import numpy as np
    from datetime import datetime, timedelta
    import subprocess
    #Given a start time, stop time, and timestep (minutes)>
    #>return an ephemeris / observation window array

    all = []
    good = []
    bad = []

    for i in range(start, stop, minstep):
        pos = compute_ephem(name, tle1, tle2, date, i)
        #Check if the moon and satellite are within 170degs of each other in RA and DEC.

        if ((abs(pos[1] - pos[5]) < 85) and (abs(pos[2] - pos[6]) < 85)
                and pos[4] == 1 and pos[9] <= (2)):
            print 'Yes: ', [1] + [pos[4]] + pos
            good.append([1] + pos)
            all.append([1] + pos)
        else:
            print 'No: ', [0] + [pos[4]] + pos
            bad.append([0] + pos)
            all.append([1] + pos)

    #string to add to filename
    dstring = (date.isoformat(' ')[0:4] + '_' + date.isoformat(' ')[5:7]
              + '_' + date.isoformat(' ')[9:10] + '_')

    #'all' is an array of all ephemerides
    all = np.asarray(all)
    fname = name + '_' + dstring + 'all_times.txt'
    with open(fname,'w') as f:
        f.write('#All ephemerides over DATES\n#Observation possible? (0=n,1=y)'
                + 'Spacecraft RA (deg);\t\tSpacecraft DEC (deg);\tSpacecraft'
                + ' Elevation (?);\tIn Eclipse? (no=0,yes=1);\tMoon RA (deg);'
                + '\tMoon Dec (deg);\tLunar Phase (per/full)\n')
        np.savetxt(f, all)
    subprocess.call('cp '+ fname + ' ./all_times.txt', shell=True)
    subprocess.call('mv ' + fname +' ./history', shell=True)

    #'good' is an array of possible observation opportunities.
    good = np.asarray(good)
    fname = name + '_' + dstring + 'obs_times.txt'
    with open(fname,'w') as f:
        f.write('#Observation-possible ephemerides over DATES\n'
                + '#Observation possible? (0=n,1=y)\t'
                + 'Spacecraft RA (deg);\t\tSpacecraft DEC (deg);\tSpacecraft'
                + ' Elevation (?);\tIn Eclipse? (no=0,yes=1);\tMoon RA (deg);'
                + '\tMoon Dec (deg);\tLunar Phase (per/full)\n')
        np.savetxt(f, good)
    subprocess.call('cp ' + fname + ' ./obs_times.txt', shell=True)
    subprocess.call('mv ' + fname +' ./history', shell=True)

    #'bad' is an array of all other sun-moon-satellite ephemerides.
    bad = np.asarray(bad)
    fname = name + '_' + dstring + 'noobs_times.txt'
    with open(fname,'w') as f:
        f.write('#No observation-possible ephemerides over DATES\n'
                + '#Observation possible? (0=n,1=y)\t'
                + 'Spacecraft RA (deg);\t\tSpacecraft DEC (deg);\tSpacecraft '
                + 'Elevation (?);\tIn Eclipse? (no=0,yes=1);\tMoon RA (deg);\tMoon'
                + ' Dec (deg);\tLunar Phase (per/full)\n')
        np.savetxt(f, bad)
    subprocess.call('cp '+ fname + ' noobs_times.txt', shell=True)
    subprocess.call('mv ' + fname +' ./history', shell=True)
