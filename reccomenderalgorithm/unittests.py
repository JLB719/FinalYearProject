import unittest
import recomendtvshow
import random
import pandas as pd
from combiner import mergePreferences
from recomendtvshow import reccomendtvshow

testinput1 = [[5780, 2006, ['Finnish', 'Korean', 'Chinese', 'Catalan', 'Mandarin', 'Urdu', 'Hebrew'],
               ['Pakistan', 'Mexico', 'China'], ['News', 'Sci-Fi'], ['Romance'],
               ['OCTB', 'The Platform', 'Abla Fahita: Drama Queen', 'O Crush Perfeito', 'Xia Yi Zhan Shi Xing Fu'],
               ['How to Fix a Drug Scandal', 'Storage Wars Canada', 'Sensei wo Kesu Houteishiki', 'Upin & Ipin',
                'The Goop Lab']], [3224, 1980, ['Hindi', 'Min Nan', 'Chinese', 'Arabic', 'Korean', 'Swedish', 'Polish'],
                                   ['Singapore', 'Saudi Arabia', 'Australia', 'France', 'Japan', 'Philippines',
                                    'Mexico', 'India', 'Czech Republic'], ['Musical'], ['Family'],
                                   ['Scare Tactics', 'Bakugan: Battle Planet', 'The Killing', 'Social Distance',
                                    'Jenni Rivera: Mariposa de Barrio'],
                                   ['The Kominsky Method', 'Yeolyeodeolui Soongan', 'I Am Not Okay with This',
                                    'Happy Valley', 'Jack Whitehall: Travels with My Father']],
              [1128, 1992, ['Hungarian', 'Danish', 'Latin', 'English', 'Icelandic'],
               ['Argentina', 'Israel', 'Senegal', 'Japan', 'South Africa', 'Philippines'], ['Adventure'],
               ['Short', 'Thriller', 'Documentary', 'Reality-TV'],
               ['Star Trek: Voyager', 'Suzumiya Haruhi no yûutsu', 'Vexed', 'Inuyasha', 'Abby Hatcher'],
               ['Continuum', 'Babylon', 'Señora Acero', 'Advokaten', 'Yeok-jeok: baek-seong-eul hom-chin do-jeok']],
              [7464, 1975, ['Italian'],
               ['Turkey', 'Argentina', 'Taiwan', 'Mauritius', 'Lebanon', 'Sweden', 'South Africa'],
               ['Talk-Show', 'War'], ['News', 'Action', 'Family', 'Western', 'Horror'],
               ['Take My Brother Away', 'Taj Mahal 1989', 'Drag Race: Untucked!', 'Tower of God', 'Juana Inés'],
               ['Chosen', 'The Movies That Made Us', 'Valentino', 'Diablero', 'Damnation']]]
answerinput1 = [1128, 2006,
                ['Finnish', 'Korean', 'Chinese', 'Catalan', 'Mandarin', 'Urdu', 'Hebrew', 'Hindi', 'Min Nan', 'Arabic',
                 'Swedish', 'Polish', 'Hungarian', 'Danish', 'Latin', 'English', 'Icelandic', 'Italian'],
                ['Pakistan', 'Mexico', 'China', 'Singapore', 'Saudi Arabia', 'Australia', 'France', 'Japan',
                 'Philippines', 'India', 'Czech Republic', 'Argentina', 'Israel', 'Senegal', 'Turkey', 'Taiwan',
                 'Mauritius', 'Lebanon', 'Sweden', 'South Africa'],
                ['News', 'Sci-Fi', 'Musical', 'Adventure', 'Talk-Show', 'War'],
                ['Romance', 'Family', 'Short', 'Thriller', 'Documentary', 'Reality-TV', 'News', 'Action', 'Western',
                 'Horror'],
                ['OCTB', 'The Platform', 'Abla Fahita: Drama Queen', 'O Crush Perfeito', 'Xia Yi Zhan Shi Xing Fu',
                 'Scare Tactics', 'Bakugan: Battle Planet', 'The Killing', 'Social Distance',
                 'Jenni Rivera: Mariposa de Barrio', 'Star Trek: Voyager', 'Suzumiya Haruhi no yûutsu', 'Vexed',
                 'Inuyasha', 'Abby Hatcher', 'Take My Brother Away', 'Taj Mahal 1989', 'Drag Race: Untucked!',
                 'Tower of God', 'Juana Inés'],
                ['How to Fix a Drug Scandal', 'Storage Wars Canada', 'Sensei wo Kesu Houteishiki', 'Upin & Ipin',
                 'The Goop Lab', 'The Kominsky Method', 'Yeolyeodeolui Soongan', 'I Am Not Okay with This',
                 'Happy Valley', 'Jack Whitehall: Travels with My Father', 'Continuum', 'Babylon', 'Señora Acero',
                 'Advokaten', 'Yeok-jeok: baek-seong-eul hom-chin do-jeok', 'Chosen', 'The Movies That Made Us',
                 'Valentino', 'Diablero', 'Damnation']]
testinput2 = [[700, 1985, ["English", "Japanese"], ["United States", "United Kingdom"], ["Action", "Horror", "Comedy"],
               ["Drama", "Adventure", "Mystery"],
               ["New Amsterdam", "Chasing Cameron", "The Politician", "Queen of the South", "Richie Rich"],
               ["Dogs", "Revenge", "Dark Desire", "Home Game", "Queer Eye"]],
              [600, 2000, ["French", "Japanese", "English"], ["United States", "United Kingdom"],
               ["Fantasy", "Horror", "Reality TV"],
               ["History", "Thriller", "Romance"], ["Fawlty Towers", "7Seeds", "Chasing Cameron", "Emily in Paris"],
               ["The Queens Gambit", "Revenge", "Babies", "Cheese in the Trap", "Life in Our Universe"]],
              [300, 2005, ["English"], ["United States", "United Kingdom"], ["Gameshow", "Reality TV", "Comedy"],
               ["Drama", "Fantasy", "Animation"],
               ["Emily in Paris", "Another Life", "Shadow", "Crossing Lines", "Brooklyn Nine-Nine"],
               ["Lego: City", "The Letdown", "Married to Medicine", "Five Came Back", "Queer Eye"]],
              [300, 1950, ["English", "Chinese", "Russian"], ["United States", "United Kingdom"],
               ["Gameshow", "Romance", "Comedy"],
               ["Reality TV", "Thriller", "History"],
               ["Brooklyn Nine-Nine", "Floor Is Lava", "Supernatural", "No Good Nick", "Signal"],
               ["Teen Wolf", "The Good Place", "Ridley Jones", "The Dragon Prince", "Last Chance U"]]]
answerinput2 = [300, 2005, ["English"], ["United States", "United Kingdom"],
                ["Action", "Horror", "Comedy", "Fantasy", "Reality TV", "Gameshow", "Romance"],
                ["Drama", "Adventure", "Mystery", "History", "Thriller", "Romance", "Fantasy", "Animation",
                 "Reality TV", ],
                ["New Amsterdam", "Chasing Cameron", "The Politician", "Queen of the South", "Richie Rich",
                 "Fawlty Towers", "7Seeds", "Emily in Paris", "Another Life", "Shadow", "Crossing Lines",
                 "Brooklyn Nine-Nine", "Floor Is Lava", "Supernatural", "No Good Nick", "Signal"],
                ["Dogs", "Revenge", "Dark Desire", "Home Game", "Queer Eye", "The Queens Gambit", "Babies",
                 "Cheese in the Trap", "Life in Our Universe", "Lego: City", "The Letdown", "Married to Medicine",
                 "Five Came Back", "Teen Wolf", "The Good Place", "Ridley Jones", "The Dragon Prince", "Last Chance U"]]
testinput3 = [[100, 2000, ["English", "French"], ["Belgium", "France", "United Kingdom", "United States"],
               ["Comedy", "Drama", "History", "Romance"], ["Action", "Adventure", "Crime", "Thriller", "Western"],
               ["Emily in Paris", "Gilmore Girls: A Year in the Life", "Hannah Montana", "James Acaster: Repertoire",
                "Unbreakable Kimmy Schmidt"],
               ["Country Comfort", "Cuckoo", "Derry Girls", "Californication", "Family Business"]]]
answerinput3 = [100, 2000, ["English", "French"], ["Belgium", "France", "United Kingdom", "United States"],
                ["Comedy", "Drama", "History", "Romance"], ["Action", "Adventure", "Crime", "Thriller", "Western"],
                ["Emily in Paris", "Gilmore Girls: A Year in the Life", "Hannah Montana", "James Acaster: Repertoire",
                 "Unbreakable Kimmy Schmidt"],
                ["Country Comfort", "Cuckoo", "Derry Girls", "Californication", "Family Business"]]
testinput4 = [
    [500, 1986, ["English"], ["United States", "United Kingdom"], ["Action", "Adventure", "Crime", "Thriller"],
     ["Animation", "Biography", "Documentary", "Family", "Game-Show"],
     ["13 Reasons Why", "12 Monkeys", "Altered Carbon", "Delete", "Trinkets"],
     ["Arrow", "Babylon", "Dare Me", "The Fall", "The Flash"]],
    [400, 1987, ["English"], ["United States", "United Kingdom"],
     ["Action", "Comedy", "History", "Horror", "Thriller", "War", "Western"],
     ["Drama", "Fantasy", "Family"], ["Archer", "Deadly Class", "On My Block", "Pacific Rim", "Seinfeld"],
     ["The Umbrella Academy", "Prank Encounters", "Mighty Express", "White Gold", "The Wedding Coach"]]]
answerinput4 = [400, 1987, ["English"], ["United States", "United Kingdom"],
                ["Action", "Adventure", "Crime", "Thriller", "Comedy", "History", "Horror", "War", "Western"],
                ["Animation", "Biography", "Documentary", "Game-Show", "Drama", "Fantasy", "Family"],
                ["13 Reasons Why", "12 Monkeys", "Altered Carbon", "Delete", "Trinkets", "Archer", "Deadly Class",
                 "On My Block", "Pacific Rim", "Seinfeld"],
                ["Arrow", "Babylon", "Dare Me", "The Fall", "The Flash", "The Umbrella Academy", "Prank Encounters",
                 "Mighty Express", "White Gold", "The Wedding Coach"]]
testinput5 = [[3052, 1975, ['Filipino', 'Malay', 'Mandarin', 'Arabic'],
               ['Colombia', 'South Korea', 'Kuwait', 'Italy', 'China', 'France', 'Malaysia', 'Turkey', 'Argentina',
                'Mauritius', 'Australia', 'Israel', 'Luxembourg', 'New Zealand', 'Nigeria', 'Canada',
                'United Arab Emirates', 'Russia', 'Egypt', 'Pakistan', 'United Kingdom', 'Ireland', 'United States',
                'Singapore'], ['Animation', 'Game-Show', 'Short', 'Drama', 'Action', 'Sport'],
               ['Comedy', 'Short', 'Game-Show', 'Music', 'Sci-Fi', 'Thriller', 'Animation', 'Crime', 'History', 'News'],
               ['Three Wives, One Husband', 'Night Stalker: The Hunt for a Serial Killer', "Julie's Greenroom",
                'Operation Buffalo', 'Ask the Doctor'],
               ['Kono Oto Tomare!', 'Travelers', 'Hip-Hop Evolution', 'Fate/stay night: Unlimited Blade Works',
                'My Husband Oh Jak-doo']], [2962, 2012,
                                            ['Spanish', 'Hungarian', 'Luxembourgish', 'Portuguese', 'Indonesian',
                                             'German', 'Tagalog', 'Zulu', 'French', 'Icelandic', 'Norwegian',
                                             'Galician', 'English'],
                                            ['Hungary', 'Norway', 'Taiwan', 'Malaysia', 'Germany', 'South Korea',
                                             'Australia', 'Canada', 'Brazil', 'Italy', 'United Arab Emirates'],
                                            ['Romance', 'Sport', 'Sci-Fi', 'Mystery'],
                                            ['Musical', 'Drama', 'Documentary', 'Reality-TV', 'Action', 'Music',
                                             'Comedy', 'Adventure', 'Animation', 'Sci-Fi', 'Crime', 'Talk-Show',
                                             'Horror'], ['Dynasty', 'Cong qian you zuo ling jian shan', 'Slugterra',
                                                         'The Midnight Gospel', 'Mako Mermaids'],
                                            ['The One', 'Choi-go-eui Han-bang', 'Pajanimals', 'Rotten', 'The Ranch']]]
answerinput5 = [2962, 2012,
                ['Filipino', 'Malay', 'Mandarin', 'Arabic', 'Spanish', 'Hungarian', 'Luxembourgish', 'Portuguese',
                 'Indonesian', 'German', 'Tagalog', 'Zulu', 'French', 'Icelandic', 'Norwegian', 'Galician', 'English'],
                ['Italy', 'South Korea', 'Malaysia', 'Australia', 'Canada', 'United Arab Emirates'],
                ['Animation', 'Game-Show', 'Short', 'Drama', 'Action', 'Romance', 'Sport', 'Sci-Fi', 'Mystery'],
                ['Comedy', 'Short', 'Game-Show', 'Music', 'Sci-Fi', 'Thriller', 'Animation', 'Crime', 'History', 'News',
                 'Musical', 'Drama', 'Documentary', 'Reality-TV', 'Action', 'Adventure', 'Talk-Show', 'Horror'],
                ['Three Wives, One Husband', 'Night Stalker: The Hunt for a Serial Killer', "Julie's Greenroom",
                 'Operation Buffalo', 'Ask the Doctor', 'Dynasty', 'Cong qian you zuo ling jian shan', 'Slugterra',
                 'The Midnight Gospel', 'Mako Mermaids'],
                ['Kono Oto Tomare!', 'Travelers', 'Hip-Hop Evolution', 'Fate/stay night: Unlimited Blade Works',
                 'My Husband Oh Jak-doo', 'The One', 'Choi-go-eui Han-bang', 'Pajanimals', 'Rotten', 'The Ranch']]


def getrandomyear(data):
    """
    Gets a random year within the years range
    Parameters
    data: Pandas dataframe
    Returns
    Random integer year
    """
    years = []
    for ind in data.index:
        years.append(data['startYear'][ind])
    years = sorted(years)
    return random.randint(years[0], years[len(years) - 1])


def getrandomlengths(data):
    """
    Gets a random number of episodes within the episodes range
    Parameters
    data: Pandas dataframe
    Returns
    Random integer number of episodes
    """
    lengths = []
    for ind in data.index:
        lengths.append(data['episodes'][ind])
    lengths = sorted(lengths)

    return random.randint(lengths[0], lengths[len(lengths) - 1])


def getrandomlanguages(data):
    """
    Gets a random number of languages in the given languages
    Parameters
    data: Pandas dataframe
    Returns
    List of languages
    """
    languages = []
    for ind in data.index:
        languages.append(data['language'][ind])
    languages = list(set(languages))

    languagesample = random.sample(languages, random.randint(1, int(len(languages) / 2)))
    return languagesample


def getrandomcountries(data):
    """
    Gets a random number of origin countries in the given origin countries
    Parameters
    data: Pandas dataframe
    Returns
    List of origin countries
    """
    orgincountries = []
    for ind in data.index:
        orgincountries.append(data['origin_country'][ind])
    orgincountries = list(set(orgincountries))
    orginsample = random.sample(orgincountries, random.randint(1, int(len(orgincountries) / 2)))
    return orginsample


def getrandomgenres(data):
    """
    Gets a random number of genres in the given genres
    Then makes a random split of the genres into liked and disliked genres
    Parameters
    data: Pandas dataframe
    Returns
    List of likeed and disliked genres
    """
    allgenres = []
    for ind in data.index:
        smalllist = data['genres'][ind].split(".")
        for i in smalllist:
            allgenres.append(i)
    allgenres = list(set(allgenres))
    samplegenres = random.sample(allgenres, random.randint(2, int(len(allgenres) / 2)))

    random.shuffle(samplegenres)

    samplelength = len(samplegenres)
    firstlot = random.randint(1, int(len(samplegenres) / 2))

    return samplegenres[:firstlot], samplegenres[(-1 * (samplelength - firstlot)):]


def getrandomshows(data):
    """
    Gets a random number of tv shows in the given genres
    Then makes a random split of the tv shows into liked and disliked tv shows
    Parameters
    data: Pandas dataframe
    Returns
    List of liked and disliked tv shows
    """
    allshows = []
    for ind in data.index:
        allshows.append(data['title'][ind])

    showsample = random.sample(allshows, 10);
    random.shuffle(showsample)
    return showsample[:5], showsample[-5:]


def genrandompreferences():
    """
    Reads the data and generates random preferences for a random number of people
    Returns
    List of tv shows
    """
    data = pd.read_csv('data.csv')
    numberofpeople = random.randint(1, 10)

    dataprocesslist = []
    for _ in range(numberofpeople):
        dataprocesslist.append(
            [getrandomlengths(data), getrandomyear(data), getrandomlanguages(data), getrandomcountries(data),
             getrandomgenres(data)[0],
             getrandomgenres(data)[1], getrandomshows(data)[0], getrandomshows(data)[1]])

    return reccomendtvshow(dataprocesslist)


class MyTest(unittest.TestCase):
    def test_randominput(self):
        """
        Generates 10000 random pereferenes and runs them through the recommender system.
        Makes sure that no error occurs and the list is not empty
        """
        numberofruns = 10000
        blankcount = 0
        nocontent = 0
        properecs = 0
        for i in range(numberofruns):

            randomlist = genrandompreferences()
            if randomlist[0] == 'No results':
                blankcount += 1
            elif len(randomlist) != 10:
                nocontent += 1
            elif len(randomlist) == 10:
                properecs += 1
            self.assertTrue(bool([randomlist]))


def checklistsame(check, against):
    """
    Check if the list is the same as well as the length
    Set is used to not check the acutal contents of the sub lists are the same as order of the list doesn't matter
    Parameters
    check: One sample list
    against: A different sample list
    Returns
    true if the lists match
    false if the lists don't match
    """
    return (len(check) == len(against)) and (check[0] == against[0]) and (check[1] == against[1]) and (
            set(check[2]) == set(against[2])) and (set(check[3]) == set(against[3])) and (
                   set(check[4]) == set(against[4])) and (set(check[5]) == set(against[5])) and (
                   set(check[6]) == set(against[6])) and (set(check[7]) == set(against[7]))


def testcasedata(data, actual, lookstring):
    """
    Checks if the data only contains the values in a given list
    Parameters
    data: The remaining data after knowledge filtering
    actual: The list of values being checked
    lookstring: The data points being checked
    Returns
    true if all the items only have values in the actual list
    false if there are values in the data that aren't in the actual list
    """
    catlist = []

    for ind in data.index:
        catsublist = data[lookstring][ind]

        catlist.append(catsublist)

    catlist = list(set(catlist))

    return any(item in catlist for item in actual)


def testcasegenre(data, actual, lookstring):
    """
    Checks if the data only contains the values in a given list
    Parameters
    data: The remaining data after knowledge filtering
    actual: The list of values being checked
    lookstring: The data points being checked
    Returns
    true if all the items only have values in the actual list
    false if there are values in the data that aren't in the actual list
    """
    catlist = []

    for ind in data.index:
        catsublist = data[lookstring][ind]

        for i in catsublist:
            catlist.append(i)

    catlist = list(set(catlist))
    return any(item in catlist for item in actual)


def testyear(data, threshold, showlist):
    """
    Checks all the year is above the max year
    Parameters
    data: Pandas dataframe
    threshold: A year that is being checked
    showlist: THe list of shows as they don't count in the year threshold
    Returns
    true if all the data years are above the threshold
    false if any of the data years are less than the threshold
    """
    for ind in data.index:

        if (int(data['startYear'][ind]) < threshold) and data['title'][ind] not in showlist:
            return False

    return True


def testMaxEpisodes(data, threshold, showlist):
    """
    Checks all the episodes is less the max number of episodes
    Parameters
    data: Pandas dataframe
    threshold: A number of episodes that is being checked
    showlist: THe list of shows as they don't count in the max episodes threshold
    Returns
    true if all the data episodes are less than the threshold
    false if any of the data episodes are more than the threshold
    """
    for ind in data.index:
        if (int(data['episodes'][ind]) > threshold) and (data['title'][ind] not in showlist):
            return False
    return True


class UnitTesting(unittest.TestCase):
    def test_combinecorrect(self):
        """
        Runs the test input through the mergePreferences function
        Checks if the expected and generated list are the same
        """
        self.assertTrue(checklistsame(answerinput1, mergePreferences(testinput1)))
        self.assertTrue(checklistsame(answerinput2, mergePreferences(testinput2)))
        self.assertTrue(checklistsame(answerinput3, mergePreferences(testinput3)))
        self.assertTrue(checklistsame(answerinput4, mergePreferences(testinput4)))
        self.assertTrue(checklistsame(answerinput5, mergePreferences(testinput5)))

    def test_languagefilter(self):
        """
        Runs the test input through the uptoknowl function
        Checks that no unexpected languages are included
        """
        self.assertTrue(testcasedata(recomendtvshow.uptoknowl(testinput4), answerinput4[2], 'language'))
        self.assertTrue(testcasedata(recomendtvshow.uptoknowl(testinput1), answerinput1[2], 'language'))
        self.assertTrue(testcasedata(recomendtvshow.uptoknowl(testinput2), answerinput2[2], 'language'))
        self.assertTrue(testcasedata(recomendtvshow.uptoknowl(testinput3), answerinput3[2], 'language'))
        self.assertTrue(testcasedata(recomendtvshow.uptoknowl(testinput5), answerinput5[2], 'language'))

    def test_orgincountry(self):
        """
        Runs the test input through the uptoknowl function
        Checks that no unexpected origin countries are included
        """
        self.assertTrue(testcasedata(recomendtvshow.uptoknowl(testinput4), answerinput4[3], 'origin_country'))
        self.assertTrue(testcasedata(recomendtvshow.uptoknowl(testinput1), answerinput1[3], 'origin_country'))
        self.assertTrue(testcasedata(recomendtvshow.uptoknowl(testinput2), answerinput2[3], 'origin_country'))
        self.assertTrue(testcasedata(recomendtvshow.uptoknowl(testinput3), answerinput3[3], 'origin_country'))
        self.assertTrue(testcasedata(recomendtvshow.uptoknowl(testinput5), answerinput5[3], 'origin_country'))

    def test_year(self):
        """
        Runs the test input through the uptoknowl function
        Checks that no unexpected years are included
        """
        self.assertTrue(
            testyear(recomendtvshow.uptoknowl(testinput4), answerinput4[1], answerinput4[6] + answerinput4[7]))
        self.assertTrue(
            testyear(recomendtvshow.uptoknowl(testinput1), answerinput1[1], answerinput1[6] + answerinput1[7]))
        self.assertTrue(
            testyear(recomendtvshow.uptoknowl(testinput2), answerinput2[1], answerinput2[6] + answerinput2[7]))
        self.assertTrue(
            testyear(recomendtvshow.uptoknowl(testinput3), answerinput3[1], answerinput3[6] + answerinput3[7]))
        self.assertTrue(
            testyear(recomendtvshow.uptoknowl(testinput5), answerinput5[1], answerinput5[6] + answerinput5[7]))

    def test_number(self):
        """
        Runs the test input through the uptoknowl function
        Checks that no unexpected number of episodes are included
        """
        self.assertTrue(
            testMaxEpisodes(recomendtvshow.uptoknowl(testinput4), answerinput4[0], answerinput4[6] + answerinput4[7]))
        self.assertTrue(
            testMaxEpisodes(recomendtvshow.uptoknowl(testinput1), answerinput1[0], answerinput1[6] + answerinput1[7]))
        self.assertTrue(
            testMaxEpisodes(recomendtvshow.uptoknowl(testinput2), answerinput2[0], answerinput2[6] + answerinput2[7]))
        self.assertTrue(
            testMaxEpisodes(recomendtvshow.uptoknowl(testinput3), answerinput3[0], answerinput3[6] + answerinput3[7]))
        self.assertTrue(
            testMaxEpisodes(recomendtvshow.uptoknowl(testinput5), answerinput5[0], answerinput5[6] + answerinput5[7]))

    def test_genres(self):
        """
        Runs the test input through the uptoknowl function
        Checks that no unexpected genres are included
        """
        self.assertFalse(testcasegenre(recomendtvshow.uptoknowl(testinput4), answerinput4[6], 'genres'))
        self.assertFalse(testcasegenre(recomendtvshow.uptoknowl(testinput1), answerinput1[6], 'genres'))
        self.assertFalse(testcasegenre(recomendtvshow.uptoknowl(testinput2), answerinput2[6], 'genres'))
        self.assertFalse(testcasegenre(recomendtvshow.uptoknowl(testinput3), answerinput3[6], 'genres'))
        self.assertFalse(testcasegenre(recomendtvshow.uptoknowl(testinput5), answerinput5[6], 'genres'))


if __name__ == '__main__':
    unittest.main()
