#Find inter-point trapazoids for trapazoidal integration and function - data
#Technically only need to do one time once reference data is determined




#ref_file = '62231_avg_scaled_std_text'
#ref = np.loadtxt( ref_file + '.txt' ) #load reference text

def make_traps(a):
    import numpy as np
    data = []
    for i in (range(len( a ) - 1 ) ):
        w0 = a[i][0]
        w1 = a[i+1][0]
        r0 = a[i][1]
        r1 = a[i+1][1]
        b = ( a[i+1][1] - a[i][1] ) / ( a[i+1][0] - a[i][0] )
        m =  ( a[i+1][1] - b * a[i+1][0])
        A = ( ( a[i+1][1] + a[i][1] ) / 2 ) * ( a[i+1][0] - a[i][0] )
        data.append([w0,w1,r0,r1,b,m,A])
    return np.asarray(data)


#with open( 'trapazoids_' + ref_file + '.txt', 'w') as f:
#    f.write('#trapazoidal\n# startwidth \t\tendwidth \t\tstartheight \t\tendheight \t\tslope \t\t\ty-intercept \t\t\tarea\n')
#    np.savetxt(f, make_traps(ref))
