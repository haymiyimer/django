from django.urls import path
from.import views

urlpatterns=[
    path('', views.about),
    path('', views.index),

    path('',views.portfolio) ,
    path('',views.blog),
    path('',  views.contact),
    path('',views.services),
    path('', views.team)
]