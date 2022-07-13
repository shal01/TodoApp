from django.urls import path
from API import views
urlpatterns = [
    path("todos",views.TodoView.as_view()),
    path("todos/<int:todo_id>",views.TodoDetails.as_view()),
    path("users/accounts/signin",views.UserCreationView.as_view()),

]