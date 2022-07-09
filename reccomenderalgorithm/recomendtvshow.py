from dataloader import loadInData
from combiner import mergePreferences
from knowledgefilter import knowledgeFilter
from contentfilter import contentFilter


def howmany(data):
    """
    Works out how many TV shows there are in the dataset
    Parameters
    data: Pandas dataframe of tv shows
    Returns
    integer
    list

    """
    output = []
    for ind in data.index:
        output.append(data['title'][ind])
    return len(output), output


def getremainingshows(data):
    """
    Extracts the shows left in the dataset
    Parameters
    data: Pandas dataframe containing the tv shows
    Returns
    List of tv shows
    """
    output = []
    for ind in data.index:
        output.append(data['title'][ind])
    return output


def reccomendtvshow(userinput):
    """
    Main algorithm for recomending tv shows
    Calls methods from other files then returns a list of tv shows
    Parameters
    userinput: Preferences to search the data with
    Returns
    list of tv shows to be recommended to the user
    """
    data = loadInData()

    userPreferences = mergePreferences(userinput)

    tvshowscombined = userPreferences[6]
    dislikedtvshows = userPreferences[7]

    filterresults = knowledgeFilter(userPreferences, data)

    howmanyshows = howmany(filterresults)

    remainingshows = getremainingshows(filterresults)
    if howmanyshows[0] == 0 or (set(remainingshows) == set(tvshowscombined + dislikedtvshows)):
        return ["No results"]
    elif howmanyshows[0] <= (len(tvshowscombined) + len(dislikedtvshows)) + 11:

        return howmanyshows[1]
    else:

        reccomendedtvshows = contentFilter(filterresults, tvshowscombined, dislikedtvshows)
        return reccomendedtvshows


def uptoknowl(userinputs):
    """
    Only does knowledge filtering of the data
    Paratmers:
    userinputs: Parameters to filter the dataset by
    Returns:
    dataset of remaining tv shows
    """
    data = loadInData()
    userpreferences = mergePreferences(userinputs)
    return knowledgeFilter(userpreferences, data)


def knowledgeshows(userinput):
    """
    Returns the tv shows that have are left after knowledge filtering
    Parameters
    userinput: User preferences sued for knowledge filtering
    Returns
    list of tv shows
    """
    data = loadInData()
    userpreferences = mergePreferences(userinput)

    filterresults = knowledgeFilter(userpreferences, data)
    output = []
    for ind in filterresults.index:
        output.append(filterresults['title'][ind])
    output.sort()
    return output
