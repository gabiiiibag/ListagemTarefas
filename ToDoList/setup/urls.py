from django.contrib import admin
from django.urls import path
from toDo.views import toDoListView, toDoCreateView, toDoUpdateView, toDoDeleteView, toDoCompleteView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", toDoListView.as_view(), name="toDo_list"),
    path("create", toDoCreateView.as_view(), name="toDo_create"),
    path("update/<int:pk>", toDoUpdateView.as_view(), name="toDo_update"),
    path("delete/<int:pk>", toDoDeleteView.as_view(), name="toDo_delete"),
    path("complete/<int:pk>", toDoCompleteView.as_view(), name="toDo_complete"),
]
