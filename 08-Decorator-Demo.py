from time import time

def time_this(func):
    def wrapper():
        start_time = time()
        result = func()
        end_time = time()
        elapsed_time = end_time - start_time
        print(f"--> {func.__name__} ran in {elapsed_time:.4f} seconds")
        return result
    return wrapper

@time_this
def example_function():
    for i in range(1000):
        i = 2 + 2 ** i - 2 * i 

example_function()
