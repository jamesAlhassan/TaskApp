from django.urls import path, include
from .views import index, updata_task

urlpatterns = [
    path("",index, name="index"),
    path("update/<int:pk>/",updata_task, name="update"),
]