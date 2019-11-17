from rest_framework import serializers


class BookSerialize(serializers.Serializer):  # 对应.models中的Book类设置
    id = serializers.CharField(max_length=10)
    title = serializers.HyperlinkedIdentityField(view_name='get_id',
                                                 lookup_url_kwarg='id',
                                                 lookup_field=id,
                                                 )
    author = serializers.CharField(max_length=20)
    booktype = serializers.CharField(max_length=10)
    introduction = serializers.CharField(max_length=1024)

    def update(self, instance, validated_data):
        # 提交更新数据时必须重写update方法（serializers.Serializer中的update方法为空并且只会返回一个报错）
        instance.title, instance.author, instance.booktype, instance.introduction = validated_data['title'], \
                                                                                    validated_data['author'], \
                                                                                    validated_data['booktype'], \
                                                                                    validated_data['introduction']
        instance.save()
        return instance

