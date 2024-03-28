from django.urls import path,include
from Guest import views


app_name="webguest"

urlpatterns = [

    path('',views.Main,name="Landing Page"),

    path('filmuploader/',views.filmuploader,name="Film Uploader"),
    path('user/',views.user,name="User"),
    path('login/',views.login,name="Login"),
]
