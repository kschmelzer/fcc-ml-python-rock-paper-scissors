import random
import numpy as np

# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

states = ['R', 'P', 'S']
state_to_id = {val: k for (k, val) in enumerate(states)}

vector_table = np.zeros((3, 3, 3, 3, 3))


def get_choice_to_beat(theirs): 
    if theirs == 'P':
        return 'S'
    if theirs == 'S':
        return 'R'
    return 'P'

def player(prev_play, opponent_history=[]):

    if prev_play != '':
        opponent_history.append(prev_play)
    else:
        vector_table[:] = 0
        opponent_history.clear()
        

    choices = ['R', 'P', 'S']
    if (len(opponent_history) < 5):
        return random.choice(choices)

    prev_vector = opponent_history[-5:]

    # update occurrence table to track number of times opponent choose the 5th play given the previous 4 plays.
    vector_table[state_to_id[prev_vector[0]], state_to_id[prev_vector[1]], state_to_id[prev_vector[2]], state_to_id[prev_vector[3]], state_to_id[prev_vector[4]]] += 1


    prev_vector = opponent_history[-4:]

    # given previous 4 plays, guess the play the opponent most often chooses next. 
    their_most_popular = np.argmax(vector_table[state_to_id[prev_vector[0]], state_to_id[prev_vector[1]], state_to_id[prev_vector[2]], state_to_id[prev_vector[3]], :])

    their_next = states[their_most_popular]
    
    my_play = get_choice_to_beat(their_next)


    return my_play
