from django.contrib.auth.models import User, Group
from django.forms import Form, ModelForm
from .models import (
    Designation,
    candidate,
    Aptitude,
    FaceToFace,
    MachineMark,
    CandidateStatus,
)


class GroupCreate(ModelForm):
    class Meta:
        model = Group
        fields = ["name"]


class DesignationCreate(ModelForm):
    class Meta:
        model = Designation
        fields = "__all__"


class candidateCreate(ModelForm):
    class Meta:
        model = candidate
        fields = "__all__"


class AptitudeCreate(ModelForm):
    class Meta:
        model = Aptitude
        exclude = ["Name"]


class FaceCreate(ModelForm):
    class Meta:
        model = FaceToFace
        exclude = ["Name"]


class MachineCreate(ModelForm):
    class Meta:
        model = MachineMark
        exclude = ["Name"]


class StatusCreate(ModelForm):
    class Meta:
        model = CandidateStatus
        exclude = ["Name"]
