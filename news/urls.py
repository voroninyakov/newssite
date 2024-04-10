from django.urls import path
from .api_views import *
from .views import *

app_name = "news"

urlpatterns = [
    path('', NewsListView.as_view(), name='main'),
    path('news/<pk>/', NewsDetailView.as_view(), name='news_detail'),
    path('tag/<pk>/', news_by_tag, name='news_by_tag'),
    path('statictic/', StatisticView.as_view(), name='statistic'),
    # api
    path('api/news/', NewsListApiView.as_view(), name="news_list_api"),
    path('api/news/<pk>', NewsDetailApiView.as_view(), name="news_detail_api"),
]
