aTup = ('I', 'am', 'a', 'test', 'tuple')


def oddTuples(aTup):
    """
    aTup: a tuple

    returns: tuple, every other element of aTup.
    """
    # Your Code Here
    return aTup[::2]

print(oddTuples(aTup))