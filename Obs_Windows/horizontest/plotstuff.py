from datetime import datetime
import numpy as np

def plot_4sets(i,s,m,t):
    import matplotlib.pyplot as plt
    import numpy as np

    fig = plt.figure()
    ax1 = fig.add_subplot(111)
#    ax1.scatter(i[:,0],i[:,2], s = 10, c = 'b', marker = 's',
#                label = 'ISS (Zarya)')
    ax1.scatter(s[:,0],s[:,2], s = 10, c = 'y', marker = 's',
                label = 'Sun')
    ax1.scatter(m[:,0],m[:,2], s = 10, c = '.75', marker = 's',
                label = 'Moon')
#    ax1.scatter(t[:,0],t[:,2], s = 10, c = 'm', marker = 's',
#                label = 'PyEphem ISS Position')

#    ax1.plot(n[:,2],n[:,3], c = 'b')
#    ax1.plot(o[:,2],o[:,3], c = 'y')
#    ax1.plot(o[:,8],o[:,9], c = 'g')
#    ax1.plot(n[:,6],n[:,7], c = 'm')
#    ax1.plot(o[:,6],o[:,7], c = 'r')
    plt.xlabel('RA (deg)')
    plt.ylabel('DEC (deg)')
    #    plt.ylim(ymin = 0, ymax = 0.1)
    plt.legend(loc = 'lower left')

    plt.grid(True)
    plt.show()

def plot_diffsets(i,s,m,t):
    import matplotlib.pyplot as plt
    import numpy as np

    fig = plt.figure()
    ax1 = fig.add_subplot(111)
#    ax1.scatter(i[:,0],(t[:,2] - i[:,2]), s = 10, c = 'b', marker = 's',
#                label = 'AQUA (EOS PM-1)')
    ax1.scatter(s[:,0],(t[:,6] - s[:,2]), s = 10, c = 'y', marker = 's',
                label = 'Sun')
    ax1.scatter(m[:,0],(t[:,4] - m[:,2]), s = 10, c = '.75', marker = 's',
                label = 'Moon')
#    ax1.scatter(t[:,0],t[:,2], s = 10, c = 'm', marker = 's',
#                label = 'PyEphem ISS Position')

#    ax1.plot(n[:,2],n[:,3], c = 'b')
#    ax1.plot(o[:,2],o[:,3], c = 'y')
#    ax1.plot(o[:,8],o[:,9], c = 'g')
#    ax1.plot(n[:,6],n[:,7], c = 'm')
#    ax1.plot(o[:,6],o[:,7], c = 'r')
#    plt.ylim(ymin=0.06,ymax=.085)
    plt.xlabel('Date')
    plt.ylabel('DEC Diff (deg)')
    plt.legend(loc = 'lower left')
    plt.title('Divergence Over Time of Horizon and PyEphem\n'
              + 'Coordinate Calcuations for Sun and Moon Positions')

    plt.grid(True)
    plt.show()

iss = []
sun = []
moon = []
test = []

aqua = []
atest = []

swift = []
stest = []

with open('deg_iss_horizon_results.dat','r') as f:
    lines = f.readlines()
    for line in lines:
        iss.append(line.split())
with open('deg_sun_horizon_results.dat','r') as f:
    lines = f.readlines()
    for line in lines:
        sun.append(line.split())
with open('deg_moon_horizon_results.dat','r') as f:
    lines = f.readlines()
    for line in lines:
        moon.append(line.split())
with open('iss_test_all_times.dat','r') as f:
    lines = f.readlines()
    for line in lines:
        test.append(line.split())

with open('deg_AQUA_horizon_results.dat','r') as f:
    lines = f.readlines()
    for line in lines:
        aqua.append(line.split())
with open('AQUA_test_all_times.dat','r') as f:
    lines = f.readlines()
    for line in lines:
        atest.append(line.split())

with open('deg_Swift_horizon_results.dat','r') as f:
    lines = f.readlines()
    for line in lines:
        swift.append(line.split())
with open('Swift_test_all_times.dat','r') as f:
    lines = f.readlines()
    for line in lines:
        stest.append(line.split())


issdt = []
sundt = []
moondt = []
testdt = []

aquadt = []
atestdt = []

swiftdt = []
stestdt = []


for i in range(len(iss)):
    issdt.append(datetime.strptime(iss[i][0]+iss[i][1], '%Y-%b-%d%H:%M'))
    sundt.append(datetime.strptime(sun[i][0]+sun[i][1], '%Y-%b-%d%H:%M'))
    moondt.append(datetime.strptime(moon[i][0]+moon[i][1], '%Y-%b-%d%H:%M'))
    testdt.append(datetime.strptime(test[i][1]+test[i][2], '%Y/%m/%d%H:%M:%S'))

for i in range(len(aqua)):
    aquadt.append(datetime.strptime(aqua[i][0]+aqua[i][1], '%Y-%b-%d%H:%M'))
    atestdt.append(datetime.strptime(atest[i][1]+atest[i][2], '%Y/%m/%d%H:%M:%S'))

for i in range(len(swift)):
    swiftdt.append(datetime.strptime(swift[i][0]+swift[i][1], '%Y-%b-%d%H:%M'))
    stestdt.append(datetime.strptime(stest[i][1]+stest[i][2], '%Y/%m/%d%H:%M:%S'))



for i in range(len(iss)):
    iss[i] = [float(iss[i][2])] + [float(iss[i][3])]
    sun[i] = [float(sun[i][2])] + [float(sun[i][3])]
    moon[i] = [float(moon[i][2])] + [float(moon[i][3])]
    test[i] = ([float(test[i][3])] + [float(test[i][4])]
              + [float(test[i][7])] + [float(test[i][8])]
              + [float(test[i][9])] + [float(test[i][10])])

for i in range(len(aqua)):
    aqua[i] = [float(aqua[i][2])] + [float(aqua[i][3])]
    atest[i] = ([float(atest[i][3])] + [float(atest[i][4])]
              + [float(atest[i][7])] + [float(atest[i][8])]
              + [float(atest[i][9])] + [float(atest[i][10])])

for i in range(len(swift)):
    swift[i] = [float(swift[i][2])] + [float(swift[i][3])]
    stest[i] = ([float(stest[i][3])] + [float(stest[i][4])]
              + [float(stest[i][7])] + [float(stest[i][8])]
              + [float(stest[i][9])] + [float(stest[i][10])])



for i in range(len(iss)):
    iss[i] = [issdt[i]] + iss[i]
    sun[i] = [sundt[i]] + sun[i]
    moon[i] = [moondt[i]] + moon[i]
    test[i] = [testdt[i]] + test[i]

for i in range(len(aqua)):
    aqua[i] = [aquadt[i]] + aqua[i]
    atest[i] = [atestdt[i]] + atest[i]

for i in range(len(swift)):
    swift[i] = [swiftdt[i]] + swift[i]
    stest[i] = [stestdt[i]] + stest[i]


print 'ISS: ', iss[1], len(iss)
print 'Moon: ', moon[1], len(moon)
print 'Sun: ', sun[1], len(sun)
print 'Test: ', test[1], len(test)

print 'AQUA: ', aqua[1], len(aqua)
print 'ATest: ', atest[1], len(atest)

print 'Swift: ', swift[1], len(swift)
print 'STest: ', stest[1], len(stest)


iss = np.asarray(iss)
sun = np.asarray(sun)
moon = np.asarray(moon)
test = np.asarray(test)

aqua = np.asarray(aqua)
atest = np.asarray(atest)

swift = np.asarray(swift)
stest = np.asarray(stest)

plot_diffsets(iss, sun, moon, test)
#plot_diffsets(sun, sun, moon, test)
#plot_diffsets(aqua, sun, moon, atest)
#plot_diffsets(swift, sun, moon, stest)
