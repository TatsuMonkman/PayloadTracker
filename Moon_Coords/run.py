def derive_Selencoords(tlefile):
    import Check_tle
    import Create_SPK
    import Selen_Calc
    import clean

    #Add tle file to cwd and enter name below
    tle = tlefile

    setup = Check_tle.makesetup(tle)
    #setup looks like [setn, setn + '_setup.txt', setn + '.bsp']

    Create_SPK.mkspk(setup[1])

    a = Selen_Calc.Calculate_SCoords(setup[0])

    print a

    clean.clear(setup, tle)

    return a

derive_Selencoords('testtle.tle')
