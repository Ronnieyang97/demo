from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views import View
from demo_app.models import Book
# Create your views here.
import json
from demo_app.serializers import BookSerialize
from rest_framework.views import APIView
from rest_framework.response import Response


class BookView(APIView):
    def get(self, request):
        return Response(BookSerialize(Book.objects.all(), many=True).data)  # 返回对象为多个有序字典


class BookViewTitle(APIView):
    def get(self, request, title):
        # cantains相当于sql中的like
        return Response(BookSerialize(Book.objects.filter(title__contains=title), many=True).data)


class BookViewAuthor(APIView):
    def get(self, request, author):
        return Response(BookSerialize(Book.objects.filter(author__contains=author), many=True).data)


class BookViewType(APIView):
    def get(self, request, booktype):
        return Response(BookSerialize(Book.objects.filter(booktype__contains=booktype), many=True).data)


class BookViewOne(APIView):
    def get(self, request, dbid):
        target = BookSerialize(Book.objects.get(id=dbid))
        return Response(target.data)

    def put(self, request, dbid):
        target = BookSerialize(Book.objects.get(id=dbid), data=request.data)
        if target.is_valid():
            target.update(target, request.data)
            target.save()
            return Response(target.data)
        else:
            return HttpResponse(target.errors)


class BookCreate(APIView):
    def get(self, request):
        return Response('input the detail')

    def put(self, request):
        if request.data:
            Book.objects.create(id=len(Book.objects.all()) + 1,
                                title=request.data['title'],
                                author=request.data['author'],
                                booktype=request.data['booktype'],
                                introduction=request.data['introduction'])
            return Response(BookSerialize(Book.objects.get(id=len(Book.objects.all()))).data)


def index(request):
    return render(request, 'home.html')



