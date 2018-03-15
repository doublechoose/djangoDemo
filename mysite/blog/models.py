from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils import timezone


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
                     self).get_queryset() \
            .filter(status='published')


class Post(models.Model):
    # status 状态 草稿与发布
    # 元组 元组的元素不能修改
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    author = models.ForeignKey(User,
                               related_name='blog_posts',
                               on_delete=models.CASCADE)
    # 转为TEXT
    body = models.TextField()
    # 设置当post发布的时候，时间设置
    publish = models.DateTimeField(default=timezone.now)
    # 创建的时候，自动保存时间
    created = models.DateTimeField(auto_now_add=True)
    # 上一次更新的时候，自动保存更新时间
    updated = models.DateTimeField(auto_now=True)
    # 显示post 的状态，默认为草稿
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[
                           self.publish.year,
                           self.publish.strftime('%m'),
                           self.publish.strftime('%d'),
                           self.slug
                       ])

    # 告诉jango 排序结果，降序
    class Meta:
        ordering = ('-publish',)

    objects = models.Manager()  # the default manager
    published = PublishedManager()  # Our custom manager

    # 提供对象的可读性
    def __str__(self):
        return self.title
