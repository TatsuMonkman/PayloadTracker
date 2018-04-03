#This function returns the date of the tle as a datetime object
#followed by a list containing the three TLE lines (no line breaks).

def read(t_file):
    import os
    from datetime import datetime, timedelta

    #read TLE File
    tle = [x for x in os.listdir('.') if x == (t_file)] #find raw tle file in directory need to turn into t_file

    if tle == []: #check if TLE file is present
        print 'TLE File named ' + t_file + ' not found'
        return

    lines   = []
    with open(tle[0]) as f:
        lines = f.readlines()
    print '\nTLE File:\n',lines[0][0:-1]+ '\n',lines[1],lines[2]

    #This block extracts the date of observation, assuming after yr 2000.
    #When naming files, all files from same hour will be labeled in>
    #>the order they were taken.
    yr   = '20'+lines[1][18:20] #year
    dy    = lines[1][20:23]     #day
    subdy = lines[1][23:32]     #day frac
    hr   = int(float(subdy)*24) #find hour, round down.
    mn    = int((float(subdy)*24 - hr) * 60)
    sc    = (((float(subdy)*24 - hr) * 60) - mn)*60

    #Format TLE file (need to get rid of \n at the end of each line string)
    lines[0] = lines[0][0:-1]
    lines[1] = lines[1][0:-1]
    if '\n' in lines[2]:
        lines[2] = lines[2][0:-1]
    tle_date = (datetime(int(yr), 1,1,0,0)
                + timedelta(days = float(dy + subdy) - 1))

    return(tle_date, lines)
