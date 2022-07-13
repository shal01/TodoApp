from django.shortcuts import render
from rest_framework.views import APIView,status
from API.models import Todos
from rest_framework.response import Response
from API.serializer import UserSerializer,TodoSerializer
from django.contrib.auth.models import User

# Create your views here.
class TodoView(APIView):
    def get(self,request,*args,**kwargs):
        qs=Todos.objects.all()
        serializer=TodoSerializer(qs,many=True)
        return Response(serializer.data)
    def post(self,request,*args,**kwargs):
        serializer=TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

# detail of a specific todo with given id

class TodoDetails(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("todo_id")
        todo=Todos.objects.get(id=id)
        serializer=TodoSerializer(todo)
        return Response(serializer.data)
    def post(self,request,*args,**kwargs):
        id=kwargs.get("todo_id")
        todo=Todos.objects.get(id=id)
        serializer=TodoSerializer(instance=todo,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self,request,*args,**kwargs):
            id = kwargs.get("todo_id")
            todo = Todos.objects.get(id=id)
            todo.delete()
            return Response({"msg": "deleted"})




# url=> api/v1/todos
# todo create
# todo detail
# todo list
# todo update
# todo delete



class UserCreationView(APIView):
    def post(self,request,*args,**kwargs):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            # first_name=serializer.validated_data("first_name")
            # last_name=serializer.validated_data("last_name")
            # username=serializer.validated_data("username")
            # email=serializer.validated_data.get('email')
            # password=serializer.validated_data.get('password')
            # User.objects.create_user(first_name=first_name,
            #                          last_name=last_name,
            #                          username=username,
            #                          email=email,
            #                          password=password)
            # print(serializer.validated_data)
            # serializer.save()
            User.objects.create_user(**serializer.validated_data)   #**used for changing  the post values into dictionary
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



