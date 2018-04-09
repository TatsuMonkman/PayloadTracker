#And this is why you need comments...
#This script generates an RSR spectrum for a given instrument configuration.
#
import numpy as np

#Instrument telescope throughput:
with open('KE_Throughput_estimate.dat','r') as f:
    Tel = np.genfromtxt(f)

#Detector quantum efficiency:
with open('KE_QE_SparseCFA.dat','r') as f:
    QE = np.genfromtxt(f)

#Instrument filter throughput:
with open('Scout_Filter.dat','r') as f:
    Scout = np.genfromtxt(f)
    #Scout is upside down...
    Scout = np.flip(Scout, 0)


wTel = Tel[0][1:16:1].tolist()
tTel = Tel[15][1:16:1].tolist()

#Fit linear regressions between points in telescope throughput data
xymb = []

for i in range(len(wTel)-1):
    m = (tTel[i+1] - tTel[i])/(wTel[i+1] - wTel[i])
    b = tTel[i] - m*wTel[i]
    xymb.append([wTel[i],tTel[i],wTel[i+1],tTel[i+1],m,b])

Scout = Scout.tolist()
totaldata = QE.tolist()

#Compute total throughput
#Wavelength,QER1,QEG1,QEB1,QEP1,QER2,QEG2,QEB2,QEP2,Scout,Telescope
for i in range(len(totaldata)):
    for j in range(len(Scout)):
        #Match up qe and scout filter by wavelength
        if Scout[j][0] == totaldata[i][0]:
            totaldata[i] += [Scout[j][1::][0]/100]
            break

#These for loops add in telescope data
for i in range(len(totaldata)):
    for k in range(len(xymb)-1):
        if xymb[k+1][0] >= totaldata[i][0] >= xymb[k][0]:
            totaldata[i] += [(xymb[k][4]*totaldata[i][0] + xymb[k][5])]
            break

combined_data = []

#Trimming off the high end of the spectrum...
totaldata = totaldata[1:len(totaldata)-20:1]

#Multiply qe data by telescope and scout throughput, append to combined
#array alongth with total dat
for i in range(len(totaldata)):
    a = totaldata[i][1:9]
    a = [(x * totaldata[i][9] * totaldata[i][10]) for x in a]
    combined_data.append([totaldata[i][0]] + a)

qr2 = []
qg2 = []
qb2 = []
qp2 = []

for i in range(len(combined_data)):
    qr2.append(combined_data[i][5])
    qg2.append(combined_data[i][6])
    qb2.append(combined_data[i][7])
    qp2.append(combined_data[i][8])

#Find the maximum value of each filter and find it's location in the data..
print 'Max RQE: ', max(qr2)
print 'Index: ', qr2.index(max(qr2))
print totaldata[qr2.index(max(qr2))]
print 'Max QQE: ', max(qg2)
print 'Index: ', qg2.index(max(qg2))
print totaldata[qg2.index(max(qg2))]
print 'Max BQE: ', max(qb2)
print 'Index: ', qb2.index(max(qb2))
print totaldata[qb2.index(max(qb2))]
print 'Max PQE: ', max(qp2)
print 'Index: ', qp2.index(max(qp2))
print totaldata[qp2.index(max(qp2))]
#print 'Max QEB: ', max(totaldata)

#append normalized qe2 spectrum to combined_data
for i in range(len(combined_data)):
    combined_data[i] += ( [combined_data[i][5]/max(qr2)]
                        + [combined_data[i][6]/max(qg2)]
                        + [combined_data[i][7]/max(qb2)]
                        + [combined_data[i][8]/max(qp2)])
    pass


combined_data = np.asarray(combined_data)

wl    = combined_data[:,0]
r_rsr = combined_data[:,9]
g_rsr = combined_data[:,10]
b_rsr = combined_data[:,11]
p_rsr = combined_data[:,12]

#print np.concatenate((wl,rsr),axis=0)
with open('RSR_spec.dat','w') as f:
    f.write('#wl\tQR\n')
    for i in range(len(wl)):
        f.write(str(wl[i]) + '\t' + str(r_rsr[i]) +  '\t' + str(g_rsr[i])
                +  '\t' + str(b_rsr[i]) + '\t' + str(p_rsr[i]) +'\n')

with open('RSR_estimate.dat','w') as f:
    f.write('#Wavelength,\tQER1,\tQEG1,\tQEB1,\t,QEP1,\tQER2,\tQEG2,\tQEB2,\tQEP2,\tQER2 RSR,\tQEG2 RSR,\tQEB2 RSR,\tQEP2 RSR\n')
    np.savetxt(f, combined_data)
