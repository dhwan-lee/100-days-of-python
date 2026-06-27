# from flask import Flask
# app = Flask(__name__)
# print(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

# if __name__ == "__main__":
#     app.run()

# def outer_function():
#     print("I'm outer")

#     def nested_function():
#         print("I'm inner")

#     return nested_function

# inner_function = outer_function()   # print "I'm outer"
# inner_function() # print "I'm inner"

## Python Decorator
from time import sleep

def delay_decorator(function):
    def wrapper_function():
        # Do something before
        function()
        function()
        # Do something after
    return wrapper_function

@delay_decorator
def say_hello():
    sleep(2)
    print("Hello")

@delay_decorator
def say_bye():
    print("Bye")

def say_greeting():
    print("How are you?")

decorator_function = delay_decorator(say_greeting)
decorator_function()