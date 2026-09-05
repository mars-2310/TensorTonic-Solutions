import numpy as np

def manhattan_distance(x: list, y: list) -> float:
    """
    Returns the Manhattan distance as a Python float.
    """
    # Write code here
    x = np.asarray(x)
    y = np.asarray(y)
    sum = 0.0
    for i in range(len(x)):
        sum += abs(y[i] - x[i])
    return sum
    pass