from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views import View
from demo_app.models import Book
# Create your views here.
import json
# from django.core import serializers as se
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response


class BookSerialize(serializers.Serializer):  # 对应.models中的Book类设置
    title = serializers.CharField(max_length=30)
    author = serializers.CharField(max_length=20)
    booktype = serializers.CharField(max_length=10)
    introduction = serializers.CharField(max_length=1024)


class BookView(APIView):
    def get(self, request):
        # title = '1984'
        # target = se.serialize("json", Book.objects.all())  # django内置的序列化
        target = BookSerialize(Book.objects.all(), many=True)  # many的设置意为序列化所有
        return Response(target.data)  # 返回对象为多个有序字典

    def post(self, request):
        pass


class BookViewTitle(APIView):
    def get(self, request, title):
        target = BookSerialize(Book.objects.filter(title=title), many=True)
        print(title)
        return Response(target.data)


def index(request):
    return render(request, 'home.html')
