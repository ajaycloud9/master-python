# Generators
# Generators are functions that allow you to generate a sequence of values dynamically, 
# one at a time, rather than generating all values at once and storing them in memory. 
# They are particularly useful when dealing with large datasets or infinite sequences.

# How Generators Work:
# Using yield Statement: Generators are defined using a yield statement instead of return.
# State Preservation: When a generator function is called, it returns a generator object. The state of the generator is preserved between successive calls to next() or when used in a loop.
# Lazy Evaluation: Values are generated on-demand, as needed, conserving memory.

def count_up_to(limit):
    count = 1
    while count <= limit:
        yield count
        count += 1

counter = count_up_to(5)
print(next(counter))  # Output: 1
print(next(counter))  # Output: 2
print(next(counter))  # Output: 3


# Decorators
# Decorators are functions that modify the behavior of another function or method. 
# They allow you to wrap another function and execute code before and/or after the wrapped 
# function runs. Decorators are commonly used for logging, authentication, memoization, and more.

# How Decorators Work:
# Function Wrapping: Decorators wrap other functions or methods.
# Closure: Decorator functions typically take a function as an argument, 
# create a nested function (closure) that modifies the behavior of the original function, 
# and return the modified function.
# Symbol @ Syntax: Decorators can be applied using the @decorator_name syntax above the function definition.

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Logging: Calling {func.__name__} with args {args} and kwargs {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@logger
def add(a, b):
    return a + b

print(add(2, 3))  # Output: Logging: Calling add with args (2, 3) and kwargs {} \n 5
