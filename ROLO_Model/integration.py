#Find inter-point trapazoids for trapazoidal integration and function - data
#Technically only need to do one time once reference data is determined

#ref_file = '62231_avg_scaled_std_text'
#ref = np.loadtxt( ref_file + '.txt' ) #load reference text

def make_traps(a):
    import numpy as np
    data = []
    for i in (range(len( a ) - 1 )):
        w0 = a[i][0]
        w1 = a[i+1][0]
        r0 = a[i][1]
        r1 = a[i+1][1]
        b = (a[i+1][1] - a[i][1])/(a[i+1][0] - a[i][0])
        m =  (a[i+1][1] - b * a[i+1][0])
        A = ((a[i+1][1] + a[i][1])/2)*(a[i+1][0] - a[i][0])
        data.append([w0,w1,r0,r1,b,m,A])
    return np.asarray(data)


def offset( targ, ref): #expects a one dimensional array for target and full list from trapazoids
    os = 0

    for i in range(len(ref)): #THIS SCRIPT CAN BE OPTIMIZED
        if ref[i][0] == targ[0]:
            print ref[i][0], targ[0]
            os = ref[i][2]
            print 'found offset for ' + str(targ[0]) + ': ' + str(os)
            break
        elif ref[i][0] <= targ[0] <= ref[i+1][0]:
            print ref[i][0], targ[0]
            os = ref[i][4] * targ[0] + ref[i][5] - targ[1] #offset offset = m * w + b - R
            print 'found offset for ' + str(targ[0]) + ': ' + str(os)
            break
        else:
            pass

    return os


def integrate(file, offset):


    import numpy as np
    from find_traps import make_traps

    #    ref_file = '62231_avg_scaled_std_text'
    #    ref = np.loadtxt( ref_file + '.txt' )
    ref_file = file
    ref = np.loadtxt(ref_file)

    ref[:,1] -= offset


    with open('scaled_trapazoid_' + ref_file,'w') as f:
        f.write('#scaled trapazoidal data for ' + ref_file
        + '.txt\n# startwidth \t\tendwidth \t\tstartheight'
        + ' \t\tendheight \t\tslope \t\t\ty-intercept \t\t\tarea\n')

        np.savetxt(f, make_traps(ref))
