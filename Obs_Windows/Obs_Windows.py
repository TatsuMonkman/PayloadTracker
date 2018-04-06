#The two functions in this script return the positions of the sun, observer,
#and moon relative to the earth in geocentric lat lon coordinates and finds
#suitable observation windows based on the moon-observer-earth geometry,
#respectively.

def compute_ephem(line1, line2, line3, time, time_step):
    #This function returns the time of the ephemeris (dtime), the ephemeris
    #of the satellite (Sc.ra.deg, Sc.dec.deg) (RA, DEC, elevation), whether the
    #satellite is in eclipse (e) (0=no,1=yes), the ephemeris of the moon
    #(Mc.ra.deg, Mc.dec.deg) (RA, DEC), the ephemeris of the sun (Suc.ra.deg,
    #Suc.dec.deg) (RA, DEC), and lunar phase (mp) (radians; 0=full, +/-pi =
    #new). All ephemerides are given in geocentric coordinates.

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

    #Print ephemerides for manual checking.
    #print('Moon: %s %s' % (m.g_ra, m.g_dec))
    #print('Sun: %s %s' % (su.g_ra, su.g_dec))
    #print('Sat: %s %s' % (sat_ephem.a_ra, sat_ephem.a_dec))

    #Convert ephemeris to degrees
    Sc = SkyCoord(str(sat_ephem.a_ra) + ' ' + str(sat_ephem.a_dec),
                  unit=(u.hourangle, u.deg))
    Mc = SkyCoord(str(m.g_ra) + ' ' + str(m.g_dec),
                  unit=(u.hourangle, u.deg))
    Suc = SkyCoord(str(su.g_ra) + ' ' + str(su.g_dec),
                   unit=(u.hourangle, u.deg))

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

    #Returnt calculated values as a 10-element list
    return([dtime, Sc.ra.deg, Sc.dec.deg, sat_ephem.elevation, e,
            Mc.ra.deg, Mc.dec.deg, Suc.ra.deg, Suc.dec.deg, mp])



def FindWindows(name, tle1, tle2, date, start, stop, minstep, dt):
    #Given the lines of a tle (line1: name, line2: tle1, line3: tle2)
    #a start time, stop time, and timestep (minutes) return an
    #ephemeris / observation window array. Returned array contains all
    #information calculated in compute_ephem for each timestep.

    import numpy as np
    from datetime import datetime, timedelta
    import subprocess

    all = []
    good = []
    bad = []

    #Find possible observation windows between start / stop dates
    #using file io for test
    f = open(name + '_' + dt + '_etimes.dat','w')
    g = open(name + '_good_' + dt + '_etimes.dat','w')
    b = open(name + '_bad_' + dt + '_etimes.dat','w')
    for i in range(start, stop, minstep):
        pos = compute_ephem(name, tle1, tle2, date, i)
        #Check if the moon and satellite are within 170degs of each other in
        #RA and DEC.
        if ((abs(pos[1] - pos[5]) < 85) and (abs(pos[2] - pos[6]) < 85)
                and pos[4] == 1
                and pos[9] <= (2)):
            print 'Yes: ', [1] + [pos[4]] + pos
            good.append([1] + pos)
            all.append([1] + pos)
            f.write('1\t')
            g.write('1\t')
            for j in range(len(pos)):
                f.write(str(pos[j])+'\t')
                g.write(str(pos[j])+'\t')
            f.write('\n')
            g.write('\n')

        else:
            print 'No: ', [0] + [pos[4]] + pos
            bad.append([0] + pos)
            all.append([0] + pos)
            f.write('0\t')
            b.write('0\t')
            for j in range(len(pos)):
                f.write(str(pos[j])+'\t')
                b.write(str(pos[j])+'\t')
            f.write('\n')
            b.write('\n')
    f.close()
    g.close()
    b.close()

def readet(file):
    from datetime import datetime, timedelta
    import numpy as np
    #This script pull ephemerides from *etimes.dat files and
    #convert them into arrays suitable for matplotlib.
    obs = []
    with open(file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            a = line.split()
            fl = a[3:12]
            fl = [float(i) for i in fl]
            obs.append([float(a[0])]
                        + [datetime.strptime(a[1]+a[2], '%Y/%m/%d%H:%M:%S')]
                        + fl)
    obs = np.asarray(obs)
    return obs
