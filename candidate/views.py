from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.db.models import F
from .forms import (
    GroupCreate,
    DesignationCreate,
    candidateCreate,
    AptitudeCreate,
    MachineCreate,
    FaceCreate,
    MachineCreate,
    StatusCreate,datefilter,datechange
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
from django.contrib.auth.models import User,Group
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator

# Create your views here.
def home(request):
    return render(request, "home.html")

@method_decorator(login_required(login_url='/login'), name='dispatch')
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

@method_decorator(login_required(login_url='/login'), name='dispatch')
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

@method_decorator(login_required(login_url='/login'), name='dispatch')
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

@method_decorator(login_required(login_url='/login'), name='dispatch')
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

@method_decorator(login_required(login_url='/login'), name='dispatch')
class logoutr(TemplateView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("/")

@method_decorator(login_required(login_url='/login'), name='dispatch')
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
            try:
                q.save()
                return redirect("/")
            except:
                return HttpResponse("Aptitude mark Already Created")
            
        else:
            return render(request,"aptitude.html",{'form':form})

@method_decorator(login_required(login_url='/login'), name='dispatch')
class FaceView(TemplateView):
    form = FaceCreate()

    def get(self, request, *args, **kwargs):
        cand = candidate.objects.get(id=kwargs.get("id"))
        # print(kwargs.get("id"))
        return render(
            request, "aptitude.html", {"form": self.form, "data": "Face To Face"}
        )

    def post(self, request, *args, **kwargs):
        print(request.POST)
        form=FaceCreate(request.POST)
        wq=int(request.POST["personality_marks"])+float(request.POST["communication_marks"])+float(request.POST["technical_marks"])+float(request.POST["logical_marks"])
        wq=wq/4
        if form.is_valid():
            q=form.save(commit=False)
            q.Name=candidate.objects.get(id=kwargs.get("id"))
            q.average_marks=wq
            try:
                q.save()
            except:
                return HttpResponse("Face To face Interview mark Already Created")
            return redirect("/")
        else:
            return render(request,"aptitude.html",{'form':form, "data": "Face To Face"})

@method_decorator(login_required(login_url='/login'), name='dispatch')
class MachineView(TemplateView):
    form = MachineCreate()

    def get(self, request, *args, **kwargs):
        cand = candidate.objects.get(id=kwargs.get("id"))
        return render(
            request, "aptitude.html", {"form": self.form, "data": "Machine Test"}
        )

    def post(self, request, *args, **kwargs):
        wq=int(request.POST["logic_marks"])+int(request.POST["problemsolve_marks"])+int(request.POST["Finalout_marks"])
        wq=wq/3
        form=MachineCreate(request.POST)
        if form.is_valid():
            q=form.save(commit=False)
            q.Name=candidate.objects.get(id=kwargs.get("id"))
            q.average_marks=wq
            try:
                q.save()
            except:
                return HttpResponse("Machine mark Already Created")
            return redirect("/")
        else:
            return render(request,"aptitude.html",{'form':form, "data": "Machine Test"})
@method_decorator(login_required(login_url='/login'), name='dispatch')
class CandView(TemplateView):

    def get(self, request, *args, **kwargs):
        data_list=[]
        cand = candidate.objects.all().values("username",
        "FullName", "LastName", "Designation__name", "Experience", "id"
    )
        for i in cand:
            apt=Aptitude.objects.filter(Name__username=i["username"]).values("aptitude_marks")
            fact=FaceToFace.objects.filter(Name__username=i["username"]).values("average_marks")
            mac=MachineMark.objects.filter(Name__username=i["username"]).values("average_marks")
            sta=CandidateStatus.objects.filter(Name__username=i["username"]).values("interview_status")
            try:
                wq=float(apt[0]["aptitude_marks"])+int(fact[0]["average_marks"])+int(mac[0]["average_marks"])
                datad={
                    "id":i["id"],
                    "full":i["FullName"],
                    "last":i["LastName"],
                    "Des":i["Designation__name"],
                    "Experience":i["Experience"],
                    "apt":apt[0]["aptitude_marks"],
                    "fact":fact[0]["average_marks"],
                    "mac":fact[0]["average_marks"],
                    "total":float(wq),
                    "stain":sta[0]["interview_status"]
                }
                data_list.append(datad)
            except:
                wq=0
                datad={
                    "id":i["id"],
                    "full":i["FullName"],
                    "last":i["LastName"],
                    "Des":i["Designation__name"],
                    "Experience":i["Experience"],
                    "apt":0,
                    "fact":0,
                    "mac":0,
                    "total":float(wq),
                    "stain":"NONE"

                }
                data_list.append(datad)
        new = sorted(data_list, key=lambda d: d['total'],reverse=True) 
        # print(new)
        return render(
            request, "candidate_full.html", {"data": new}
        )

@method_decorator(login_required(login_url='/login'), name='dispatch')
class HRCreate(TemplateView):

    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return render(
                request, "aptitude.html", {"data": "HR","form":UserCreationForm}
            )
        else:
            return redirect("/")
    
    def post(self,request,*args, **kwargs):
        form=UserCreationForm(request.POST)
        if form.is_valid():
            q=form.save()
            my_group=Group.objects.get(name='H.R')
            my_group.user_set.add(q)
            return redirect("/")
        else:
            return render(
                request, "aptitude.html", {"data": "HR","form":form}
            )
@method_decorator(login_required(login_url='/login'), name='dispatch')
class InterviewerCreate(TemplateView):

    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return render(
                request, "aptitude.html", {"data": "HR","form":UserCreationForm}
            )
        else:
            return redirect("/")
    
    def post(self,request,*args, **kwargs):
        form=UserCreationForm(request.POST)
        if form.is_valid():
            q=form.save()
            my_group=Group.objects.get(name='Interviewer')
            my_group.user_set.add(q)
            return redirect("/")
        else:
            return render(
                request, "aptitude.html", {"data": "HR","form":form}
            )
@method_decorator(login_required(login_url='/login'), name='dispatch')
class CandDetail(TemplateView):

    def get(self, request, *args, **kwargs):
        cand=candidate.objects.filter(id=kwargs.get("id")).annotate(interviewer=F("Interviewer__username")).values()
        # cand=cand[0].values()
        return render(
                request, "candidatedetail.html", {"data":cand[0]}
            )
        
@method_decorator(login_required(login_url='/login'), name='dispatch')
class MarkView(TemplateView):

    def get(self, request, *args, **kwargs):
        data_list=[]
        cand = candidate.objects.filter(id=kwargs.get("id")).values("username",
        "FullName", "LastName", "Designation__name", "Experience", "id"
    )
        for i in cand:
            apt=Aptitude.objects.filter(Name__username=i["username"]).values("aptitude_marks")
            fact=FaceToFace.objects.filter(Name__username=i["username"]).values("average_marks",'personality_marks', 'communication_marks', 'technical_marks', 'logical_marks')
            mac=MachineMark.objects.filter(Name__username=i["username"]).values("average_marks",'logic_marks', 'problemsolve_marks', 'Finalout_marks')
            sta=CandidateStatus.objects.filter(Name__username=i["username"]).values("interview_status")
            
            try:
                wq=float(apt[0]["aptitude_marks"])+int(fact[0]["average_marks"])+int(mac[0]["average_marks"])
                datad={
                    "First Name":i["FullName"],
                    "Last Name":i["LastName"],
                    "Designation Name":i["Designation__name"],
                    "Experience":i["Experience"],
                    "Aptitude Average Marks":apt[0]["aptitude_marks"],
                    'personality_marks':fact[0]["personality_marks"],
                    'communication_marks':fact[0]["communication_marks"], 
                    'technical_marks':fact[0]["technical_marks"], 
                    'logical_marks':fact[0]["logical_marks"],
                    "Face To Face Average Marks":fact[0]["average_marks"],
                    'logic_marks':mac[0]["logic_marks"],
                    'problemsolve_marks':mac[0]["problemsolve_marks"], 
                    'Finalout_marks':mac[0]["Finalout_marks"],
                    "Machine Average Mark":mac[0]["average_marks"],
                    "Total Marks":float(wq),
                    "Interview Status":sta[0]["interview_status"]
                }
                data_list.append(datad)
            except:
                datad={
                    "First Name":i["FullName"],
                    "Last Name":i["LastName"],
                    "Designation Name":i["Designation__name"],
                    "Experience":i["Experience"]
                }
                data_list.append(datad)
        # new = sorted(data_list, key=lambda d: d['total'],reverse=True) 

        return render(
            request, "markdetail.html", {"data": data_list}
        )



@method_decorator(login_required(login_url='/login'), name='dispatch')
class StatusCV(TemplateView):
    # form=datefilter
    form = StatusCreate

    def get(self, request, *args, **kwargs):
        return render(request, "aptitude.html", {"form": self.form, "data": "Status"})

    def post(self, request, *args, **kwargs):
        form=StatusCreate(request.POST)
        if form.is_valid():
            q=form.save(commit=False)
            q.Name=candidate.objects.get(id=kwargs.get("id"))
            try:
                q.save()
            except:
                return HttpResponse("Status Already Created")
            return redirect("/")
        else:
            return render(request,"aptitude.html",{'form':form, "data": "Status"})

@method_decorator(login_required(login_url='/login'), name='dispatch')
class filterCandidateListView(TemplateView):
    form=datefilter
    data = candidate.objects.all().values(
        "FullName", "LastName", "Designation__name", "Experience", "id","InterviewDate","InterviewT"
    )

    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return render(request, "date.html", {"data": self.data,"form":self.form})
        else:
            return redirect("/")
    
    def post(self, request, *args, **kwargs):
        # form=datefilter(request.POST) 
        data = candidate.objects.filter(InterviewDate=request.POST["date"]).values(
        "FullName", "LastName", "Designation__name", "Experience", "id","InterviewDate","InterviewT"
    )
        return render(request, "date.html", {"data": data,"form":datefilter(request.POST)})

class changedate(TemplateView):
    form=datechange
    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return render(request, "aptitude.html", {"data":"InterviewDate","form":self.form})
        else:
            return redirect("/")
    
    def post(self, request, *args, **kwargs):
        # form=datefilter(request.POST) 
        data = candidate.objects.filter(id=kwargs.get("id")).update(InterviewDate=request.POST["InterviewDate"],InterviewT=request.POST["InterviewT"])
    
        return redirect("/")