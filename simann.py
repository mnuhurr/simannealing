'''
simulated annealing

'''

import numpy as np

def minimize(start_state, fstateval, fnewstate, maxrounds=10000, temp_update_interval=5, temp_update_factor=0.99):
    '''

    :param start_state: start state object
    :param fstateval: function to compute the state value, e.g. val = fstateval(state)
    :param fnewstate: function to generate a new state, e.g. new_state = fnewstate(state)
    :param maxrounds: number of maximum rounds
    :param temp_update_interval: number of rounds between temperature update
    :param temp_update_factor: temperature updating
    :return: found state
    '''

    state = start_state
    v = fstateval(state)

    vbest = v

    # is this a good heuristic for picking the initial temperature
    temp = np.abs(v)

    loop = True

    rnum = 0
    temp_update = 0


    while loop:
        rnum += 1

        new_state = fnewstate(state)
        vnew = fstateval(new_state)

        #print('round:', rnum, ' val:', v, ' new val:', vnew)

        if vnew <= v:
            # new state is better
            v = vnew
            state = new_state

        else:
            th = np.exp((v - vnew) / temp)

            if np.random.random() < th:
                v = vnew
                state = new_state

        if rnum >= maxrounds:
            break

        if rnum - temp_update >= temp_update_interval:
            # update temperature
            temp *= temp_update_factor
            temp_update = rnum
            #print('temp update')

    return state


