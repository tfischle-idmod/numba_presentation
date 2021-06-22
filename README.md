# numba

# Motivation
- Python is nimble and flexible
- great language for quick prototyping and complete systems
- Mix types
- but its flexibility, and typeless, high-level syntax can result in poor performance

Performance
- Tried "@jit" did not speed up execution
- numpy was the way to go
- Looked into how to write fast code
- hardware cache, memory access, memory layout
- Basically the takeway is we cannot write fast code and use flexible (Python) data structures like lists, dicts

But, how often do we write code like:
d = {"first": 1, "second": "two"}
or
l = [1]
l.append["two"]

i.e. mixing datatypes


## What is numba, how does it work?
### Numba Website
- Python compiler
- CUDA-capable GPUs or
- multicore CPU
- How can numba do this?
- jit
- etc.
- idea is speed up on function by function basis especially math code
- It doesn't generate C-code

- Jit python compiler
- Taking bytecode of the function
- What does your code do what are the data types
- Intermediate representation 

- optimixinz and code generation by llvm compiler
- for different hardware
- llvm backend
- code is cached

unboxing: strip of python bits
swap in fast numba function for Builtin or function (numba can be compiled to fast machine code)
spotting things and putting in an implementation that can be compiled

compiler does
- loop unrolling
- inlining
- etc.


(re)boxing
- translating it back into Python land (interpreter)


https://www.youtube.com/watch?v=-4tD8kNHdXs




## When to use it?
- Calculations with NumPy arrays can be speeded up 
- What kind of code can we accelerate?
	- LLVM
		- needs defined data types
	- examples:
		- numpy dicts and lists
		- 
- Creating ufuncs, gufuncs? 
- easy GPU access
- no parallelization
	- run sims in parallel anyway, only add overhead
	- parallelization is challanging e.g. race conditions


## When does it work?
- nummerically orientated
- code uses loops
- Works great with numpy arrays
- doesn't work with 3rd party packages like pandas





# References
[1] https://developer.nvidia.com/blog/numba-python-cuda-acceleration/
[2] https://www.youtube.com/watch?v=-4tD8kNHdXs