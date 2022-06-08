from django.urls import path
from app.views import bookview, studentview,adminview, updateview, deleteview, BookApi, BookInfo

urlpatterns=[
    path('bv/',bookview, name='bookurl'),
    path('sv/',studentview,name='studenturl'),
    path('av/',adminview,name='adminurl'),
    path('uv<int:id>/',updateview,name='updateurl'),
    path('dv<int:id>/',deleteview,name="deleteurl"),
    path('ba/',BookApi.as_view(),name='bookapiurl'),
    path('bi/<int:id>/',BookInfo.as_view(),name='bookinfourl')
]