from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveDestroyAPIView, ListCreateAPIView
from .serializers import NewsSerializer
from .models import News

class NewsListApiView(ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class NewsDetailApiView(RetrieveDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

