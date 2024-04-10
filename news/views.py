from typing import Any
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views.generic import DetailView, ListView
from .models import *

class NewsDetailView(DetailView):
    model = News
    
    def get(self, request, *args, **kwargs):
        news = self.get_object()
        news.views += 1
        news.save()
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        if 'like' in request.POST.keys():
            try:
                reaction = Reaction.objects.get(is_like=request.POST['like']=='like', user=request.user, news=self.get_object())
                reaction.delete()
            except Reaction.DoesNotExist:
                new_reaction = Reaction(is_like=request.POST['like']=='like', user=request.user, news=self.get_object())
                try:
                    last_reaction = Reaction.objects.get(is_like=request.POST['like']!='like', user=request.user, news=self.get_object())
                    last_reaction.delete()
                finally:
                    new_reaction.save()
            finally:
                return JsonResponse({"likes_count": self.get_object().get_likes_count(), "dislikes_count": self.get_object().get_dislikes_count()})
        return super().get(request, *args, **kwargs)
    
    
class NewsListView(ListView):
    model = News
    paginate_by = 3
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["max"] = self.get_paginator(self.get_queryset(), 3).num_pages
        return context
    
    def get(self, request, *args, **kwargs):
        paginator = self.get_paginator(self.get_queryset(), 3)
        if 'next_news' in request.GET.keys() and paginator.num_pages >= int(request.GET.get('next_news')):
            return JsonResponse({"max": paginator.num_pages, "page": request.GET.get('next_news'), "news": [news.get_html() for news in paginator.get_page(request.GET.get('next_news'))] })
        return super().get(request, *args, **kwargs)

    
def news_by_tag(request, pk):
    news = News.objects.filter(tags__in=[Tag.objects.get(pk=pk)])
    return render(request, 'news/news_list.html', context={"object_list": news, "tag": Tag.objects.get(pk=pk)})

class StatisticView(ListView):
    model = News
    template_name = "news/statistic.html"