animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def how_many(aDict):
    """
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    """
    all_values = 0
    for value in aDict.values():
        all_values +=len(value)
    return all_values

print(how_many(animals))