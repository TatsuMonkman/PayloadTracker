#This script generates selenographic coordinates for the Earth, Sun, and spacecraft given a UTC date
#This script needs MoonMetdat.txt and its listed files to be in the same directory
#This script needs to know the TLE_SPK_OBJ_ID and SPK file of the spacecraft
#Need to double check some units...

def Calculate_SCoords(run):

    #setup
    import spiceypy as spice
    import numpy as np
    import math
    spice.furnsh("./MetDat/MoonMetdat.txt")

    #import ~_setup.txt and SPK (~.bsp) file
    slines = []
    with open(run + '_setup.txt') as f:
        slines = f.read().splitlines()
    spice.furnsh(run + '.bsp')

    #get TLE_SPK_OBJ_ID and et (time, seconds past J2000) from TLE File
    obj_id = slines[5].split('=')[1]
    et     = float(slines[28].split('=')[1])
    print ''
    print '\n', spice.et2utc(et, 'C', 3) #read out date as yyyy mmm dd hr:min:sec.millisecond

    #Calculate sub-observer point
    state = spice.spkezr(obj_id , et , "MOON_PA" , "LT+S" , "Moon")
    s_obs = spice.reclat(state[0][0:3])
    print '\nSub-Observer Point:'
    print 'slong: ', s_obs[1] * 180 / math.pi
    print 'slat:  ', s_obs[2] * 180 / math.pi

    #Calculate sub-Earth point
    state = spice.spkezr("Earth",et,"MOON_PA", "LT+S","Moon")
    s_eat = spice.reclat(state[0][0:3])
    print '\nSub-Earth Point:'
    print 'slong: ', s_eat[1] * 180 / math.pi
    print 'slat:  ', s_eat[2] * 180 / math.pi

    #Calculate sub-Sun point
    state = spice.spkezr("Sun",et,"MOON_PA", "LT+S","Moon")
    s_sun = spice.reclat(state[0][0:3])
    print '\nSub-Sun Point:'
    print 'slong: ', 90 - s_sun[1] * 180 / math.pi
    print 'slat:  ', s_sun[2] * 180 / math.pi, '\n'

    with open(run + '_spoints.txt', 'w') as f:
        f.write(''
                + '\nSub-Observer Point:'
                + '\n\tslong: ' + str(s_obs[1] * 180 / math.pi)
                + '\n\tslat: ' + str(s_obs[2] * 180 / math.pi)
                + '\n\nSub-Earth Point:'
                + '\n\tslong: ' + str(s_eat[1] * 180 / math.pi)
                + '\n\tslat: ' + str(s_eat[2] * 180 / math.pi)
                + '\n\nSub-Sun Point:'
                + '\n\tslong: ' + str(90 - s_sun[1] * 180 / math.pi)
                + '\n\tslat: ' + str(s_sun[2] * 180 / math.pi)
        )

    return [slines[21].split('=')[1][1:], et, s_obs, s_eat, s_sun]



#print Calculate_SCoords('SWIFT_201808521_1')
