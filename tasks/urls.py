from django.urls import path, include
from .views import index, updata_task, delete_task

urlpatterns = [
    path("",index, name="home"),
    path("update/<int:pk>/",updata_task, name="update_task"),
    path("delete/<int:pk>/",delete_task, name="delete_task"),
]