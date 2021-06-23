# Numba presenation in a Jupyter notebook 

## Motivation
- Significantly speeds up performance
- Runs same code on single CPU, multiple CPUs, or GPU

## How Numba works 
- Just In Time (JIT) python compiler (compiles when function is executed)
- Generates intermediate representation (IR),
- then uses LLVM to compile and optimize code
- Does (un)boxing of Python objects

## When to use it?
- Can be used with NumPy or Python loops

## Dictionaries and Lists
- Recently Numba added experimental support for Dictionaries

## Classes
- @jitclass decorator to define classes
- these classes can be used in @njit decorated functions 

## References
[1] https://developer.nvidia.com/blog/numba-python-cuda-acceleration/

[2] https://www.youtube.com/watch?v=-4tD8kNHdXs

[3] https://numba.pydata.org/

