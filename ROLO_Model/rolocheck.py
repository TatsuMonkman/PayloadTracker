import matplotlib.pyplot as plt
import numpy as np

myrolo = np.genfromtxt('ROLO_Results.txt')
Stonerolo = np.genfromtxt('Stone_ROLO_results.dat')

diffrolo = [myrolo[:,0]/Stonerolo[:,0], myrolo[:,1]/(Stonerolo[:,1]/Stonerolo[:,2])]

###############################################################################
###############################################################################
#########################REVIEW STONE'S ROLO DATA##############################
btest = []
atest = []

for i in range(len(Stonerolo) - 1):
    b = (Stonerolo[i+1][2]-Stonerolo[i][2])/(Stonerolo[i+1][0]-Stonerolo[i][0])
    btest.append([Stonerolo[i][0],b])

btest = np.asarray(btest)
print('b mean: ', np.mean(btest, axis=0)[1])

for i in range(len(Stonerolo) - 1):
    a =(Stonerolo[i][2] + Stonerolo[i+1][2]
        - btest[i][1]*(Stonerolo[i][0]+Stonerolo[i+1][0]))
    atest.append([Stonerolo[i][0],a])

atest = np.asarray(atest)
print('a mean: ', np.mean(atest, axis=0)[1])
print('A\'/A mean: ', np.mean(Stonerolo, axis=0)[2])

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.scatter(btest[:,0], btest[:,1], s = 10, c = 'b', marker = 'o')
ax1.plot(btest[:,0], btest[:,1], c = 'b')
for i, j in zip(btest[:,0],btest[:,1]):
    ax1.annotate(str(j)[0:8], xy=(i,j))
plt.xlabel('Wavelength (nm)')
plt.ylabel('Scaling Coefficient b')
plt.legend(loc = 'lower right')
plt.title('Scaling Coefficient b vs Wavelength')
plt.grid(True)
#plt.show()

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.scatter(atest[:,0], atest[:,1], s = 10, c = 'b', marker = 'o')
ax1.plot(atest[:,0], atest[:,1], c = 'b')
for i, j in zip(atest[:,0],atest[:,1]):
    ax1.annotate(str(j)[0:8], xy=(i,j))
plt.xlabel('Wavelength (nm)')
plt.ylabel('Scaling Coefficient a')
plt.legend(loc = 'lower right')
plt.title('Scaling Coefficient b vs Wavelength')
plt.grid(True)
#plt.show()

fig = plt.figure()
ax2 = fig.add_subplot(111)
ax2.scatter(Stonerolo[:,0], Stonerolo[:,2], s = 10, c = 'b', marker = 'o')
ax2.plot(Stonerolo[:,0], Stonerolo[:,2], c = 'b')
for i, j in zip(Stonerolo[:,0],Stonerolo[:,2]):
    ax2.annotate(str(j)[0:8], xy=(i,j))
plt.xlabel('Wavelength (nm)')
plt.ylabel('Scaling Coefficient A\'/A = (a+blam)')
plt.legend(loc = 'lower right')
plt.title('A\'/A vs Wavelength for Apollo Samples')
plt.grid(True)
#plt.show()

###############################################################################
###############################################################################
#######################FIND CONVERGING a, b, A'/A VALUES#######################

#These two arrays *should* be the same length
myrolo = np.genfromtxt('ROLO_Results.txt')
stonerolo = np.genfromtxt('Stone_ROLO_results.dat')

A = np.arange(-10,10,0.0005, dtype=np.float)
B = np.arange(-0.005, 0.005, 0.000005, dtype=np.float)

def s_factor(a,b):
    f = 0
    for i in range(len(myrolo)):
        Ar = stonerolo[i][1]/stonerolo[i][2]
        AR = myrolo[i][1]
        lam = stonerolo[i][0]
        f += (1./32.)*Ar*(a + b*lam)/(AR)
    return f

C = []

for i in range(len(A)):
    x = abs(s_factor(A[i],B))-1
    C.append(x)
    print x
C = np.asarray(C)

fig = plt.figure()
ax1 = fig.add_subplot(111)
plt.imshow(C, cmap='viridis')
plt.show()

print np.amin(C)
