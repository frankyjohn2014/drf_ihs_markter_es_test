import abc
from django.http import HttpResponse
from elasticsearch_dsl import Search, Q
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.views import APIView
from blog_ihs.documents import ArticleDocument,UserDocument
from blog_ihs.serializers import ArticleSerializer, UserSerializer
from elasticsearch import Elasticsearch
from elasticsearch_dsl.query import MultiMatch
import datetime
from blog_ihs.models import User
from collections import defaultdict
import json 
from django.shortcuts import render

class PaginatedElasticSearchAPIView(APIView, LimitOffsetPagination):
    serializer_class = None
    document_class = None

    @abc.abstractmethod
    def generate_q_expression(self, query):
        """This method should be overridden
        and return a Q() expression."""

    def get(self, request, query):
        try:
            q = self.generate_q_expression(query)
            search = self.document_class.search().query(q)
            response = search.execute()
            print(f'Found {response.hits.total.value} hit(s) for query: "{query}"')
            results = self.paginate_queryset(response, request, view=self)
            serializer = self.serializer_class(results, many=True)
            return self.get_paginated_response(serializer.data)
        except Exception as e:
            return HttpResponse(e, status=500)

class Search_range_date(APIView,LimitOffsetPagination):
    serializer_class = ArticleSerializer
    document_class = ArticleDocument

    def get(self, request):
        try:
            search = self.document_class.search().filter('range', created_datetime={'gt': 2019, 'lte': 2021})
            response = search.execute()
            print(f'Found {response.hits.total.value} hit(s) for query: "{search}"')
            results = self.paginate_queryset(response, request, view=self)
            serializer = self.serializer_class(results, many=True)
            return self.get_paginated_response(serializer.data)
        except Exception as e:
            return HttpResponse(e, status=500)

class Top_authors(PaginatedElasticSearchAPIView):
    serializer_class = UserSerializer
    document_class = UserDocument
    def get(self, request):
        try:
            top_authors_raw = []
            top_authors = []
            top_authors_value = []
            authors_to_html = []
            articles_authors = []
            result = User.objects.values('full_name').distinct()
            for i in range(1,result.count()):
                names = list(result[i].values())
                search = self.document_class.search().query('match', full_name='%s'% names).execute()
                search_articles_authors = self.document_class.search().query('match', article='%s'% names).execute()
                print(search_articles_authors)
                count_articles_of_authors = search.hits.total.value
                top_authors_raw.append(names)
                top_authors_value.append(count_articles_of_authors)
            for i in top_authors_raw:
                top_authors.append(i[0])
            zip_iterator = zip(top_authors, top_authors_value)
            dict_top_names = dict(zip_iterator)
            sorted_top = sorted(dict_top_names.items(), key=lambda x: x[1], reverse=True)
            count = 0
            for i in sorted_top:
                count += 1
                authors_to_html.append(str(count) + ' ' + i[0] + ' posted ' + str(i[1]) + ' article(s)')
            return render(request, 'profile_list.html', {'profiles': authors_to_html[0:10]})
        except Exception as e:
            return HttpResponse(e, status=500)

class SearchArticles(PaginatedElasticSearchAPIView):
    serializer_class = ArticleSerializer
    document_class = ArticleDocument

    def generate_q_expression(self, query):
        return Q(
                'multi_match', query=query,
                fields=[
                    'paragraph',
                    'author.full_name',
                ], fuzziness='auto')            



