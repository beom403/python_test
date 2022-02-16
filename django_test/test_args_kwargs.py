# positional arguments and keyword arguments

# sample
def plus(a, b, *args, **kwargs):
    print(args)
    return a + b


# positional arguments sample
def args_function(*args):
    for num in args:
        print(num)


# keyword arguments
def kwargs_function(**kwargs):

    for element in kwargs:
        print(element)
    for element in kwargs.items():
        print(element)
    for element in kwargs.values():
        print(element)


args_function(1, 2, 3, 4, 5)
kwargs_function(name = "asdf", age = "123")