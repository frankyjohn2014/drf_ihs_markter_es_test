from rest_framework import serializers
from blog_ihs.models import Article,User
from blog_ihs.models import User
class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(max_length=256)
    class Meta:
        model = User
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    paragraph = serializers.CharField(max_length=256)
    author = serializers.CharField(max_length=256)
    created_datetime = serializers.DateTimeField(allow_null=True)

    class Meta:
        model = Article
        # fields = '__all__'
        fields = '__all__'