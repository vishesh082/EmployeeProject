from django.urls import path
from EmployeeDetail import views

urlpatterns = [
    path('', views.index),
    path('views/', views.display_),
    path('delete/<int:id>/', views.delete_, name="deletedata")
]
