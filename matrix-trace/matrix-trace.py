import numpy as np

def matrix_trace(A: list) -> float:
    """
    Returns the trace as a float.
    """
    # Write code here
    n = len(A)
    tr = 0
    for i in range(0, n):
        tr += A[i][i]
    return float(tr)
    pass
    