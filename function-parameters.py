# Positional arguments, keyword arguments
def complicated_function(x, y, z):      # Parameters
    print('Keyword arguments: ', x, y)
    pass

complicated_function(1, z = 2, y = 1)   # Arguments - If assigning varaibles, position not enforced
                                        # Positional argument MUST come first

# Optional parameters
def other_function(x, y = 5, z = None):
    print('Optional parameters: ', x, y, z)
    pass

other_function(1)

# Args and Kwargs
def args_and_kwargs(*args, **kwargs):
    print('Args and Kwargs: ', args, kwargs)
    pass

args_and_kwargs(1, 2, 3, x = 1, s = "hello", b = True)

# Decomposed positional arguments

def decompose(a, b, c = True, d = False):
    print('Decomposed: ', a, b, c, d)
    pass

decompose(*[1, 2], **{"c": "hello", "d": "cool"})