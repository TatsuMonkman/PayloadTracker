

def makesetup(t_file):
    #This function generates a setup file from a TLE file (input) and returns setup file name (output)
    #The setup file is formatted to be read into the SPICE mkspk utility

    #setup
    import spiceypy as spice
    import os
    spice.furnsh("./MetDat/MoonMetdat.txt") #spice.getelm needs leapsecond kernel (naif0011.)

    #read TLE File
    tlefile = t_file
    tle     = [x for x in os.listdir('.') if x == (tlefile)] #find raw tle file in directory
    lines   = []
    with open(tle[0]) as f:
        lines = f.readlines()
    print '\n',lines[0][0:-1]+' TLE File:\n',lines[1],lines[2]


    #Extract date of observation
    year   = '20'+lines[1][18:20]
    day    = lines[1][20:23]
    subday = lines[1][23:32]
    hour   = int(float(subday)*24) #find hour, round down. When naming files all files from same hour will be labeled in the order they were taken
    min    = int((float(subday)*24 - hour) * 60)
    sec    = (((float(subday)*24 - hour) * 60) - min)*60

    #Format TLE file (need to get rid of \n at the end of each line string)
    lines[0] = lines[0][0:-1]
    lines[1] = lines[1][0:-2]
    lines[2] = lines[2][0:-2]
    tlelines = [lines[1],lines[2]]

    get = spice.getelm(int(year), 138, tlelines) #getelm needs year of obs, length of the tle file (total)


    #Pull TLE_INPUT_OBJ_ID, TLE_SPK_OBJ_ID, SEGMENT_ID from TLE File
    input_id = lines[1][2:7]
    spk_id   = '-1'+lines[1][2:7]
    seg_id   = lines[0]

    #Make setup file
    spacecraft = lines[0] #Same as seg_id
    num = 1 #index for observations taken in the same hour
    setn = spacecraft + '_' + year + str(day) + str(hour) + '_' + str(num) #name setup file
    with open(setn + '_setup.txt','w') as f:
        f.write('\\begindata\n\n'
                + '\tINPUT_DATA_TYPE   = \'TL_ELEMENTS\'\n'
                + '\tOUTPUT_SPK_TYPE   = 10\n'
                + '\tTLE_INPUT_OBJ_ID  = '+ input_id + '\n'
                + '\tTLE_SPK_OBJ_ID    = ' + spk_id + '\n'
                + '\tCENTER_ID         = 399\n'
                + '\tREF_FRAME_NAME    = \'J2000\'\n'
                + '\tTLE_START_PAD     = \'2 days\'\n'
                + '\tTLE_STOP_PAD      = \'2 days\'\n'
                + '\tLEAPSECONDS_FILE  = \'naif0011.tls\'\n'
                + '\tINPUT_DATA_FILE   = \'' + tlefile + '\'\n'
                + '\tOUTPUT_SPK_FILE   = \'' + setn + '.bsp\'\n'
                + '\tPCK_FILE          = \'geophysical.ker\'\n'
                + '\tSEGMENT_ID        = \'NOAA-14 TLE-based Trajectory\'\n'
                + '\tPRODUCER_ID       = \'Tatsu the Intern, SFI\''
                + '\n\n\\begintext\n\n'
                + '\tObservation info:\n\n'
                + '\tSpacecraft        = ' + spacecraft + '\n'
                + '\tYear              = ' + year + '\n'
                + '\tDay               = ' + str(day) + '\n'
                + '\tHour              = ' + str(hour) + '\n'
                + '\tMinute            = ' + str(min) + '\n'
                + '\tSecond            = ' + str(sec) + '\n'
                + '\tTLE File          = ' + str(tlefile) + '\n'
                + '\tJD(sec past J2000)= ' + str(get[0]) + '\n\n')

    print('Setup file named ' + setn + '_setup.txt')

    return setn + '_setup.txt'

print makesetup('testtle.tle')
