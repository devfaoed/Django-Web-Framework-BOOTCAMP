from django import forms

from .models import userinfo

class userdata(forms.ModelForm):
    class info:
        model = userinfo
        fields = "__all__"