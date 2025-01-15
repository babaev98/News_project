from django import forms
from .models import Post, Author, Category
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group


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


class BasicSignupForm(SignupForm):
    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        basic_group = Group.objects.get(name='common')
        basic_group.user_set.add(user)
        return user

