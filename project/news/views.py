from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .filters import NewFilter
from .forms import NewsForm, ArticlesForm


class PostsList(ListView):
    model = Post
    ordering = '-date_time_created'
    template_name = 'news.html'
    context_object_name = 'posts'
    paginate_by = 10


class PostsListSearch(PostsList):
    template_name = 'news_search.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'new'


class NewsCreate(CreateView):
    form_class = NewsForm
    model = Post
    template_name = 'news_edit.html'

    def form_valid(self, form):
        news = form.save(commit=False)
        news.article_or_news = True
        return super().form_valid(form)


class ArticlesCreate(CreateView):
    form_class = NewsForm
    model = Post
    template_name = 'news_edit.html'

    def form_valid(self, form):
        news = form.save(commit=False)
        news.article_or_news = False
        return super().form_valid(form)


class NewsUpdate(UpdateView):
    form_class = NewsForm
    model = Post
    template_name = 'news_edit.html'


class NewsDelete(DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news_list')


