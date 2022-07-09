from django import forms

from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parent.parent;

sys.path.insert(0, str(BASE_DIR) + '/reccomenderalgorithm')
from dataloader import loadInData
import pandas as pd


def filtertvshows():
    inputarray = loadInData()
    outputlist = []
    for i in range(len(inputarray)):
        outputlist.append(inputarray[i][0])
    outputlist = sorted(outputlist, key=str.lower)
    return outputlist


def filtercountries():
    data = pd.read_csv('reccomenderalgorithm/data.csv')
    biglist = []
    for ind in data.index:
        biglist.append(data['origin_country'][ind])

    setlist = set(biglist)
    biglist = list(setlist)
    biglist.sort()
    biglist.pop(0)
    return biglist


class KnowledgeSelect(forms.Form):
    oldestyear = forms.IntegerField(initial=1966,
                                    label="<h7>What is the oldest TV show you are willing to watch <b>(enter "
                                          "year)</b></h7>",
                                    max_value=2020,
                                    min_value = 0)
    minepisodes = forms.IntegerField(initial=8358,
                                     label="<h7>How many <b>episodes</b> of a TV are you willing to watch?</h7>",
                                     min_value=1, max_value= 2**31)
    listofgenres = ['Sci-Fi', 'News', 'Crime', 'Romance', 'Thriller', 'Mystery', 'Drama', 'Biography', 'Short',
                    'Horror', 'Music', 'Game-Show', 'Animation', 'Action', 'Comedy', 'Documentary', 'Musical', 'Sport',
                    'Fantasy', 'Reality-TV', 'Talk-Show', 'Adventure', 'History', 'War', 'Western', 'Family']
    listofgenres = sorted(listofgenres)
    listoflanguages = ["Arabic", "Cantonese", "Catalan", "Chinese", "Danish", "Dutch", "English", "Filipino", "Finnish",
                       "French", "Galician", "German", "Hebrew", "Hindi", "Hungarian", "Icelandic", "Indonesian",
                       "Italian", "Japanese", "Korean", "Latin", "Luxembourgish", "Malay", "Mandarin", "Min Nan",
                       "Norwegian", "Polish", "Portuguese", "Russian", "Spanish", "Swedish", "Tagalog", "Tamil", "Thai",
                       "Turkish", "Urdu", "Zulu"]
    languages = forms.MultipleChoiceField(label="<h7>In which <b>languages</b> are you willing to watch TV shows?</h7>",
                                          widget=forms.CheckboxSelectMultiple,
                                          choices=[(x, x) for x in listoflanguages])
    orgincountries = forms.MultipleChoiceField(
        label="<h7>Select which <b>countries'</b> TV shows you are willing to watch</h7>",
        widget=forms.CheckboxSelectMultiple,
        choices=[(x, x) for x in filtercountries()])
    likedgenres = forms.MultipleChoiceField(label="<h7>Select the genres you <b>like</b></h7>",
                                            widget=forms.CheckboxSelectMultiple,
                                            choices=[(x, x) for x in listofgenres])
    dislikedgenres = forms.MultipleChoiceField(label="<h7>Select the genres you <b>dislike</b></h7>",
                                               widget=forms.CheckboxSelectMultiple,
                                               choices=[(x, x) for x in listofgenres])


class ContentFilter(forms.Form):
    likedtvshow1 = forms.ChoiceField(label="<h7>Select TV show you <b>like</b></h7>")
    likedtvshow2 = forms.ChoiceField(label="<h7>Select TV show you <b>like</b></h7>")
    likedtvshow3 = forms.ChoiceField(label="<h7>Select TV show you <b>like</b></h7>")
    likedtvshow4 = forms.ChoiceField(label="<h7>Select TV show you <b>like</b></h7>")
    likedtvshow5 = forms.ChoiceField(label="<h7>Select TV show you <b>like</b></h7>")
    dislikedtvshow1 = forms.ChoiceField(label="<h7>Select TV show you <b>dislike</b></h7>")
    dislikedtvshow2 = forms.ChoiceField(label="<h7>Select TV show you <b>dislike</b></h7>")
    dislikedtvshow3 = forms.ChoiceField(label="<h7>Select TV show you <b>dislike</b></h7>")
    dislikedtvshow4 = forms.ChoiceField(label="<h7>Select TV show you <b>dislike</b></h7>")
    dislikedtvshow5 = forms.ChoiceField(label="<h7>Select TV show you <b>dislike</b></h7>")

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(ContentFilter, self).__init__(*args, **kwargs)
        shows = self.request
        self.fields['likedtvshow1'].choices = [(x, x) for x in shows]
        self.fields['likedtvshow2'].choices = [(x, x) for x in shows]
        self.fields['likedtvshow3'].choices = [(x, x) for x in shows]
        self.fields['likedtvshow4'].choices = [(x, x) for x in shows]
        self.fields['likedtvshow5'].choices = [(x, x) for x in shows]
        self.fields['dislikedtvshow1'].choices = [(x, x) for x in shows]
        self.fields['dislikedtvshow2'].choices = [(x, x) for x in shows]
        self.fields['dislikedtvshow3'].choices = [(x, x) for x in shows]
        self.fields['dislikedtvshow4'].choices = [(x, x) for x in shows]
        self.fields['dislikedtvshow5'].choices = [(x, x) for x in shows]


class GenerateResultsForm(forms.Form):
    groupname = forms.ChoiceField(label="Select group to generate results for")

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(GenerateResultsForm, self).__init__(*args, **kwargs)

        usergroupsquery = self.request.user.groups.all()

        usergroupslist = []
        for i in range(len(usergroupsquery)):
            usergroupslist.append(usergroupsquery[i])
        self.fields['groupname'].choices = [(x, x) for x in usergroupslist]


class CreateGroup(forms.Form):
    groupname = forms.CharField(label="Enter the name of the group you would like to create", max_length=150)


class JoinGroupForm(forms.Form):
    grouplistfield = forms.ChoiceField(label="Select the group you would like to join")

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(JoinGroupForm, self).__init__(*args, **kwargs)

        usergroupsquery = self.request

        usergroupslist = []
        for i in range(len(usergroupsquery)):
            usergroupslist.append(usergroupsquery[i])
        self.fields['grouplistfield'].choices = [(x, x) for x in usergroupslist]
