from django_filters import FilterSet, DateFilter, ModelChoiceFilter, CharFilter
from .models import Post, Author
from django import forms


class NewFilter(FilterSet):

    title = CharFilter(
        lookup_expr='icontains',
        label='Заголовок',
    )

    date_time_created = DateFilter(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Дата',
        lookup_expr='date__gte',

    )

    author = ModelChoiceFilter(
        queryset=Author.objects.all(),
        label='Автор',
        empty_label='Все авторы'
    )
