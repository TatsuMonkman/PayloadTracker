#takes in general offset and spits out trapazoidal integration of shifted reference data

def integrate(file, offset):
    import numpy as np
    from find_traps import make_traps

#    ref_file = '62231_avg_scaled_std_text'
#    ref = np.loadtxt( ref_file + '.txt' )
    ref_file = file
    ref = np.loadtxt( ref_file )



    print ref[:,1]

    ref[:,1] -= offset

    print ref[:, 1]

    with open('scaled_trapazoid_' + ref_file,'w') as f:
        f.write('#scaled trapazoidal data for ' + ref_file +'.txt\n# startwidth \t\tendwidth \t\tstartheight \t\tendheight \t\tslope \t\t\ty-intercept \t\t\tarea\n')
        np.savetxt(f, make_traps(ref))
