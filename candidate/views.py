from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import GroupCreate
from django.shortcuts import redirect
# Create your views here.
def home(request):
    return render(request,"home.html")


class GroupView(TemplateView):
    form=GroupCreate
    def get(self,request,*args, **kwargs):
        if request.user.is_superuser:
            return render(request,"groupcreate.html",{'form':self.form})
        else:
            return redirect("/")
    def post(self,request,*args, **kwargs):
        form=GroupCreate(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            return render(request,"groupcreate.html",{'form':form})
