from django.contrib.auth.models import User,Group
from django.forms import Form,ModelForm
from .models import Designation,candidate
class GroupCreate(ModelForm):
    class Meta:
        model=Group
        fields=["name"]


class DesignationCreate(ModelForm):
    class Meta:
        model=Designation
        fields="__all__"

class candidateCreate(ModelForm):
    class Meta:
        model=candidate
        fields="__all__"