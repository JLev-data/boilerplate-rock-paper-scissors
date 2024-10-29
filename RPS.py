# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

import random

def make_combinaisons(possibilities,lenght):
    if lenght == 1:
        return possibilities
    else:
        combinaisons_list = []
        for i in possibilities:
            for j in make_combinaisons(possibilities,lenght-1):
                combinaisons_list.append(i+j)

    return combinaisons_list



def player(prev_play, opponent_history=[]):
  #  random.seed(0)
    opponent_history.append(prev_play)
    possibilities = ['R', 'P', 'S']

    n_prev = 2

    if len(opponent_history) < n_prev+1+1:  # opponent_history include one ''
        return random.choice(possibilities)

    last_play = "".join(opponent_history)[-100:]

    possibilities_dict = {key: val for val, key in enumerate(possibilities)}
    n_pos = len(possibilities)
    combinaisons_dict = {key: val for val, key in enumerate(make_combinaisons(possibilities,n_prev))}

    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}

    Q_opponent = [ [[0] * n_pos for _ in range(n_pos ** 2)] for _ in range(n_pos ** n_prev)]
    
    previous_guess = random.choice(possibilities)
    for idx in range(n_prev,len(last_play)-n_prev):
        play = last_play[idx:idx+n_prev]
        next_play = last_play[idx+n_prev]
        ideal_guess = ideal_response[next_play]

        Q_opponent[combinaisons_dict[play]][possibilities_dict[previous_guess]][possibilities_dict[ideal_guess]] += 1

        pred_opponent = Q_opponent[combinaisons_dict[play]][possibilities_dict[previous_guess]]
        real_guess = possibilities[pred_opponent.index(max(pred_opponent))]

        if real_guess != ideal_guess:
            Q_opponent[combinaisons_dict[play]][possibilities_dict[previous_guess]][possibilities_dict[real_guess]] -= 0.5

        previous_guess = str(real_guess)


    play = last_play[-n_prev:]
    pred_opponent = Q_opponent[combinaisons_dict[play]][possibilities_dict[previous_guess]]
    guess = possibilities[pred_opponent.index(max(pred_opponent))]


    return guess
