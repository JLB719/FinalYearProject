from django.urls import path
from . import views
from .views import SignUpView

urlpatterns = [
    path('', views.index, name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('creategroup/', views.createGroup, name='creategroup'),
    path('groupsuccess/', views.createGroup, name='groupsuccess'),
    path('joingroup/', views.joinGroup, name='joingroup'),
    path('joingroupsuccess/', views.joinGroup, name='joingroupsuccess'),
    path('selectgroupgenerate/', views.generateResults, name='selectgroupgenerate'),
    path('generatedresults/', views.generateResults, name='generatedresults'),
    path('showsgroup/', views.generateResults, name='showsgroup'),
    path('userrecommend/', views.showPreferences, name='useresults'),
    path('contentform/', views.knowledgeEnter, name='contentform'),
    path('form/', views.knowledgeEnter, name='form'),
    path('contentresults/', views.contentEnter, name='contentresults'),
    path('groups/<str:groupname>', views.joinGroupLink, name='joingrouplink'),
    path('allshows/', views.listShows, name='listshows')

    
]