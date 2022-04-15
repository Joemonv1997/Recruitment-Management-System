from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import (
    GroupCreate,
    DesignationCreate,
    candidateCreate,
    AptitudeCreate,
    MachineCreate,
    FaceCreate,
    MachineCreate,
    StatusCreate,
)
from .models import (
    candidate,
    Designation,
    Aptitude,
    FaceToFace,
    MachineMark,
    CandidateStatus,
)
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect

# Create your views here.
def home(request):
    return render(request, "home.html")


class GroupView(TemplateView):
    form = GroupCreate

    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return render(request, "groupcreate.html", {"form": self.form})
        else:
            return redirect("/")

    def post(self, request, *args, **kwargs):
        form = GroupCreate(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            return render(request, "groupcreate.html", {"form": form})


class DesignationView(TemplateView):
    form = DesignationCreate

    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return render(request, "designation.html", {"form": self.form})
        else:
            return redirect("/")

    def post(self, request, *args, **kwargs):
        form = DesignationCreate(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            return render(request, "designation.html", {"form": form})


class CandidateView(TemplateView):
    form = candidateCreate()

    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return render(request, "candidate.html", {"form": self.form})
        else:
            return redirect("/")

    def post(self, request, *args, **kwargs):
        form = candidateCreate(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            return render(request, "candidate.html", {"form": form})


class CandidateListView(TemplateView):
    data = candidate.objects.all().values(
        "FullName", "LastName", "Designation__name", "Experience", "id"
    )

    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return render(request, "candidatelist.html", {"data": self.data})
        else:
            return redirect("/")


class loginrequest(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, "login.html")

    def post(self, request, *args, **kwargs):
        user = authenticate(
            request, username=request.POST["uname"], password=request.POST["psw"]
        )
        if user is not None:
            login(request, user)
            redirect("/")
        else:
            return HttpResponse("Authentication Failed")
        return redirect("/")


class logoutr(TemplateView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("/")


class AptitudeView(TemplateView):
    form = AptitudeCreate()

    def get(self, request, *args, **kwargs):
        return render(request, "aptitude.html", {"form": self.form, "data": "Aptitude"})

    def post(self, request, *args, **kwargs):
        # pass
        form=AptitudeCreate(request.POST)
        if form.is_valid():
            q=form.save(commit=False)
            q.Name=candidate.objects.get(id=kwargs.get("id"))
            q.save()
            return redirect("/")
        else:
            return render(request,"candidate.html",{'form':form})


class FaceView(TemplateView):
    form = FaceCreate()

    def get(self, request, *args, **kwargs):
        cand = candidate.objects.get(id=kwargs.get("id"))
        print(cand)
        # print(kwargs.get("id"))
        return render(
            request, "aptitude.html", {"form": self.form, "data": "Face To Face"}
        )

    def post(self, request, *args, **kwargs):
        pass
        # form=candidateCreate(request.POST)
        # if form.is_valid():
        #     form.save()
        #     return redirect("/")
        # else:
        #     return render(request,"candidate.html",{'form':form})


class MachineView(TemplateView):
    form = MachineCreate()

    def get(self, request, *args, **kwargs):
        cand = candidate.objects.get(id=kwargs.get("id"))
        print(cand)
        # print(kwargs.get("id"))
        return render(
            request, "aptitude.html", {"form": self.form, "data": "Machine Test"}
        )

    def post(self, request, *args, **kwargs):
        pass
        # form=candidateCreate(request.POST)
        # if form.is_valid():
        #     form.save()
        #     return redirect("/")
        # else:
        #     return render(request,"candidate.html",{'form':form})
