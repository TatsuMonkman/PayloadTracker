#import numpy as np

#traps = np.loadtxt('trapazoid_referencedata.txt')
#Rolo  = np.loadtxt('ROLO_Results.txt')

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

#dy = []
#avg = 0

#for i in range(len(Rolo)):
#    dy.append(offset( Rolo[i], traps))
#    avg += offset( Rolo[i], traps)

#print dy #all offsets
#print avg / len(Rolo) #average offset
