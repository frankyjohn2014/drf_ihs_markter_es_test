from django.urls import path

from search.views import SearchArticles,Search_range_date,Top_authors

urlpatterns = [
    path('article/<str:query>/', SearchArticles.as_view()),
    path('search_range_date/', Search_range_date.as_view()),
    path('top_authors/', Top_authors.as_view()),
]