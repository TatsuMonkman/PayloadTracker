import numpy as np


with open('KE_Throughput_estimate.dat','r') as f:
    Tel = np.genfromtxt(f)

with open('KE_QE_SparseCFA.dat','r') as f:
    QE = np.genfromtxt(f)

with open('Scout_Filter.dat','r') as f:
    Scout = np.genfromtxt(f)
    #Scout is upside down...
    Scout = np.flip(Scout, 0)


wTel = Tel[0][1:16:1].tolist()
tTel = Tel[15][1:16:1].tolist()

xymb = []

for i in range(len(wTel)-1):
    m = (tTel[i+1] - tTel[i])/(wTel[i+1] - wTel[i])
    b = tTel[i] - m*wTel[i]
    xymb.append([wTel[i],tTel[i],wTel[i+1],tTel[i+1],m,b])

Scout = Scout.tolist()
totaldata = QE.tolist()

qr2 = []
qg2 = []
qb2 = []
qp2 = []

for i in range(len(totaldata)):
    qr2.append(totaldata[i][5])
    qg2.append(totaldata[i][6])
    qb2.append(totaldata[i][7])
    qp2.append(totaldata[i][8])

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

#Compute total throughput
#Wavelength,QER1,QEG1,QEB1,QEP1,QER2,QEG2,QEB2,QEP2,Scout,Telescope,product
for i in range(len(totaldata)):
    for j in range(len(Scout)):
        if Scout[j][0] == totaldata[i][0]:
            totaldata[i] += [Scout[j][1::][0]/100]
            break

#These for loops add in telescope data
for i in range(len(totaldata)):
    for k in range(len(xymb)-1):
        if xymb[k+1][0] >= totaldata[i][0] >= xymb[k][0]:
            totaldata[i] += [(xymb[k][4]*totaldata[i][0] + xymb[k][5])]
            break

for i in range(len(totaldata)):
    for k in range(len(xymb)-1):
        if xymb[k+1][0] >= totaldata[i][0] >= xymb[k][0]:
            #THE LINES BELOW IS WHERE YOU CALCULATE TOTAL RESPONSE
            totaldata[i] += [(totaldata[i][5]/max(qr2))*(totaldata[i][9]*totaldata[i][10])/(totaldata[qr2.index(max(qr2))][9]*totaldata[qr2.index(max(qr2))][10])]
            totaldata[i] += [(totaldata[i][6]/max(qg2))*(totaldata[i][9]*totaldata[i][10])/(totaldata[qg2.index(max(qg2))][9]*totaldata[qg2.index(max(qg2))][10])]
            totaldata[i] += [(totaldata[i][7]/max(qb2))*(totaldata[i][9]*totaldata[i][10])/(totaldata[qb2.index(max(qb2))][9]*totaldata[qb2.index(max(qb2))][10])]
            totaldata[i] += [(totaldata[i][8]/max(qp2))*(totaldata[i][9]*totaldata[i][10])/(totaldata[qp2.index(max(qp2))][9]*totaldata[qp2.index(max(qp2))][10])]

            break

#Trimming off the high end of the spectrum...
totaldata = totaldata[1:len(totaldata)-20:1]

totaldata = np.asarray(totaldata)

wl    = totaldata[:,0]
r_rsr = totaldata[:,11]
g_rsr = totaldata[:,12]
b_rsr = totaldata[:,13]
p_rsr = totaldata[:,14]

#print np.concatenate((wl,rsr),axis=0)
with open('RSR_spec.dat','w') as f:
    f.write('#wl\tQR\n')
    for i in range(len(wl)):
        f.write(str(wl[i]) + '\t' + str(r_rsr[i]) +  '\t' + str(g_rsr[i])
                +  '\t' + str(b_rsr[i]) + '\t' + str(p_rsr[i]) +'\n')


with open('RSR_estimate.dat','w') as f:
    f.write('#Wavelength,\tQER1,\tQEG1,\tQEB1,\t,QEP1,\tQER2,\tQEG2,\tQEB2,QEP2,\tScout,\tTelescope,\tQER1 RSR,\tQEG1 RSR,\tQEB1 RSR,\tQEP1 RSR\n')
    np.savetxt(f,totaldata)
