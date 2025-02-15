from django.shortcuts import render,redirect
from . import models
from django.urls import reverse,reverse_lazy
from tweetapp.forms import AddTweetForm,AddtweeTmodelForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView


# Create your views here.

def listtweet(request):
    all_tweets=models.Tweet.objects.all()
    tweet_dic = {"tweets":all_tweets}
    return render(request, 'tweetapp/listtweet.html',context=tweet_dic)

@login_required(login_url="/login")
def addtweet(request):
    if request.POST:
        
        message=request.POST["message"]
        models.Tweet.objects.create(username=request.user,message=message)
        return redirect(reverse('tweetapp:listtweet'))
    else:
        
        return render(request, 'tweetapp/addtweet.html')
    
def adtweetbyform(request):
    if request.method=="POST": 
        form=AddTweetForm(request.POST)
        if form.is_valid():
            nickname = form.cleaned_data["nickname_input"]
            message = form.cleaned_data["message_input"]
            models.Tweet.objects.create(nickname=nickname,message=message)

            return redirect(reverse('tweetapp:listtweet'))
        
        else:
            print("error in forma")
            return render (request,'tweetapp/adtweetbyform.html',context={"form":form})
    else:
        form = AddTweetForm()
        return render (request,'tweetapp/adtweetbyform.html',context={"form":form})

def addtweetbymodel(request):
     if request.method=="POST": 
        form=AddtweeTmodelForm(request.POST)
        if form.is_valid():
            nickname = form.cleaned_data["nickname"]
            message = form.cleaned_data["message"]
            models.Tweet.objects.create(nickname=nickname,message=message)

            return redirect(reverse('tweetapp:listtweet'))
        
        else:
            print("error in form")
            return render (request,'tweetapp/addtweetbymodel.html',context={"form":form})
     else:
        form = AddtweeTmodelForm()
        return render (request,'tweetapp/addtweetbymodel.html',context={"form":form})
@login_required
def deletetweet(request,id):
    tweet=models.Tweet.objects.get(pk=id)
    if request.user == tweet.username:
        models.Tweet.objects.filter(id=id).delete()
        return redirect("tweetapp:listtweet")


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name ="registration/signup.html"
