from django.urls import path
from . import views
urlpatterns=[
    path("planner/",views.plannerex,name = 'plannerex'),
    path("Home/",views.Homepage,name = 'Homepage'),
    path("add/",views.ind,name = 'ind'),
    path("add1/",views.ind1,name = 'ind1'),
    path("Home/addd/",views.addrecord,name = "addrecord"),
    path("Home/addd1/",views.addrecord1,name = "addrecord1"),
    path("register/",views.registerpage,name = 'registerpage'),
    path("login/",views.loginpage,name = 'loginpage'),
    path("thankyou/",views.thankyoupage,name = 'thankyoupage'),
]