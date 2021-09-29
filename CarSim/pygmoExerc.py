import pygmo as pg
import numpy as np
import matplotlib.pyplot as plt


n_trials = 2
p_size = 10
n_gens = 50
D = 5

pg.set_global_rng_seed(seed=32)

# The user-defined problem
udp = pg.rastrigin(dim=D)
# The pygmo problem
prob = pg.problem(udp)
shift = np.linspace(np.pi*4, np.pi*4, D)
prob1 = pg.translate(prob=prob, translation=shift)

# For a number of generation based algorithms we can use a similar script to run and average over 25 runs.
udas = [pg.sade(gen=n_gens, variant=6, variant_adptv=1, memory=False, seed=1234)]
        #pg.de(gen=n_gens, variant=7, F=0.6, CR=0.9, seed=1234),
        #pg.pso(gen=n_gens, neighb_type=4, memory=True, seed=1234)]

global_results = []
for uda in udas:
    logs = []
    algo = pg.algorithm(uda)
    results_trial = []
    for i in range(0,n_trials):
        log_trial = []
        # regulates both screen and log verbosity
        algo.set_verbosity(9)
        pop = pg.population(prob, p_size)
        algo.evolve(pop)
        log_trial.append(algo.extract(type(uda)).get_log())
        log_trial = np.array(log_trial)
        results_trial.append(np.min(log_trial[:, log_trial.shape[1] - 1, 2]))
    logs.append(algo.extract(type(uda)).get_log())
    logs = np.array(logs)
    avg_log = np.average(logs, 0)
    global_results.append(np.min(results_trial,0))
    plt.plot(avg_log[:, 1], avg_log[:, 2], label=algo.get_name())

print(global_results)

# We then add details to the plot
plt.legend()
plt.grid()
plt.show()