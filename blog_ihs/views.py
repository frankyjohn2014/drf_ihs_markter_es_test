from django.shortcuts import render
from rest_framework import viewsets
from blog_ihs.models import Article,User
from blog_ihs.serializers import ArticleSerializer,UserSerializer
from rest_framework.renderers import TemplateHTMLRenderer,JSONRenderer
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    # renderer_classes = [TemplateHTMLRenderer]
    # template_name = 'profile_list.html'

    serializer_class = UserSerializer
    queryset = User.objects.all()
    # print(queryset)

    # def get(self, request):
    #     queryset = User.objects.all()
    #     return Response({'profile1': queryset})


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
