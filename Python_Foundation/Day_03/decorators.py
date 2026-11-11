def my_decorator(original_function):
    def wrapper():
        print("Before execution")
        original_function()
        print("After execution")
    return wrapper

@my_decorator
def greet():print("Welcome to Python")
greet()