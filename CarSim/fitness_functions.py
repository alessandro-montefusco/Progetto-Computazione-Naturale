import math

def fitness_on_lap(lap):
    '''
    Calcolo della fitness sul singolo giro.
    :param lap: giro su cui e' calcolata la fitness
    :return: valore medio del modulo della velocita' su un singolo giro
    '''
    speed_arr = []
    for j in range(lap.speedX.__len__()):
        speed_arr.append(math.sqrt(math.pow(lap.speedX[j], 2) + math.pow(lap.speedY[j], 2) + math.pow(lap.speedZ[j], 2)))
    print("Vel max: ", max(speed_arr))
    mean_speed = sum(speed_arr) / len(speed_arr)

    return mean_speed

def speed_fitness(laps):
    '''
    Tale fitness tiene conto soltanto dell'andamento medio della velocita'. Si vuole minimizzare tale valore.
    Si tiene conto di quanti giri effettivamente vengono completati. Nel caso di giri non finiti, si penalizza
    di più questo individuo. Fitness in range [0; 1]
    :param laps: giri effettuati.
    :return: tupla contenente: valore medio della fitness sui giri completati; stringa da salvare a file.
    '''
    fit_val = 0.0
    # Caso 1: 0/2 giri completati
    if len(laps) == 0:
        penalty = 1
        str_info = "Nessun giro completato\n"
        str_lap = "-- \t--\t"

        return (penalty, str_info, str_lap)
    # Caso 2: 1/2 giri completati
    elif len(laps) == 1:
        mean_speed = fitness_on_lap(laps[0])
        score = 1/mean_speed + 0.5
        str_lap = str(laps[0].get_time()) + "\t" + "--\t"
        str_info = "Lap: " + str(1) + " - Time: " + str(laps[0].get_time()) + "\t\n"

        return (score, str_info, str_lap)
    else:
        i = 0
        str_info = ""
        str_lap = ""
        for lap in laps:
            mean_speed = fitness_on_lap(lap)
            score = 1 / mean_speed
            str_lap += str(lap.get_time()) + "\t"
            fit_val += score
            str_info = str_info + "Lap: " + str(i + 1) + " - Time: " + str(lap.get_time()) + "\t\n"
            i += 1

        return (fit_val, str_info, str_lap)

def speed_pos_fitness(laps, curr_gen, tot_gen):
    '''
    Tale fitness tiene conto dell'andamento medio della velocita' e dei fuori pista. Si vuole minimizzare tale valore.
    Per info dettagliate guardare la relazione fornita.
    Range della fitness [0,2.1]
    :param laps: giri effettuati.
    :param curr_gen: numero di generazione corrente.
    :param tot_gen: generazioni totali.
    :return: valore della fitness su tutti i giri.
    '''
    ADAPTATION_FACTOR = 1 + (curr_gen/tot_gen)
    PENALTY_BORDER = 0.05*ADAPTATION_FACTOR
    PENALTY_OFFTRACK = 0.5*ADAPTATION_FACTOR
    fit_val = 0.0
    t_border = 0.0
    t_offtrack = 0.0
    if len(laps) == 0:
        str_info = "Nessun giro completato\n"
        str_lap = "-- \t--\t"
        return (1, str_info, str_lap)
    elif len(laps) == 1:
        mean_speed = fitness_on_lap(laps[0])
        score = 1 / mean_speed + 1
        for item in laps[0].trackPos:
            if abs(item) > 0.95 and abs(item) < 1.2:
                t_border += 1
            if abs(item) > 1.2:
                t_offtrack += 1
        t_border = (t_border * 0.02 / laps[0].get_time())  # secondi/tempo_giro in cui la macchina e' sui bordi
        t_offtrack = (t_offtrack * 0.02 / laps[0].get_time())  # secondi/tempo_giro in cui la macchina e' fuori pista
        fit_val += score + (PENALTY_BORDER * t_border + PENALTY_OFFTRACK * t_offtrack)

        str_lap = str(laps[0].get_time()) + "\t" + "--\t"
        str_info = "Lap: " + str(1) + " - Time: " + str(laps[0].get_time()) + "\t\n"
    else:
        i = 0
        str_info = ""
        str_lap = ""
        for lap in laps:
            mean_speed = fitness_on_lap(lap)
            score = 1 / mean_speed
            for item in lap.trackPos:
                if abs(item) > 0.95 and abs(item) < 1.2:
                    t_border += 1
                if abs(item) > 1.2:
                    t_offtrack += 1

            t_border = (t_border*0.02 / lap.get_time()) #secondi/tempo_giro in cui la macchina e' sui bordi
            t_offtrack = (t_offtrack*0.02 / lap.get_time()) #secondi/tempo_giro in cui la macchina e' fuori pista
            fit_val += score + (PENALTY_BORDER*t_border + PENALTY_OFFTRACK*t_offtrack)
            str_lap += str(lap.get_time()) + "\t"
            str_info = str_info + "Lap: " + str(i + 1) + " - Time: " + str(lap.get_time()) + "\t\n"
            i += 1

    return (fit_val/len(laps), str_info, str_lap)



