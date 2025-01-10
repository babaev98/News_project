from django.urls import path
from .views import (PostsList, PostDetail, PostsListSearch, NewsCreate, NewsUpdate, NewsDelete, ArticlesCreate)

urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем товарам у нас останется пустым,
   # чуть позже станет ясно почему.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
   path('', PostsList.as_view(), name='news_list'),
   path('<int:pk>', PostDetail.as_view(), name='new_detail'),
   path('search/', PostsListSearch.as_view(), name='news_search'),
   path('news/create/', NewsCreate.as_view(), name='news_create'),
   path('news/<int:pk>/update/', NewsUpdate.as_view(), name='news_update'),
   path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
   path('articles/create/', ArticlesCreate.as_view(), name='articles_create'),
   path('articles/<int:pk>/update/', NewsUpdate.as_view(), name='news_update'),
   path('articles/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
]