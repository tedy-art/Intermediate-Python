"""
Write a function greet(name) that contains an inner function say_hello() and
prints "Hello" followed by the name.
"""


def greet(name):
    def say_hello():
        print(f'Hello, {name}!')

    return say_hello()


# calling
greet('Tejas')
greet('Lorry')
greet('john')
greet('ronny')
