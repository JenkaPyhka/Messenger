from django.urls import path
from . import views

urlpatterns = [
    path('', views.auth, name='home'),
    path('reg', views.reg, name='reg'),
    path('log', views.log, name='log'),
]
