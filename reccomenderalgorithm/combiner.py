def minLength(inputs):
    """
    Finds the smallest value in a list of numbers
    Parameters
    inputs: List of integers
    Returns
    Integers
    """
    return min(inputs)


def minAge(inputs):
    """
    Find the oldest age from all preferences
    Parameters
    inputs: List of integers
    Returns
    Integers
    """
    return max(inputs)


def commonLanguages(inputs):
    """
    Finds the common languages from the user preferences
    If there are no common language then all the languages are returned. 
    Parameters:
    inputs: 2d array of with each sub array containing a list of languagues
    Returns
    list of lanaguages
    """
    commonlanguagues = list(set.intersection(*map(set, inputs)))

    if len(commonlanguagues) == 0:
        output = []
        for i in inputs:
            output = output + i
        return list(set(output))
    else:
        return commonlanguagues


def combineList(inputs):
    """
    Combines a list of strings in a 2d array then gets rid of duplicates
    Parameters
    inputs: 2d list of strings
    Returns
    List of stings in 1d array
    """
    biglist = []
    for i in inputs:
        for j in range(len(i)):
            biglist.append(i[j])

    return list(set(biglist))


def mergePreferences(datainput):
    """
    Takes 2d array of different user preferences and combines them
    Parameters
    datainput: List of all users preferences each stored in a sub array
    Returns
    Combined list of preferences in 1d array
    """
    lengths = []
    ages = []
    languages = []
    orgincountries = []
    likedgenres = []
    dislikedgenres = []
    likedtvshows = []
    dislikedtvshows = []
    for i in datainput:
        for j in range(0, len(i)):
            if j == 0:
                lengths.append(i[j])
            elif j == 1:
                ages.append(i[j])
            elif j == 2:
                languages.append(i[j])
            elif j == 3:
                orgincountries.append(i[j])
            elif j == 4:
                likedgenres.append(i[j])
            elif j == 5:
                dislikedgenres.append(i[j])
            elif j == 6:
                likedtvshows.append(i[j])
            elif j == 7:
                dislikedtvshows.append(i[j])

    return [minLength(lengths)] + [minAge(ages)] + [commonLanguages(languages)] + [commonLanguages(orgincountries)] + [
        combineList(likedgenres)] + [combineList(dislikedgenres)] + [combineList(likedtvshows)] + [
               combineList(dislikedtvshows)]
