from django import forms
from tweetapp.models import Tweet
from django.forms import ModelForm

class AddTweetForm(forms.Form):
    nickname_input = forms.CharField(label="username",max_length=10)
    message_input = forms.CharField(label="Message",max_length=50,
                                    widget=forms.Textarea())
class AddtweeTmodelForm(ModelForm):
    class Meta:
        model = Tweet
        fields=["username","message"]