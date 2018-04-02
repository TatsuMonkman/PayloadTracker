

def clear(dat, tle):
    #set looks like [setn, setn + '_setup.txt', setn + '.bsp']
    import subprocess

    subprocess.call('mv ' + tle + ' ./history/' + dat[0]
                    + '.tle', shell = True)
    subprocess.call('mv ' + dat[1] + ' ./history/', shell = True)
    subprocess.call('mv ' + dat[2] + ' ./history/', shell = True)
    subprocess.call('mv ' + dat[0] + '_spoints.txt '
                    + './history/', shell = True)
