from django import forms

class userinput(forms.Form):
    q=forms.CharField(required=True,max_length=15,label='Input #hashtag')