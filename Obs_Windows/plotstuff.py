
def plot_2sets(o,n):
    import matplotlib.pyplot as plt
    import numpy as np

    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.scatter(n[:,2],n[:,3], s = 10, c = 'b', marker = 's')
    ax1.scatter(o[:,2],o[:,3], s = 10, c = 'y', marker = 's', label = 'Observation Window')
    ax1.scatter(o[:,8],o[:,9], s = 10, c = 'g', marker = 's', label = 'Sub-Sun Position')
    ax1.scatter(n[:,6],n[:,7], s = 10, c = 'm', marker = 's', label = 'Nonobservable Sub-Sun Position')
    ax1.scatter(o[:,6],o[:,7], s = 10, c = 'r', marker = 's', label = 'Observable Sub-Lunar Position')

#    ax1.plot(n[:,2],n[:,3], c = 'b')
#    ax1.plot(o[:,2],o[:,3], c = 'y')
#    ax1.plot(o[:,8],o[:,9], c = 'g')
#    ax1.plot(n[:,6],n[:,7], c = 'm')
#    ax1.plot(o[:,6],o[:,7], c = 'r')

    plt.xlabel('Sub Object Longitude (deg)')
    plt.ylabel('Sub Object Latitude (deg)')
    plt.legend(loc = 'lower left')
    plt.title('Observation Windows for Payload With Eclipse Preference')

    plt.grid(True)
    plt.show()

#plot_2sets(obs,nobs)

def plot_allset_rt(a):
    import matplotlib.pyplot as plt
    import numpy as np

    with open('obs_times.txt','r') as f:
        obs = np.loadtxt(f)
    with open('noobs_times.txt', 'r') as f:
        nobs = np.loadtxt(f)
    with open('all_times.txt', 'r') as f:
        aobs = np.loadtxt(f)

    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    for i in range(len(a)):
        if a[i,0] == 0:
            ax1.scatter(a[i,8],a[i,9], s = 10, c = 'g', marker = 's', label = 'Sub-Sun Position')
            ax1.scatter(a[i,2],a[i,3], s = 10, c = 'b', marker = 's', label = 'Nonobservable Sat-Position')
            ax1.scatter(a[i,6],a[i,7], s = 10, c = 'm', marker = 's', label = 'Nonobservable Sub-Lunar Position')
        elif a[i,1] == 1:
            ax1.scatter(a[i,8],a[i,9], s = 10, c = 'g', marker = 's', label = 'Sub-Sun Position')
            ax1.scatter(a[i,2],a[i,3], s = 10, c = 'y', marker = 's', label = 'Observation Window')
            ax1.scatter(a[i,6],a[i,7], s = 10, c = 'r', marker = 's', label = ' Sub-Lunar Position')
        plt.pause(0.05)

    plt.xlabel('Sub Object Longitude (deg)')
    plt.ylabel('Sub Object Latitude (deg)')
    plt.legend(loc = 'lower left')
    plt.title('Observation Windows for Payload With Eclipse Preference')

    plt.grid(True)
    plt.show()

#plot_allset_rt(aobs)
