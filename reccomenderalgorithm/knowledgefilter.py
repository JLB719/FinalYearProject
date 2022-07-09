import pandas as pd


def knowledgeFilter(userinputs, data):
    """
    Filters a list of data based on the user inputs
    Parameters
    userinputs: an array of combined user input
    data: Data in the form of a 2d array
    Returns
    pandas dataframe containing the remaing tv shows and their assocaitated values
    """
    filtered = filter(lambda k: (lengthMatch(userinputs[0], k[3]) and yearMatch(userinputs[1], k[2])
                                 and languageMatch(userinputs[2], k[4]) and languageMatch(userinputs[3],
                                                                                          k[5]) and genreMatch(
                userinputs[4], k[9]) and not genreMatch(userinputs[5], k[9])) or (
                                    tvShowMatch(k[0], userinputs[6])) or (tvShowMatch(k[0], userinputs[7])), data)

    return convertToDataFrame(list(filtered))


def convertToDataFrame(data):
    """
    Converts a 2d array to a pandas dataframe
    Paramters
    data: 2d list of data
    returns
    pandas dataframe
    """
    indexes = []
    for i in range(len(data)):
        indexes.append(i)
    dataframe = pd.DataFrame(data,
                             columns=['title', 'popular_rank', 'startYear', 'episodes', 'language', 'origin_country',
                                      'plot', 'summary',
                                      'rating', 'genres', 'cast', 'image_url', 'imdb_id'])
    dataframe.insert(0, "index", indexes)
    return dataframe


def lengthMatch(userinputs, datainput):
    """
    Checks if the length of TV show matches requirements
    Parameters:
    datainput: length of a tv show
    userinputs: the value the datainput is being comapred against
    returns
    True if userinputs is > than data input
    False if datainput > userinptus
    """
    return int(datainput) <= userinputs


# Checks if the year matches the requirements
def yearMatch(userinputs, datainput):
    """
    Checks if the year matches the requirements
    Parameters:
    datainput: year of a tv show
    userinputs: the value the datainput is being comapred against
    returns
    True if userinputs is > than data input
    False if datainput > userinptus
    """

    return int(datainput) >= userinputs


# Checks if the languages match requirements
def languageMatch(userinputs, datainput):
    """
    Checks if the languages match requirements
    Parameters
    datainput: langauges of a tv show
    userinptus: lanagues that are being checked against the langauge
    Returns
    True if the data input is in the user input
    False if the data input is not in the user input
    """
    return datainput in userinputs


# Checks if the genre matches the requirments
def genreMatch(userinputs, datainput):
    """
    Checks if the genre matches the requirments
    Parameters
    datainput: genre of a tv show
    userinptus: genre that are being checked against the langauge
    Returns
    True if the data input is in the user input
    False if the data input is not in the user input
    """
    for i in userinputs:
        for j in datainput:
            if j == i:
                return True
    return False


# Checks if the TV show is a user specified one
def tvShowMatch(show, listofshows):
    """
    Checks if the TV show is a user specified one
    Parameters
    datainput: name of a tv show
    userinptus: name that are being checked against the langauge
    Returns
    True if the data input is in the user input
    False if the data input is not in the user input
    """
    return show in listofshows
