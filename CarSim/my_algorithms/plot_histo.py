import matplotlib.pyplot as plt
import numpy as np

def test_tracks():
    # tempi sul tracciato
    carsim = [233.608, 136.374, 232.884, 233.03]
    pso = [208.706, 132.316, 214.942, 207.336]
    sade = [231.960, 132.418, 229.978, 213.724]

    #tempi fuori pista
    carsim1 = [43.28,1.92,43.9,25.22]
    pso1 = [27.26,1.58,28.3,13]
    sade1 = [36.3,1.1,40.32,12.44]

    #top speed
    carsim2 = [272.63,257.16,231.75,246.08]
    pso2 = [268.73,251.76,232.35,239.38]
    sade2 = [270.21,249.52,230.26,240.038]

    # set width of bar
    barWidth = 0.25

    # Set position of bar on X axis
    r1 = np.arange(len(carsim))
    r2 = [x + barWidth for x in r1]
    r3 = [x + barWidth for x in r2]

    # Make the plot
    plt.figure(figsize=(11,5))
    plt.bar(r1, carsim1, color='black', width=barWidth, edgecolor='white', label='CarSim')
    plt.bar(r2, pso1, color='green', width=barWidth, edgecolor='white', label='PSO')
    plt.bar(r3, sade1, color='red', width=barWidth, edgecolor='white', label='SADE')

    # Add xticks on the middle of the group bars
    plt.title("Confronto fuori pista CarSim, PSO e SADE")
    plt.ylabel('Tempo fuori pista', fontweight='bold')
    plt.xlabel('Circuiti testati', fontweight='bold')
    plt.xticks([r + barWidth for r in range(len(carsim))], ['Street 1', 'CG Track 2', 'Alpine 2', 'E-Track 6'])
    plt.yticks(np.arange(0, 46, step=2))

    # Create legend & Show graphic
    plt.grid(axis='y', linewidth=0.5, color='grey', linestyle=':')
    plt.legend()
    plt.show()

def training_tracks():
    #tempi sul tracciato
    carsim = [98.53, 292.47]
    pso = [87.18, 197.72]
    sade = [87.95, 194.27]

    #fuori pista
    carsim1 = [0.88, 83.1]
    pso1 = [1.62, 0.96]
    sade1 = [1.56, 6.46]

    #top speed
    carsim2 = [226, 276]
    pso2 = [243, 276.94]
    sade2 = [243.44, 291.77]

    # set width of bar
    barWidth = 0.15

    # Set position of bar on X axis
    r1 = np.arange(len(carsim))
    r2 = [x + barWidth for x in r1]
    r3 = [x + barWidth for x in r2]

    # Make the plot
    plt.figure(figsize=(8, 5))
    plt.bar(r1, carsim2, color='black', width=barWidth, edgecolor='white', label='CarSim')
    plt.bar(r2, pso2, color='green', width=barWidth, edgecolor='white', label='PSO')
    plt.bar(r3, sade2, color='red', width=barWidth, edgecolor='white', label='SADE')

    # Add xticks on the middle of the group bars
    plt.title("Confronto top speed, PSO e SADE per la fitness " + chr(966)+"1")
    plt.ylabel('Velocità', fontweight='bold')
    plt.xlabel('Circuiti di training', fontweight='bold')
    plt.xticks([r + barWidth for r in range(len(carsim))], ['CGS 1', 'Forza'])
    #plt.yticks(np.arange(0, 90, step=5))
    plt.yticks(np.arange(0, 330, step=30))

    # Create legend & Show graphic
    plt.grid(axis='y', linewidth=0.5, color='grey', linestyle=':')
    plt.legend(loc='upper left')
    plt.show()


# stampa lettere greche
#greek_letterz = 'letter' + chr(966)
