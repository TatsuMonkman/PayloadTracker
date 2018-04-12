def run(a, xmin, xmax):
    #Run ROLO over all wavelengths for observation date, selenographic
    #coordinates. Values in lunar are assigned as follows with long and lat
    #in selenographic coordinates:
    import numpy as np
    import subprocess
    import math
    from DiskE_Ref import lunar
    from com_sol_rsr import combine_spectra
    from integration import make_traps, trap_integrate, trap_file
    from clean import clear
    from plotspectra import plot_sets


    #This script runs ROLO over all ROLO wavelengths using lunar
    #Saves results to ROLO_Results.txt
    #lunar(date(JD seconds), observer sublongitude (deg),
    #observer sublatitude (deg), sun sublongitude(deg), ROLO wavelength band)
    model    = []
    name = a[0]
    date = a[1]
    sat_long = a[2][1]*180/math.pi
    sat_lat  = a[2][2]*180/math.pi
    sun_long = (90 - a[4][1]*180)/math.pi
    print sat_long
    print sat_lat
    print sun_long

    for j in range(4,36):
        model.append(lunar(date, sat_long, sat_lat, sun_long, j))
    m3 = np.asarray(model)
    with open('ROLO_Results.dat','w') as f:
        f.write('#Disk Reflectance Results\n#Wavelength\t\tReflectance\n')
        np.savetxt(f, m3, fmt='%4f')

    #Integrate ROLO model results over desired wavelength range
    ref_file = 'ROLO_Results.dat'
    trap_file(ref_file, 'trapazoid_' + ref_file, 0, 1)
    area = trap_integrate('trapazoid_' + ref_file, xmin, xmax)

    #Combine (multiply) ROLO model results with the combined
    #solar-rsr spectrum for each band
    combine_spectra('trapazoid_' + ref_file,
                    './rsr_spectrums/trapazoid_r_combined_spectrum.dat',
                    'r_AkSolRSR_')
    trap_file('r_AkSolRSR_combined_spectrum.dat',
              'trapazoid_r_AkSolRSR_combined_spectrum.dat',0,1)
    combine_spectra('trapazoid_' + ref_file,
                    './rsr_spectrums/trapazoid_g_combined_spectrum.dat',
                    'g_AkSolRSR_')
    trap_file('g_AkSolRSR_combined_spectrum.dat',
              'trapazoid_g_AkSolRSR_combined_spectrum.dat',0,1)
    combine_spectra('trapazoid_' + ref_file,
                    './rsr_spectrums/trapazoid_b_combined_spectrum.dat',
                    'b_AkSolRSR_')
    trap_file('b_AkSolRSR_combined_spectrum.dat',
              'trapazoid_b_AkSolRSR_combined_spectrum.dat',0,1)
    combine_spectra('trapazoid_' + ref_file,
                    './rsr_spectrums/trapazoid_p_combined_spectrum.dat',
                    'p_AkSolRSR_')
    trap_file('p_AkSolRSR_combined_spectrum.dat',
              'trapazoid_p_AkSolRSR_combined_spectrum.dat',0,1)


    #Calculate the integrated Satellite RSR over specified bands
    rRSR = trap_integrate('./rsr_spectrums/trapazoid_r_RSR_estimate.dat',
                          xmin, xmax)
    gRSR = trap_integrate('./rsr_spectrums/trapazoid_g_RSR_estimate.dat',
                          xmin, xmax)
    bRSR = trap_integrate('./rsr_spectrums/trapazoid_b_RSR_estimate.dat',
                          xmin, xmax)
    pRSR = trap_integrate('./rsr_spectrums/trapazoid_p_RSR_estimate.dat',
                          xmin, xmax)
    rcom = trap_integrate('trapazoid_r_AkSolRSR_combined_spectrum.dat',
                          xmin, xmax)
    gcom = trap_integrate('trapazoid_g_AkSolRSR_combined_spectrum.dat',
                          xmin, xmax)
    bcom = trap_integrate('trapazoid_b_AkSolRSR_combined_spectrum.dat',
                          xmin, xmax)
    pcom = trap_integrate('trapazoid_p_AkSolRSR_combined_spectrum.dat',
                          xmin, xmax)

    print rcom, gcom, bcom, pcom

    #Convert effective disk reflectance to irradiance
    #Ik = Ak*OmegaM*Ek/pi
    OmegaM = 6.4177*(10**-5)
    AkEk = np.asarray([rcom/rRSR,gcom/gRSR,bcom/bRSR,pcom/pRSR])
    Ik = OmegaM*AkEk/math.pi

    #Add in distance correction
    #1 Astronomical Unit (km)
    AU  = 149597870.700
    #Literature Sun-Moon distance (km)
    DSM = a[4][0]
    #Observer-Moon distance (km)
    DOM = a[2][0]
    #Literature Earth-Moon distance (km)
    DEM = 384400.
    #Distance correction factor
    Fd = ((DSM/AU)**2)*((DOM/DEM)**2)
    #At detector Irradiance
    I = Ik*Fd*10**6

    print'At detector irradiance: ',I[:],'microW/(m**2)'

    with open('trapazoid_r_AkSolRSR_combined_spectrum.dat','r') as f:
        r_trap = np.genfromtxt(f)

    with open('trapazoid_b_AkSolRSR_combined_spectrum.dat','r') as f:
        b_trap = np.genfromtxt(f)

    with open('trapazoid_g_AkSolRSR_combined_spectrum.dat','r') as f:
        g_trap = np.genfromtxt(f)

    with open('trapazoid_p_AkSolRSR_combined_spectrum.dat','r') as f:
        p_trap = np.genfromtxt(f)

    with open('trapazoid_ROLO_Results.dat', 'r') as f:
        ROLO_trap = np.genfromtxt(f)

    plot_sets(r_trap,b_trap,g_trap,p_trap,ROLO_trap)

    clear(name, date, ref_file, 'trapazoid_' + ref_file)

    return I

#a = ['SWIFT', JD (seconds past J2000),
#     (Observer-Moon distance, Satellite sub-long, Satellite sub-lat),
#     (Earth-Moon distance, Earth sub-long, Earth sub-lat),
#     (Sun-Moon distance, Sun sub-long, Sun sub-lat)]
a = ['SWIFT', 575372835.433,
     (375596.1103675459, 0.014740347874767908, 0.019861289528241136),
     (369086.03386759775, 0.010256408131108879, 0.015251407741792608),
     (149433273.59575933, 1.0591410064895943, -0.021307684847200876)]

run(a,375,750)
#print run(0, 7, 0, 0, 7, 450, 750)
