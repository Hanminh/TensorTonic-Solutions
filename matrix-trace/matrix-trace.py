import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    # Write code here
    trace_A = 0.0
    d = len(A)
    # A = np.ndarray(A)
    for id in range(0, d):
        trace_A += A[id][id]
    return trace_A
    # pass
