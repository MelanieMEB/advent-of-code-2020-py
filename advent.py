import operator

def read_files(filename):
    return open(filename,'r').read().split('\n')

def multiply(array):
    return reduce(operator.mul, array, 1)
