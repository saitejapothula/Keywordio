from django.shortcuts import render,redirect
from app.forms import BookForm
from app.models import Book
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from app.serializers import BookSerializer


# Create your views here.

@login_required()
def bookview(request):
    form = BookForm()
    template_name = "app/book.html"
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request,template_name,context)

def updateview(request,id):
    obj = Book.objects.get(id=id)
    form = BookForm(instance=obj)
    template_name = "app/book.html"
    if request.method=="POST":
        form = BookForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect ('adminurl')
    context = {'form':form}
    return render(request,template_name,context)

def deleteview(request,id):
    obj = Book.objects.get(id=id)
    template_name = "app/confirm.html"
    context = {'data':obj}
    if request.method == "POST":
        obj.delete()
        return redirect ('adminurl')
   
    return render(request,template_name,context)

@login_required()
def adminview(request):
    obj = Book.objects.all()
    template_name = "app/show.html"
    context = {'obj':obj}
    return render(request, template_name,context)

def studentview(request):
    obj = Book.objects.all()
    template_name = "app/showbook.html"
    context = {'obj':obj}
    return render(request, template_name,context)


class BookApi(APIView):
    def get(self, request):
        lap = Book.objects.all()
        serializer = BookSerializer(lap, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BookForm(data= request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class BookInfo(APIView):
    def get(self,request,id):
        try:
            lap = Book.objects.get(id=id)
        except Book.DoesNotExist:
            msg = {'msg':'Book Does not exists'}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        serializer = BookSerializer(lap)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self,request,id):
        try:
            lap = Book.objects.get(id=id)
        except Book.DoesNotExist:
            msg = {'msg':'Book Does not Exists'}
        serializer = BookSerializer(lap, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,id):
        try:
            lap = Book.objects.get(id=id)
        except Book.DoesNotExist:
            msg = {'msg':'Book Does not Exists'}
        serializer = BookSerializer(lap, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        try:
            lap = Book.objects.get(id=id)
        except Book.DoesNotExist:
            msg = {'msg':'Book Does not Exists'}
        lap.delete()
        return Response({'msg':'Record Deleted'}, status=status.HTTP_204_NO_CONTENT)
    
    