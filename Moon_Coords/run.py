import Check_tle
import Create_SPK
import Selen_Calc
import clean

tle = 'testtle.tle'

setup = Check_tle.makesetup(tle)
#setup looks like [setn, setn + '_setup.txt', setn + '.bsp']

Create_SPK.mkspk(setup[1])

Selen_Calc.Calculate_SCoords(setup[0])

clean.clear(setup, tle)
