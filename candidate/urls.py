from . import views

from django.urls import path,include

urlpatterns = [
    path("",views.home,name="home"),
    path("group",views.GroupView.as_view(),name="group"),
    path("designation",views.DesignationView.as_view(),name="desi"),
    path("candidate",views.CandidateView.as_view(),name="cand"),
    path("candlist",views.CandidateListView.as_view(),name="candlist"),
    path("login",views.loginrequest.as_view(),name="loginrequ"),
    path("logout",views.logoutr.as_view(),name="logoutrequ"),

]
