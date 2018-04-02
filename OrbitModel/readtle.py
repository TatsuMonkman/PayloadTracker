#Function to read in tle file and return tle lines in 3-line list, along witht the date
#PyEphem wants tle file lines each be an element in a 3-element list

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

    #Extract date of observation
    yr   = '20'+lines[1][18:20] #year
    dy    = lines[1][20:23]     #day
    subdy = lines[1][23:32]     #day frac
    hr   = int(float(subdy)*24) #find hour, round down. When naming files all files from same hour will be labeled in the order they were taken
    mn    = int((float(subdy)*24 - hr) * 60)
    sc    = (((float(subdy)*24 - hr) * 60) - mn)*60

    #Format TLE file (need to get rid of \n at the end of each line string)
    lines[0] = lines[0][0:-1]
    lines[1] = lines[1][0:-1]
    lines[2] = lines[2][0:-1]
    tle_date = datetime(int(yr), 1,1,0,0) + timedelta(days = float(dy + subdy) - 1) #CHECK THIS

    return(tle_date, lines) #returns date AS A DATETIME OBJECT followed by a list containing the TLE lines (no line breaks)
