from django.urls import path
from . import views

urlpatterns = [
    path('queri/', views.querris, name='queri'),
    path('update/<int:id>', views.update, name='update'),
]