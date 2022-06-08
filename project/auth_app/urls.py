from django.urls import path
from auth_app.views import registerview,loginview,logoutview

urlpatterns = [
    path('rv/',registerview,name='registerurl'),
    path('lv/',loginview,name='loginurl'),
    path('lov/',logoutview,name='logouturl')
]