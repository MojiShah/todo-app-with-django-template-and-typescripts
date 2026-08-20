from django.urls import path;
from . import views

urlpatterns=[
    path('',view=views.TodoListView.as_view(),name='todo_list'),
    path('<int:pk>/',view=views.TodoDetailView.as_view(),name='todo-detail'),
    path('create/',view=views.TodoCreateView.as_view(),name='todo-create'),
    path('<int:pk>/update/',view=views.TodoUpdateView.as_view(),name='todo-update'),
    path('<int:pk>/delete/',view=views.TodoDeleteView.as_view(),name='todo-delete'),
];