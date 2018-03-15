from django.contrib.auth.models import User
from django.db import models
from taggit.managers import TaggableManager

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
    tags = TaggableManager()

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[
                           self.publish.year,
                           self.publish.strftime('%m'),
                           self.publish.strftime('%d'),
                           self.slug
                       ])

    # 告诉django 排序结果，降序
    class Meta:
        ordering = ('-publish',)

    objects = models.Manager()  # the default manager
    published = PublishedManager()  # Our custom manager

    # 提供对象的可读性
    def __str__(self):
        return self.title


class Comment(models.Model):
    # 评论的数据模型
    # 对哪个post的评论
    # 谁评论
    # 邮箱
    # 评论的内容
    # 创建时间
    # 更新时间
    # active 用于屏蔽
    # related_name 允许我们命名不适当的评论
    post = models.ForeignKey(Post, related_name='comments',on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name,self.post)
