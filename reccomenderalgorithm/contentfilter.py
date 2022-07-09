from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import linear_kernel
import ast


def contentFilter(data, likedtvshows, dislikedtvshows):
    """
    Carries out content filtering on the data
    Parameters
    Data: Pandas dataframe containing remaining TV shows 
    LikedTvshows: The tv shows users like
    DislikedTVshows: The tv shows user dislikes
    Returns
    List of 10 tv shows
    """
    features = ['genres', 'cast']
    for f in features:
        data[f] = data[f].apply(clean_data)

    data['soup2'] = data.apply(create_soup_keyword, axis=1)
    count = CountVectorizer(analyzer='word', ngram_range=(1, 2), min_df=0, stop_words='english')

    count_matrix = count.fit_transform(data['soup2'])

    cosine_similarities_categ = cosine_similarity(count_matrix, count_matrix)

    # makes a vectorizer
    data['soup'] = data.apply(create_soup, axis=1)
    tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 3), min_df=0, stop_words='english')
    # applys vecorization to the plots of the shows
    tfidf_matrix = tf.fit_transform(data['soup'])

    # generates a matrix containing the similarity of the plots compared to eachtoher
    cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)

    # extracts the relevant rows containing the tv shows we are interested in
    result = extract_relevant_rows(data, likedtvshows, dislikedtvshows, cosine_similarities)
    resultcast = extract_relevant_rows(data, likedtvshows, dislikedtvshows, cosine_similarities_categ)
    # gets the rows needed
    extracted = result[0]
    extracted_cast = resultcast[0]

    # gets the indexes of the relevant tv shows
    indexes = result[1]

    # rotates the matrix ot make it easier to work out
    rotatedscores = rotatescores(extracted)
    rotatedscorescast = rotatescores(extracted_cast)
    # returns the indexs of the relvant films that have a high socre

    scoreindexes = bestindexes(rotatedscores, rotatedscorescast, indexes)

    # #returns the best tv shows based on the indexes
    return toptvshows(data, scoreindexes)


def create_soup(x):
    """
    Joins the plots and summaries together
    Parameters
    x: The data line
    Returns
    Joined list of plot and summary
    """
    return ''.join(x['plot']) + '' + ''.join(x['summary'])


def create_soup_keyword(x):
    """
    Joins the genres and cast together
    Parameters
    x: The data line
    Returns
    Joined list of genres and cast
    """
    x['cast'] = ast.literal_eval(x['cast'])

    return ' '.join(x['genres']) + ' ' + ' '.join(x['cast'])


def clean_data(x):
    """
    Removes spaces from data
    Parameters
    x: Data to be cleaned
    Returns
    Cleaned data
    """
    if isinstance(x, list):
        return [str.lower(i.replace(' ', '')) for i in x]
    else:
        if isinstance(x, str):
            return str.lower(x.replace(' ', ''))
        else:
            return ''


def toptvshows(shows, indexes):
    """
    Grabs the top 10 tv shows based on their indexes
    Parameters
    shows: Pandas dataframe containing tv shows
    indexes: Indexes of the top 10 tv shows
    Returns
    10 TV shows
    """
    output = []

    for i in range(10):
        showind = shows.loc[indexes[i]]['title']
        output.append(showind)

    return output


def extract_relevant_rows(data, likedtvshows, dislikedtvshows, cosine_similarities):
    """
    First gets the indexes of the liked and disliekd shows then returns the remaining similarity scores
    Paramters
    Data: The pandas dataframe
    Likedtvshows: The shows a user likes
    Dislikedtvshows: The shouws a user doesn't like
    Cosine_similarities: The similarity matrix of the shows
    Returns
    Similarity matrix with the rows not containing liked tv shows and diskliked tv shows
    """
    indexlist = []
    negativeindexlist = []

    for ind in data.index:

        if tvshowcontained(data['title'][ind], likedtvshows):
            indexlist.append(ind)
        if tvshowcontained(data['title'][ind], dislikedtvshows):
            negativeindexlist.append(ind)
    cosinelist = cosine_similarities.tolist()

    similarityscores = []
    for i in range(len(cosinelist)):
        if tvshowcontained(i, indexlist):
            similarityscores.append(cosinelist[i])
        if tvshowcontained(i, negativeindexlist):
            for j in range(len(cosinelist[i])):
                cosinelist[i][j] = cosinelist[i][j] * -1
            similarityscores.append(cosinelist[i])

    return similarityscores, indexlist + negativeindexlist


def rotatescores(data):
    """
    Rotates the cosine matrix to make it easier to manipulate
    Parameters
    data: Consine simialrity matrix 
    Returns
    rotated simialrity matrix
    """
    output = []
    samplelist = []
    for i in range(len(data[0])):
        for j in range(len(data)):

            if j == 0:
                samplelist = []

            samplelist.append(data[j][i])
        output.append(samplelist)
    return output


def bestindexes(data, cast, tvindexes):
    """
    Calculates the average simialrity score corresponing to teach remaining tv show candiate
    First calulates average cosine similarity then adds the index to it. Then sorts them from highest to lowest
    Takes the top 10 values in the list and extracts the indexes
    Parameters
    Data: THe cosine similarity scores for the plot and summary
    Cast: The cosine similarity scores for the cast and genres
    tvindexes: Indexes of the liked and disliked tv shows
    Returns
    Indexes of the top 10 tv shows
    """
    output = []
    plainlist = []
    maxval = 0
    lowval = 0
    for i in range(len(data)):
        innerlist = []

        average = (sum(data[i])) / (len(data[i]))
        averagecast = (sum(cast[i])) / (len(cast[i]))
        totalaverage = averagecast + average
        if totalaverage > maxval:
            maxval = totalaverage
        elif totalaverage < lowval:
            lowval = totalaverage
        innerlist.append(average + averagecast)
        innerlist.append(i)
        plainlist.append(totalaverage)
        output.append(innerlist)

    sortedlist = sorted(output, key=lambda x: x[0], reverse=True)

    purelist = []
    for i in sortedlist:
        purelist.append(i[0])

    output = []
    for i in sortedlist:
        if i[1] not in tvindexes:
            output.append(i[1])

    return output


def tvshowcontained(inputshow, tvshows):
    """
    Checks if a tv show is in the in the overal list of tv shows
    Paramters
    input: Candiate tv show
    tvshows: Overal list of tv shows
    Returns
    True if the tv show is in the set
    False if the tv show is not in the set
    """
    return inputshow in tvshows
