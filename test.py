import numpy as np
from simann import minimize

'''
test simulated annealing by sorting an array

'''


def stval(x):
    '''
    count the number of misplaced elements
    '''
    n = len(x)
    return sum(np.arange(n) != x)

def newstate(x):
    '''
    construct a new state by randomly swapping two elements
    '''
    y = np.array(x)

    # random swap
    n = len(y)
    i = np.random.randint(n)

    j = i
    while j == i:
        j = np.random.randint(n)

    y[i], y[j] = y[j], y[i]

    return y


if __name__ == '__main__':
    st = np.arange(10)
    np.random.shuffle(st)

    s = minimize(st, stval, newstate, maxrounds=10000)

    print(s)