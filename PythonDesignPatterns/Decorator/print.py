from functools import wraps

def hello_decorator(function):
    @wraps(function)
    def decorator():
        result =  function()
        return 'this is ' + result + ' decorated'
    return decorator

@hello_decorator
def hello_world():
    return 'Hello World'

print(hello_world())