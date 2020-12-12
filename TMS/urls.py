
from django.contrib import admin
from django.urls import path
from . import views


app_name='TMS'


urlpatterns = [
    path("",views.register,name="UserRegistration"),
    path("history/",views.history,name="Travel_History"),
    path("hospital/",views.hospital,name="hospital"),
    path("feedback/",views.feedback,name="feedback"),
    path("test/",views.test,name="test"),
    path("signup/",views.signup,name="signup"),
    path("login/",views.login_view  ,name="login_view"),
    path("logout/",views.logout_view  ,name="logout_view"),

]

