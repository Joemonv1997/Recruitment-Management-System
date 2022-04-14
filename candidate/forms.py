from django.contrib.auth.models import User,Group
from django.forms import Form,ModelForm

class GroupCreate(ModelForm):
    class Meta:
        model=Group
        fields=["name"]