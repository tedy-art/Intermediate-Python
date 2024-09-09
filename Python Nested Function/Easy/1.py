"""
Write a function outer() that contains another function inner()
 and prints a message from the inner function.
"""


def greetings(name):
    def inner_func():
        print(f'Hello my name is {name}.')

    return inner_func()


# calling the outer function
greetings("Tejas")
