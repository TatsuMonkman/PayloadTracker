#'com_spec' means 'combining spectra'
#This script just combines
import numpy as np
import matplotlib.pyplot as plt

soil = np.genfromtxt('62231_avg_scaled_std_text.txt')
norite = np.genfromtxt('67455_ls-CMP-10.dat')


mix = []
for i in range(len(soil)):
    mix.append([soil[i][0],(soil[i][1]*0.95)+(0.05*norite[i][1]),
                soil[i][1],norite[i][1]])

mix = np.asarray(mix)
comment =('Combined reflectance spectrum of breccia and soil samples taken'
          + 'from \nApollo 16 mission at 5% breccia and 95% lunar soil\n'
          + 'Wl (nm),\tMix,\tSoil,\tNorite')

np.savetxt('mixed_spectrum.txt', mix, fmt='%1.4f',delimiter ='\t', header = comment)

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.scatter(soil[:,0], soil[:,1], s = 10, c = 'r', marker = 'o', label = 'Soil')
ax1.plot(soil[:,0], soil[:,1], c = 'r')
ax1.scatter(soil[:,0], norite[:,1], s = 10, c = 'b', marker = 'o', label = 'Norite')
ax1.plot(soil[:,0], norite[:,1], c = 'b')
ax1.scatter(mix[:,0], mix[:,1], s = 10, c = 'm', marker = 'o', label = 'Mix')
ax1.plot(mix[:,0], mix[:,1], c = 'm')
ax1.set_yscale('log')
ax1.set_xlim([350,2500])
plt.xlabel('Wavelength (nm)')
plt.ylabel('Reflectance')
plt.legend(loc = 'lower right')
plt.title('Reflectance vs Wavelength for Apollo Samples')
plt.grid(True)
plt.show()
