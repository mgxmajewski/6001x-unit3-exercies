def biggest(aDict):
    """
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    """
    best = 0
    counter = 0
    biggest = ""
    for key in aDict:
        counter = len(aDict[key])
        if counter > best:
            best = counter
            biggest = key
    return biggest


print(biggest({'b': [1, 7, 5, 4, 3, 18, 10, 0], 'a': [1]}))