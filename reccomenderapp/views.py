from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from django.http import HttpResponse

from reccomenderapp.form import CreateGroup
from reccomenderapp.form import JoinGroupForm
from reccomenderapp.form import GenerateResultsForm
from reccomenderapp.form import KnowledgeSelect
from reccomenderapp.form import ContentFilter
from django.template import loader

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from .models import UserPreferences
from django.urls import reverse_lazy
from django.views import generic
import pandas as pd
import sys

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent;

sys.path.insert(0, str(BASE_DIR) + '/reccomenderalgorithm')

from dataloader import loadInData
from recomendtvshow import reccomendtvshow
from recomendtvshow import knowledgeshows


class SignUpView(generic.CreateView):
    """
    View copied from Django
    Used to display the user creation view and allow them to register an account
    """
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


def index(request):
    """
    Returns the home page of the website

    Parameters
    request: Meta-data to do with the request
    """
    return render(request, 'home.html')


def listShows(request):
    """
    Returns a webpage containing all the shows in the data set

    Parameters
    request: Meta-data to do with the request
    """
    data = pd.read_csv("reccomenderalgorithm/data.csv")

    biglist = []
    for ind in data.index:
        datapass = {'title': data['title'][ind], 'image': data['image_url'][ind]}
        buildurl = 'https://www.imdb.com/title/' + data['imdb_id'][ind] + '/'
        datapass['url'] = buildurl
        biglist.append(datapass)
    context = {
        "data": biglist
    }
    template = loader.get_template('showallshows.html')
    return HttpResponse(template.render(context, request))


def knowledgeEnter(request):
    """
    Form for users to enter preferences for tv shows they may want to watch
    Directs them to either a list of recomendations or another form where they enter their liked and disliked shows
    Parameters
    request: Meta-data to do with the request
    """

    grouprender = ""
    if request.method == 'POST':

        grouprender = KnowledgeSelect(request.POST)
        if grouprender.is_valid():

            userpref = ""
            if UserPreferences.objects.filter(username=request.user.username).exists():
                userpref = UserPreferences.objects.get(username=request.user.username)
            else:
                userpref = UserPreferences(username=request.user.username)

            userpref.maxyear = grouprender.cleaned_data['oldestyear']
            userpref.numberofepisodes = grouprender.cleaned_data['minepisodes']
            userpref.languages = convertStringToList(grouprender.cleaned_data['languages'])
            userpref.origincountries = convertStringToList(grouprender.cleaned_data['orgincountries'])
            userpref.likedgenres = convertStringToList(grouprender.cleaned_data['likedgenres'])
            userpref.dislikedgenres = convertStringToList(grouprender.cleaned_data['dislikedgenres'])
            userpref.save()
            sublist = [grouprender.cleaned_data['minepisodes'], grouprender.cleaned_data['oldestyear'],
                       grouprender.cleaned_data['languages'], grouprender.cleaned_data['orgincountries'],
                       grouprender.cleaned_data['likedgenres'], grouprender.cleaned_data['dislikedgenres']]

            shows = knowledgeshows([sublist])

            if len(shows) <= 20:
                form = ContentFilter(request=filterTVShows())
                return render(request, 'contentform.html', {"form": form})
            else:
                form = ContentFilter(request=knowledgeshows([sublist]))
                return render(request, 'contentform.html', {"form": form})
    else:

        grouprender = KnowledgeSelect()
    return render(request, 'knowledgeform.html', {"form": grouprender})


def contentEnter(request):
    """
    Once a user has filled out the knoweldge form they are directed to this form where they enter in the shows the like and dislike
    Recomendations are then generated for them.
    Parameters
    request: Meta-data to do with the request
    """
    if request.method == 'POST':

        contentformvar = ContentFilter(data=request.POST, request=filterTVShows())
        if contentformvar.is_valid():
            modellist = []
            accesspref = UserPreferences.objects.get(username=request.user.username)
            modellist.append(accesspref.numberofepisodes)
            modellist.append(accesspref.maxyear)
            modellist.append(accesspref.languages.split(','))
            modellist.append(accesspref.origincountries.split(','))
            modellist.append(accesspref.likedgenres.split(','))
            modellist.append(accesspref.dislikedgenres.split(','))

            likedtvshowlist = [contentformvar.cleaned_data['likedtvshow1'], contentformvar.cleaned_data['likedtvshow2'],
                               contentformvar.cleaned_data['likedtvshow3'], contentformvar.cleaned_data['likedtvshow4'],
                               contentformvar.cleaned_data['likedtvshow5']]

            dislikedtvshowlist = [contentformvar.cleaned_data['dislikedtvshow1'],
                                  contentformvar.cleaned_data['dislikedtvshow2'],
                                  contentformvar.cleaned_data['dislikedtvshow3'],
                                  contentformvar.cleaned_data['dislikedtvshow4'],
                                  contentformvar.cleaned_data['dislikedtvshow5']]

            modellist.append(likedtvshowlist)
            modellist.append(dislikedtvshowlist)
            accesspref.likedshows = convertStringToList(likedtvshowlist)
            accesspref.dislikedshows = convertStringToList(dislikedtvshowlist)
            accesspref.save()
            preferencelist = [modellist]
            reccomendedshows = reccomendtvshow(preferencelist)
            if "No results" == reccomendedshows[0]:
                return render(request, 'noshows.html')
            else:
                context = generateContext(reccomendedshows)
                template = loader.get_template('reccomendedshows.html')
                return HttpResponse(template.render(context, request))
    else:

        contentformvar = ContentFilter(request=filterTVShows())
    return render(request, 'contentform.html', {"form": contentformvar})


@login_required
def generateResults(request):
    """
    User selects the group they want to generate recommendations for
    The recommendations are then generated for them.
    Parameters
    request: Meta-data to do with the request
    """
    if request.method == 'POST':
        generateresultsformvar = GenerateResultsForm(data=request.POST, request=request)
        if generateresultsformvar.is_valid():

            groupnamesearch = generateresultsformvar.cleaned_data['groupname']
            group = Group.objects.get(name=groupnamesearch)
            userquery = group.user_set.all()

            preferencelist = []
            for i in userquery:

                
                if UserPreferences.objects.filter(username=i).exists() :
                    if checkValidInput(UserPreferences.objects.get(username=i)):

                        accesspref = UserPreferences.objects.get(username=i)

                        modellist = [accesspref.numberofepisodes, accesspref.maxyear, accesspref.languages.split(','),
                                     accesspref.origincountries.split(','), accesspref.likedgenres.split(','),
                                     accesspref.dislikedgenres.split(','), accesspref.likedshows.split(','),
                                     accesspref.dislikedshows.split(',')]

                        preferencelist.append(modellist)

            if not preferencelist:
                return render(request, 'nopreferences.html')

            reccomendedtvshows = reccomendtvshow(preferencelist)
            if reccomendedtvshows[0] == 'No results':
                return render(request,'noshows.html')
            else:

                context = generateContext(reccomendedtvshows)

                template = loader.get_template('reccomendedshows.html')
                return HttpResponse(template.render(context, request))
    else:
        usergroupsquery = request.user.groups.all()

        usergroupslist = []
        for i in range(len(usergroupsquery)):
            usergroupslist.append(usergroupsquery[i])

        if not usergroupslist:
            return render(request,'nogroups.html')
        generateformrender = GenerateResultsForm(request=request)
    return render(request, 'generateresultsselection.html', {"form": generateformrender})


@login_required
def showPreferences(request):
    """
    Returns the recomened tv shows that have previoulsy been generated for the user along with the groups the user is a part of
    Parameters
    request: Meta-data to do with the request
    """
    if UserPreferences.objects.filter(username=request.user.username).exists():
        accesspref = UserPreferences.objects.get(username=request.user.username)

        modellist = [accesspref.numberofepisodes, accesspref.maxyear, accesspref.languages.split(','),
                     accesspref.origincountries.split(','), accesspref.likedgenres.split(','),
                     accesspref.dislikedgenres.split(','), accesspref.likedshows.split(','),
                     accesspref.dislikedshows.split(',')]

        preferencelist = [modellist]
        reccomendedshows = reccomendtvshow(preferencelist)
        usergroupsquery = request.user.groups.all()
        usergroupslist = []
        for i in range(len(usergroupsquery)):
            data = {}
            data['groupname'] = usergroupsquery[i]
            stringbuild = '/groups/' + str(usergroupsquery[i])
            urlstring = request.build_absolute_uri(stringbuild)
            data['groupurl'] = urlstring
            usergroupslist.append(data)
        if reccomendedshows[0] == "No results" or not checkValidInput(accesspref):
            return render(request, 'noshows.html')
        else:
            context = generateContext(reccomendedshows)
            context['groups'] = usergroupslist
            template = loader.get_template('myinfo.html')

            return HttpResponse(template.render(context, request))
    else:
        return render(request, 'nopreferences.html')


@login_required
def createGroup(request):
    """
    Creates the group that a user has asked to be created then adds the use to that group
    Also generates an invite link for the group
    Parameters
    request: Meta-data to do with the request
    """
    if request.method == 'POST':
        groupform = CreateGroup(request.POST)
        if groupform.is_valid():

            groupname = groupform.cleaned_data['groupname']

            grouplist = Group.objects.all()

            if doesGroupExist(grouplist, groupname):
                stringbuild = '/groups/' + groupname
                urlstring = request.build_absolute_uri(stringbuild)
                context = {
                    'groupurl': urlstring
                }
                template = loader.get_template('groupalreadyexist.html')
                return HttpResponse(template.render(context, request))

            else:

                group = Group.objects.create(name=groupname)

                stringbuild = '/groups/' + groupname
                urlstring = request.build_absolute_uri(stringbuild)
                request.user.groups.add(group)
                context = {
                    'groupname': groupname,
                    'grouplink': urlstring
                }
                template = loader.get_template('groupsuccess.html')
                return HttpResponse(template.render(context, request))

    else:
        grouprender = CreateGroup()
    return render(request, 'creategroup.html', {"form": grouprender})


@login_required
def joinGroup(request):
    """
    Presents a list of groups that a user can join then adds the user to the group they requested to join
    Parameters
    request: Meta-data to do with the request
    """
    if request.method == 'POST':

        joingroupformvar = JoinGroupForm(data=request.POST, request=Group.objects.all())
        if joingroupformvar.is_valid():
            joinedgroup = joingroupformvar.cleaned_data['grouplistfield']

            group = Group.objects.get(name=joinedgroup)
            request.user.groups.add(group)
            context = {
                'groupname': joinedgroup
            }
            template = loader.get_template('joingroupsuccess.html')
            return HttpResponse(template.render(context, request))
    else:

        usergroupsquery = Group.objects.all()

        usergroupslist = []
        for i in range(len(usergroupsquery)):
            usergroupslist.append(usergroupsquery[i])
        if (usergroupslist == []):
            return render(request, 'noexistinggroups.html')
        grouplistrender = JoinGroupForm \
            (request=Group.objects.exclude(id__in=request.user.groups.all().values_list('id', flat=True)))
    return render(request, 'grouppage.html', {"form": grouplistrender})


@login_required
def joinGroupLink(request, groupname):
    """
    Looks at the end of a url entered for the group name then adds the user to that group
    Parameters
    request: Meta-data to do with the request
    groupname: The group that the user is wanted to join
    """
    grouplist = Group.objects.all()
    if doesGroupExist(grouplist, groupname):
        group = Group.objects.get(name=groupname)
        request.user.groups.add(group)
        context = {
            'groupname': groupname
        }
        template = loader.get_template('joingroupsuccess.html')
        return HttpResponse(template.render(context, request))
    else:

        return render(request, 'groupnoexist.html')


def generateContext(shows):
    """
    Converts the recommended tv shows into a python dictionary that can be displayed on a html page

    Paramters
    shows: The recommended tv shows

    Returns
    Python dictionary
    """
    data = pd.read_csv("reccomenderalgorithm/data.csv")

    biglist = []
    for i in shows:
        datapass = {}

        lookingindex = data.index[(data['title'] == i)].tolist()[0]

        datapass['title'] = i

        datapass['image'] = data['image_url'][lookingindex]
        buildurl = 'https://www.imdb.com/title/' + data['imdb_id'][lookingindex] + '/'

        datapass['imdblink'] = buildurl
        biglist.append(datapass)

    context = {
        "data": biglist
    }
    return context


def doesGroupExist(groups, groupquery):
    """
    Checks if a group has already been created

    Parameters
    groups: The list of created groups
    groupquery: The group to be checked to see if it already exits

    Returns
    boolean
    """
    for i in range(len(groups)):

        if groups[i].name == groupquery:
            return True
    return False


def filterTVShows():
    """
    Gets the tv shows from a 2d list and returns a 1d aplphabetical list of tv shows
    """
    inputarray = loadInData()
    outputlist = []
    for i in range(len(inputarray)):
        outputlist.append(inputarray[i][0])
    outputlist = sorted(outputlist, key=str.lower)
    return outputlist


def convertStringToList(inputlist):
    """
    Converts a list to a string to be inputed into a model field

    Parameters
    inputlist: A list of values that need to be converted into a string

    Returns
    output: a string of the list with the list items separated by commas
    """
    output = ''
    for i in range(len(inputlist)):
        if i == len(inputlist) - 1:
            output = output + inputlist[i]
        else:
            output = output + inputlist[i] + ","
    return output


def checkValidInput(model):
    """
    Checks if a user prefrences model has all the required fields completed.

    Parameters
    model: The input model that is being checked

    Returns
    boolean
    """
    return (model.languages != '') and (model.origincountries != '') and (model.likedgenres != '') and \
           (model.dislikedgenres != '') and (model.likedshows != '') and (model.dislikedshows != '')
