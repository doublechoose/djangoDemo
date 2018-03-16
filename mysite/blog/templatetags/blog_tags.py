from django import template
from django.db.models import Count
from ..models import Post

from django.utils.safestring import mark_safe
import markdown

register = template.Library()


# need to restart the development server
# in order to use the new template tags and filters


@register.simple_tag
def total_posts():
    return Post.published.count()


@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}


# assignment_tag was deprecated in django 1.9 and removed in django 2.0


@register.inclusion_tag('blog/post/most_commented_posts.html')
def get_most_commented_posts(count=5):
    most_commented_posts = Post.published.annotate(
        total_comments=Count('comments')
    ).order_by('-total_comments')[:count]
    return {'most_commented_posts': most_commented_posts}


@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))
