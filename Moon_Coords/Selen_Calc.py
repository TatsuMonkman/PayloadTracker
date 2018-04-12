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
    #read out date as yyyy mmm dd hr:min:sec.millisecond
    print '\n', spice.et2utc(et, 'C', 3)

    #Calculate sub-observer point and distance
    state = spice.spkezr(obj_id , et , "MOON_PA" , "LT+S" , "Moon")
    s_obs = spice.reclat(state[0][0:3])
    print '\nSub-Observer Point:'
    print ' Sat-Moon distance: ', s_obs[0], 'km'
    print ' Satellite sub-long: ', s_obs[1]*180/math.pi, 'deg'
    print ' Satellite sub-lat:  ', s_obs[2]*180/math.pi, 'deg'

    #Calculate sub-Earth point and distance
    state = spice.spkezr("Earth",et,"MOON_PA", "LT+S","Moon")
    s_eat = spice.reclat(state[0][0:3])
    print '\nSub-Earth Point:'
    print ' Earth-Moon distance: ', s_eat[0], 'km'
    print ' Earth sub-long: ', s_eat[1]*180/math.pi, 'deg'
    print ' Earth sub-lat:  ', s_eat[2]*180/math.pi, 'deg'

    #Calculate sub-Sun point and distance
    state = spice.spkezr("Sun",et,"MOON_PA", "LT+S","Moon")
    s_sun = spice.reclat(state[0][0:3])
    print '\nSub-Sun Point:'
    print ' Sun-Moon distance: ', s_sun[0], 'km'
    print ' Sun sub-long: ', 90 - s_sun[1]*180/math.pi, 'deg'
    print ' Sun sub-lat:  ', s_sun[2]*180/math.pi, 'deg\n'


    #Writes selenographic coordiantes to a file named 'run'+_spoints.txt
    with open(run + '_spoints.txt', 'w') as f:
        f.write(''
                + '\n#Sub-Observer Point:'
                + '\n\t Sat-Moon distance: '+ str(s_obs[0])
                + '\n\t slong: ' + str(s_obs[1]*180/math.pi)
                + '\n\t slat: ' + str(s_obs[2]*180/math.pi)
                + '\n\n#Sub-Earth Point:'
                + '\n\t Earth-Moon distance: '+ str(s_eat[0])
                + '\n\t slong: ' + str(s_eat[1]*180/math.pi)
                + '\n\t slat: ' + str(s_eat[2]*180/math.pi)
                + '\n\n#Sub-Sun Point:'
                + '\n\t Sun-Moon distance: '+ str(s_sun[0])
                + '\n\t slong: ' + str(90 - s_sun[1]*180/math.pi)
                + '\n\t slat: ' + str(s_sun[2]*180/math.pi)
        )

    return [slines[21].split('=')[1][1:], et, s_obs, s_eat, s_sun]



#print Calculate_SCoords('SWIFT_201808521_1')
