import sys

def loading(x):
    return sys.stdout.write("'\r'[%-20s] %d%%" % ('='*x, 5*x))