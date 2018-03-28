#Lunar Disk Irradiance Calculator

def disk_eradiance(date, o_slon, o_slat, s_slat):

    #Here we go...
    import math
    import datetime
    from PyAstronomy import pyasl

    #Determine Lunar Phase
    day_date = date / (3600*24)
    mp = pyasl.moonphase(day_date) #date in Julian Date days past epoch
#    print mp[0]*180
    mp = -51.03/180 #test value from USGS presentation

    #Lunar model constants
    c1 = 0.00034115
    c2 = -0.0013425
    c3 = 0.00095906
    c4 = 0.00066229
    p1 = 4.06054
    p2 = 12.8802
    p3 = -30.5858
    p4 = 16.7492

    slines = []
    with open('LIMCOEFF_Test.txt', 'r') as f:
        slines = f.readlines()
    for i in range(len(slines)):
        slines[i] = slines[i].split('\t')

#    print slines[5]
    i = 31 #Which wavelength row

    #Spectral Coefficients
    wl = 350 #Wavelength (nm)
    a0 = float(slines[i][1]) # 1, Constant
    a1 = float(slines[i][2]) # g, Phase 1 (rad^-1)
    a2 = float(slines[i][3]) # g2, Phase 2 (rad^-2)
    a3 = float(slines[i][4]) # g3, Phase 3 (rad^-3)
    b1 = float(slines[i][5]) # Phi, SunLon 1 (rad^-1)
    b2 = float(slines[i][6]) # Phi3, SunLon 3 (rad^-3)
    b3 = float(slines[i][7]) # Phi5, SunLon 5 (rad^-5)
    d1 = float(slines[i][8]) # e^(-g/p1), Exponent 1
    d2 = float(slines[i][9]) # e^(-g/p2), Exponent 2
    d3 = float(slines[i][10]) # cos[(g-p3)/p4], Exponent 3

    #Variables
    g = mp #Absolute phase angle
    theta = o_slat * math.pi / (180 ) #selenographic latitude of sub-observer point, degs to rads
    phi = o_slon * math.pi / (180 ) #Selenographic longitude of sub-observer point, degs to rads
    PHI = s_slat * math.pi / (180 ) #Selenographic longitude of the Sun, degs to rads

    def diskequiv(C1, C2, C3, C4, P1, P2, P3, P4, WL, A0,
                  A1, A2, A3, B1, B2, B3, D1, D2, D3, G,
                  THETA, PHi, SUNPHI):

                  asum = A0 + A1*G + A2*(G**2) + A3*(G**3)
                  bsum = B1*SUNPHI + B2*(SUNPHI**3) + B3*(SUNPHI**5)
                  csum = C1*THETA + C2*PHi + C3*SUNPHI*THETA + C4*SUNPHI*PHi
                  dsum = D1*math.exp(-G/P1) + D2*math.exp(-G/P2) + D3*math.cos((G-P3)/P4)

                  return float(asum + bsum + csum + dsum)

    AK = diskequiv(c1, c2, c3, c4, p1, p2, p3, p4, wl, a0,
                             a1, a2, a3, b1, b2, b3, d1, d2, d3, g,
                             theta, phi, PHI)
    print AK
    print math.exp(AK)

    return

disk_eradiance(575372835.433, 4.328, 5.159, 1.488)
