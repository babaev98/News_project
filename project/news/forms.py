from django import forms
from .models import Post, Author, Category


class NewsForm (forms.ModelForm):
    title = forms.CharField(min_length=10, label='Заголовок')
    text = forms.CharField(min_length=10, label='Содержание', widget=forms.Textarea)
    author = forms.ModelChoiceField(queryset=Author.objects.all(), label='Автор', empty_label='Выберете автора')
    category = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), label='Категории')

    class Meta:
        model = Post
        fields = [
            'author',
            'title',
            'text',
            'category',
        ]


class ArticlesForm (NewsForm):
    article_or_news = False