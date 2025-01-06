from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_rating = models.IntegerField(default=0)

    def update_rating(self):
        rating = 0
        list_post = list(Post.objects.filter(author = self.pk))
        for x in list_post:
            rating += rating + (x.rating * 3)
            list_comm = Comment.objects.filter(post = x.pk)
            for y in list_comm:
                rating += y.rating
        list_comm = list(Comment.objects.filter(user = self.user))
        for x in list_comm:
            rating += x.rating
        return rating
"""        post = sum(self_pk.Post_set.all('rating')) * 3
        comment = sum(self_pk.Comment_set.all('rating'))
        post_comment = self_pk.Post_set.all('pk')
        post_comment = sum(post_comment.Comment_set.all('rating'))
        return post + comment + post_comment"""


class Category(models.Model):
    category = models.CharField(unique=True, max_length=100)


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    # False = Статья | True = Новость
    article_or_news = models.BooleanField()
    date_time_created = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField('Category', through='PostCategory')
    title = models.CharField(max_length=100)
    text = models.TextField()
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        tx = self.text[0:125] + '...'
        return tx


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date_time_created = models.DateTimeField(auto_now=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
