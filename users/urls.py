from django.urls import path 
from users.views import home, register, salaries, RH_Campagnies, admin_WebApps
urlpatterns= [
    path("", home, name= "home"),
    path("register", register, name="register"),
    path("salaries", salaries, name="salaries"),
    path("RH_Campagnies", RH_Campagnies, name="RH_Campagnies"),
    path("admin_WebApps", admin_WebApps, name="admin_WebApps"),
]