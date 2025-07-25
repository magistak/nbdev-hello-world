"""This is a test page that export to the hello module."""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_hello.ipynb.

# %% auto 0
__all__ = ['hello', 'say_hello']

# %% ../nbs/00_hello.ipynb 3
def hello(): 
    """Say hello!"""
    print("Hello world!")

# %% ../nbs/00_hello.ipynb 4
def say_hello(to):
    "Say hello to somebody!"
    return f'Hello {to}!'
