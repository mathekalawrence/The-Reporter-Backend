from django.urls import path
from .views import *

#urls

urlpatterns = [
    path('users/list/', UsersListApiView.as_view()),
    path('reports/list/', ReportsListApiView.as_view()),
]
