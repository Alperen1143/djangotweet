
from django.urls import path
from . import views

app_name='tweetapp'
urlpatterns = [
    path('',views.listtweet,name='listtweet'),
    path('addtweet/',views.addtweet,name='addtweet'),
    path('addtweetbyform/',views.adtweetbyform,name='addtweetbyform'),
    path('addtweetbymodel/',views.addtweetbymodel,name='addtweetbymodel'),
    path('signup/',views.SignUpView.as_view(),name='signup'),
    path("deletetweet/<int:id>",views.deletetweet,name="deletetweet")
]
