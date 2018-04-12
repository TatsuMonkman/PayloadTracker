#Find inter-point trapazoids for trapazoidal integration and function - data
#Technically only need to do one time once reference data is determined

def trap_file(file, newfile, xcol, ycol):
    #This function reads in column data from a file (called *FILENAME*)
    #and creates a series of trapazoids using
    #make_traps and writes them to a file called trapazoid_*FILENAME*.
    import numpy as np

    ref = np.loadtxt(file)
    with open(newfile, 'w') as f:
        f.write('#trapazoidal\n# startwidth \t\tendwidth \t\tstartheight'
                + '\t\tendheight \t\tslope \t\t\ty-intercept \t\t\tarea\n')
        np.savetxt(f, make_traps(ref, xcol, ycol), fmt='%4f')
    return



def make_traps(a, c1, c2):
    #This script takes in set of xy positions and returns a set of
    #trapazoids between points with adjacent x positions
    #(for a file that has already bee organized by ascending x-value).
    #This script expects 'a' to be a numpy array structured with
    #column0=x and column1=y. I will usually use x for wavelength
    #and y for throughput.
    import numpy as np

    data = []
    for i in (range(len( a ) - 1)):
        #Dimensions of each derived trapazoid (angled side is given by
        #a linear function in x)
        w0 = a[i][c1]    #start x-value
        w1 = a[i+1][c1]  #end x-value
        r0 = a[i][c2]    #start height
        r1 = a[i+1][c2]  #end height
        b  = (a[i+1][c2] - a[i][c2])/(a[i+1][c1] - a[i][c1])    #slope
        m  = (a[i+1][c2] - b*a[i+1][c1])                        #y-intercept
        A  = ((r1 + r0)/2)*(w1 - w0)                            #trapazoid area
        data.append([w0,w1,r0,r1,b,m,A])
    return np.asarray(data)



def trap_integrate(file, xmin, xmax):
    #Returns the integrated area of a trapazoid file
    #Col0 startx; Col1 endx; Col2 starty; Col3 endy, Col4 slope,
    #Col5 y-intercept, Col6 area
    import numpy as np

    ref = np.genfromtxt(file)
    ta = 0.0
    for i in range(len(ref)):
        #Special case for when the xmin and xmax fall in between
        #the same two reference data points
        if (ref[i][1] > xmax) and (ref[i][1] > xmin >= ref[i][0]):
            m = ref[i][4]
            b = ref[i][5]
            ymin = m*xmin + b
            ymax = m*xmax + b
            ta += ((ymax + ymin)/2)*(xmax - xmin)
            break
        #Case for when xmax is one or more data points higher than
        #xmin
        elif ref[i][1] > xmin >= ref[i][0]:
            m = ref[i][4]
            b = ref[i][5]
            y = m*xmin + b
            ta += ((y + ref[i][3])/2)*(ref[i][1] - xmin)
            break
    for j in range(i+1, len(ref)):
        if xmax > ref[j][1]:
            ta += ref[j][6]
        elif ref[j][0] < xmax <= ref[j][1]:
            m = ref[j][4]
            b = ref[j][5]
            y = m*xmax + b
            ta += ((y + ref[j][2])/2)*(xmax - ref[j][0])
            break

    print file +' TOTAL AREA : ', ta,file
    return ta

#trap_integrate('testtrap.txt',1.1,1.9)
