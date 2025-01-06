from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_rating = models.IntegerField(default=0)

    def update_rating(self):
        post_rating = 0
        comment_rating = 0
        comment_post_rating = 0

        list_post = Post.objects.filter(author=self)
        for p in list_post:
            post_rating += p.rating

        list_comm = Comment.objects.filter(user=self.user)
        for c in list_comm:
            comment_rating += c.rating

        list_comm_post = Comment.objects.filter(post__author=self)
        for cp in list_comm_post:
            comment_post_rating += cp.rating

        self.user_rating = post_rating * 3 + comment_rating + comment_post_rating
        self.save()


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
