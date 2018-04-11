#Find inter-point trapazoids for trapazoidal integration and function - data
#Technically only need to do one time once reference data is determined

#ref_file = '62231_avg_scaled_std_text'
#ref = np.loadtxt( ref_file + '.txt' ) #load reference text

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
#        print i, a[i+1][c1] - a[i][c1]
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
    a = 0.0
    for i in range(len(ref)):
        if xmin <= ref[i][0] < xmax:
            a += ref[i][6]
    print file +' TOTAL AREA : ', a,file
