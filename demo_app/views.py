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
    id = serializers.CharField(max_length=10)
    title = serializers.CharField(max_length=30)
    author = serializers.CharField(max_length=20)
    booktype = serializers.CharField(max_length=10)
    introduction = serializers.CharField(max_length=1024)

    def create(self, validated_data):
        self.title, self.author, self.booktype, self.introduction = validated_data['title'], \
                                                                    validated_data['author'], \
                                                                    validated_data['booktype'], \
                                                                    validated_data['introduction']
        self.save()
        return self

    def update(self, instance, validated_data):
        # 提交更新数据时必须重写update方法（serializers.Serializer中的update方法为空并且只会返回一个报错）
        instance.title, instance.author, instance.booktype, instance.introduction = validated_data['title'], \
                                                                                    validated_data['author'], \
                                                                                    validated_data['booktype'], \
                                                                                    validated_data['introduction']
        instance.save()
        return instance


class BookView(APIView):
    def get(self, request):
        target = BookSerialize(Book.objects.all(), many=True)  # many的设置意为序列化所有
        return Response(target.data)  # 返回对象为多个有序字典

    def post(self, request):
        pass


class BookViewTitle(APIView):
    def get(self, request, title):
        target = BookSerialize(Book.objects.filter(title__contains=title), many=True)  # cantains相当于sql中的like
        return Response(target.data)


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
    def get(self):
        return HttpResponse('input the detail')

    def put(self, request):
        target = BookSerialize(request.data, data=request.data)
        if target.is_valid():
            target.create(target.data)
            target.save()
        else:
            return HttpResponse(target.errors)


def index(request):
    return render(request, 'home.html')
