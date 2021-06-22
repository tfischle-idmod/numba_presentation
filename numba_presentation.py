def sum_all(A):
    """Naive sum of elements of an array... assumes one dimensional array of floats"""
    acc = 0.0
    for i in xrange(A.shape[0]):
        acc += A[i]
    return acc