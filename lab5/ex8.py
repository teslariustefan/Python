def print_arguments(function):
    def inner(*args, **kwargs):
        print("Arguments: ", args)
        print("Keyword arguments: ", kwargs)
        return function(*args, **kwargs)
    return inner

def multiply_by_two(x):
    return x * 2

def add_numbers(a, b):
    return a + b

augmented_multiply_by_two = print_arguments(multiply_by_two)
x = augmented_multiply_by_two(10)  # this will print: Arguments are: (10,), {} and will return 20.

augmented_add_numbers = print_arguments(add_numbers)
x = augmented_add_numbers(3, 4)  # this will print: Arguments are: (3, 4), {} and will return 7.

print("----------------------------------")

def multiply_output(function):
    def inner(*args, **kwargs):
        return function(*args, **kwargs) * 2
    return inner

def multiply_by_three(x):
    return x * 3

augmented_multiply_by_three = multiply_output(multiply_by_three)
x = augmented_multiply_by_three(10)  # this will return 2 * (10 * 3)
print(x)

print("----------------------------------")

def augment_function(function, decorators):
    for decorator in decorators:
        function = decorator(function)
    return function

decorated_function = augment_function(add_numbers, [print_arguments, multiply_output]) 

x = decorated_function(3, 4)  # this will print: Arguments are: (3, 4), {} and will return (2 * (3 + 4))
print(x)