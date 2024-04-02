from django.contrib import admin
from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, UpdateView, TaskUpdate, DeleteTask, CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('tasks', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', DeleteTask.as_view(), name='task-delete'),


]
