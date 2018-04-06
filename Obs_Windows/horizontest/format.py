import numpy as np
from astropy import units as u
from astropy.coordinates import SkyCoord

moon = []
sun = []
iss = []
test = []

aqua = []
atest = []

swift = []
stest = []

with open('moon_horizon_results.dat','r') as f:
    for line in f:
        moon.append(line.split())

with open('sun_horizon_results.dat','r') as f:
    for line in f:
        sun.append(line.split())

with open('iss_horizon_results.dat','r') as f:
    for line in f:
        iss.append(line.split())

with open('iss_test_all_times.dat','r') as f:
    for line in f:
        test.append(line.split())


with open('AQUA_horizon_results.dat','r') as f:
    for line in f:
        aqua.append(line.split())

with open('AQUA_test_all_times.dat','r') as f:
    for line in f:
        atest.append(line.split())


with open('Swift_horizon_results.dat','r') as f:
    for line in f:
        swift.append(line.split())

with open('Swift_test_all_times.dat','r') as f:
    for line in f:
        stest.append(line.split())


print 'moon length: ', len(moon)
print 'sun length: ', len(sun)
print 'iss length: ', len(iss)
print 'test length: ', len(test)
print 'AQUA length: ', len(aqua)
print 'atest length: ', len(atest)
print 'Swift length: ', len(swift)
print 'stest length: ', len(stest)

moondeg = []
sundeg = []
issdeg = []
testdeg = []

aquadeg = []
atestdeg = []

swiftdeg = []
stestdeg = []

for i in range(len(moon)):
    c1 = SkyCoord(moon[i][2] + ' ' + moon[i][3], unit=(u.hourangle, u.deg))
    moondeg.append([moon[i][0]] + [moon[i][1]] + [c1.ra.deg] + [c1.dec.deg])
    c2 = SkyCoord(sun[i][2] + ' ' + sun[i][3], unit=(u.hourangle, u.deg))
    sundeg.append([sun[i][0]] + [sun[i][1]] + [c2.ra.deg] + [c2.dec.deg])
    c3 = SkyCoord(iss[i][2] + ' ' + iss[i][3], unit=(u.hourangle, u.deg))
    issdeg.append([iss[i][0]] + [iss[i][1]] + [c3.ra.deg] + [c3.dec.deg])

for i in range(len(aqua)):
    c1 = SkyCoord(aqua[i][2] + ' ' + aqua[i][3], unit=(u.hourangle, u.deg))
    aquadeg.append([aqua[i][0]] + [aqua[i][1]] + [c1.ra.deg] + [c1.dec.deg])

for i in range(len(swift)):
    c1 = SkyCoord(swift[i][2] + ' ' + swift[i][3], unit=(u.hourangle, u.deg))
    swiftdeg.append([swift[i][0]] + [swift[i][1]] + [c1.ra.deg] + [c1.dec.deg])


with open('deg_moon_horizon_results.dat','w') as f:
    for i in range(len(moondeg)):
        for j in range(len(moondeg[i])):
            f.write(str(moondeg[i][j]) + '\t\t')
        f.write('\n')

with open('deg_sun_horizon_results.dat','w') as f:
    for i in range(len(sundeg)):
        for j in range(len(sundeg[i])):
            f.write(str(sundeg[i][j]) + '\t\t')
        f.write('\n')

with open('deg_iss_horizon_results.dat','w') as f:
    for i in range(len(issdeg)):
        for j in range(len(issdeg[i])):
            f.write(str(issdeg[i][j]) + '\t\t')
        f.write('\n')

with open('deg_AQUA_horizon_results.dat','w') as f:
    for i in range(len(aquadeg)):
        for j in range(len(aquadeg[i])):
            f.write(str(aquadeg[i][j]) + '\t\t')
        f.write('\n')

with open('deg_Swift_horizon_results.dat','w') as f:
    for i in range(len(swiftdeg)):
        for j in range(len(swiftdeg[i])):
            f.write(str(swiftdeg[i][j]) + '\t\t')
        f.write('\n')
