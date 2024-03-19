from django.urls import path
from.import views

urlpatterns=[
    path('',views.new),

    path('codding/', views.codding),
    path('student/',views.student),
    path('teacher/',views.teacher) ,
    path('insertstudents/',views.insertstudents)

]