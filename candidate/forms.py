from django.contrib.auth.models import User, Group
from django.forms import Form, ModelForm,ModelChoiceField
from .models import (
    Designation,
    candidate,
    Aptitude,
    FaceToFace,
    MachineMark,
    CandidateStatus,
)

from datetime import date
class GroupCreate(ModelForm):
    class Meta:
        model = Group
        fields = ["name"]


class DesignationCreate(ModelForm):
    class Meta:
        model = Designation
        fields = "__all__"


class candidateCreate(ModelForm):
    Interviewer=ModelChoiceField(queryset=User.objects.filter(groups__name="Interviewer"))
    class Meta:
        model = candidate
        fields="__all__"


class AptitudeCreate(ModelForm):
    class Meta:
        model = Aptitude
        exclude = ["Name","average_marks"]


class FaceCreate(ModelForm):
    class Meta:
        model = FaceToFace
        exclude = ["Name","average_marks"]


class MachineCreate(ModelForm):
    class Meta:
        model = MachineMark
        exclude = ["Name","average_marks"]


class StatusCreate(ModelForm):
    class Meta:
        model = CandidateStatus
        exclude = ["Name"]

class datefilter(Form):
    date=ModelChoiceField(queryset=candidate.objects.all().values_list('InterviewDate',flat=True).distinct(),required=False,initial=date.today(),empty_label=None)
    # InterviewT=ModelChoiceField(queryset=candidate.objects.all().values_list('InterviewT',flat=True).distinct(),required=False)

class datechange(ModelForm):
    class Meta:
        model = candidate
        fields=["InterviewDate","InterviewT"]