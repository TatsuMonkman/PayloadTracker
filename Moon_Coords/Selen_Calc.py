#This script generates selenographic coordinates for the Earth, Sun, and spacecraft given a UTC date
#This script needs MoonMetdat.txt and its listed files to be in the same directory
#This script needs to know the TLE_SPK_OBJ_ID and SPK file of the spacecraft
#Need to double check some units...

import spiceypy as spice
import numpy as np
import math

date = "18085" #from getelm?
spacecraft = "SWIFT"
time = "March 26, 2018 16:00:00"

spice.furnsh("./MetDat/MoonMetdat.txt") #Constant for all iterations
spice.furnsh("./" + date + "_" + spacecraft + ".bsp") #SPK file made by setup, should add datetime and name to file name

#define variables

et = spice.utc2et("March 26, 2018 16:00:00")

#print et

state = spice.spkezr("-128485",et,"MOON_PA", "LT+S","Moon")
print 'Spacecraft:'
#print state[0][0:3]
#print state
selen = spice.reclat(state[0][0:3])
print selen[1]*180/math.pi
print selen[2]*180/math.pi


#print spice.kinfo("./testtle.bsp")

#print et

state = spice.spkezr("Earth",et,"MOON_PA", "LT+S","Moon")
print '\nEarth:'
#print state[0][0:3]
#print state
selen = spice.reclat(state[0][0:3])
print selen[1]*180/math.pi
print selen[2]*180/math.pi

state = spice.spkezr("Sun",et,"MOON_PA", "LT+S","Moon")
print '\nSun:'
#print state[0][0:3]
#print state
selen = spice.reclat(state[0][0:3])
print 90-selen[1]*180/math.pi
print selen[2]*180/math.pi
