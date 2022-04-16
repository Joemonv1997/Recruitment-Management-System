from . import views

from django.urls import path, include

urlpatterns = [
    path("", views.home, name="home"),
    path("group", views.GroupView.as_view(), name="group"),
    path("designation", views.DesignationView.as_view(), name="desi"),
    path("candidate", views.CandidateView.as_view(), name="cand"),
    path("candlist", views.CandidateListView.as_view(), name="candlist"),
    path("login", views.loginrequest.as_view(), name="loginrequ"),
    path("logout", views.logoutr.as_view(), name="logoutrequ"),
    path("apt/<int:id>", views.AptitudeView.as_view(), name="Aptitude"),
    path("face/<int:id>", views.FaceView.as_view(), name="face"),
    path("machine/<int:id>", views.MachineView.as_view(), name="machine"),
    path("candmark",views.CandView.as_view(),name="candm"),
    path("HRCreate",views.HRCreate.as_view(),name="HR"),
    path("Interviewe",views.InterviewerCreate.as_view(),name="Interviewer")
]
