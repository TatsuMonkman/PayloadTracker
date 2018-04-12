
def clear(name,date,results,trap_results):
    import subprocess

    subprocess.call('mv ROLO_Results.dat ./history/' + name
                    + '_' + str(date)[:8] + '_ROLO_Results.dat', shell = True)

    subprocess.call('mv trapazoid_ROLO_Results.dat ./history/' + name
                    + '_' + str(date)[:8] + '_trapazoid_ROLO_Results.dat',
                    shell = True)

    subprocess.call('mv r_AkSolRSR_combined_spectrum.dat ./history/' + name
                    + '_' + str(date)[:8] + '_r_AkSolRSR_combined_spectrum.dat',
                    shell = True)
    subprocess.call('mv g_AkSolRSR_combined_spectrum.dat ./history/' + name
                    + '_' + str(date)[:8] + '_g_AkSolRSR_combined_spectrum.dat',
                    shell = True)
    subprocess.call('mv b_AkSolRSR_combined_spectrum.dat ./history/' + name
                    + '_' + str(date)[:8] + '_b_AkSolRSR_combined_spectrum.dat',
                    shell = True)
    subprocess.call('mv p_AkSolRSR_combined_spectrum.dat ./history/' + name
                    + '_' + str(date)[:8] + '_p_AkSolRSR_combined_spectrum.dat',
                    shell = True)

    t = 'trapazoid_'

    subprocess.call('mv ' + t + 'r_AkSolRSR_combined_spectrum.dat ./history/' + name
                    + '_' + str(date)[:8] + '_' + t + '_r_AkSolRSR_combined_spectrum.dat',
                    shell = True)
    subprocess.call('mv ' + t + 'g_AkSolRSR_combined_spectrum.dat ./history/' + name
                    + '_' + str(date)[:8] + '_' + t + '_g_AkSolRSR_combined_spectrum.dat',
                    shell = True)
    subprocess.call('mv ' + t + 'b_AkSolRSR_combined_spectrum.dat ./history/' + name
                    + '_' + str(date)[:8] + '_' + t + '_b_AkSolRSR_combined_spectrum.dat',
                    shell = True)
    subprocess.call('mv ' + t + 'p_AkSolRSR_combined_spectrum.dat ./history/' + name
                    + '_' + str(date)[:8] + '_' + t +  '_p_AkSolRSR_combined_spectrum.dat',
                    shell = True)
