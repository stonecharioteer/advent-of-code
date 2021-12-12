from functools import wraps


def debug(f):
    """Decorator that prints out the arguments and kw-arguments of a function"""
    @wraps(f)
    def inner_function(*args, **kwargs):
        print("*"*10)
        for argument in args:
            if isinstance(argument, list):
                if isinstance(argument[0], list):
                    # this must be a matrix:
                    print("r", list(range(len(argument[0]))))
                    for r, row in enumerate(argument):
                        print(r, row)
                else:
                    print(argument)
            else:
                print(argument)
        for kw in kwargs:
            print(f"{kw} = {kwargs[kw]}")
        result = f(*args, **kwargs)
        print(result)
        print("*"*10)
        return result
    return inner_function
