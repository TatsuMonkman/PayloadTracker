
def mkspk(setup_file):
    import subprocess

    print './mkspk -setup ' + setup_file
    subprocess.call(['./mkspk -setup ' + setup_file], shell = True)

    return
