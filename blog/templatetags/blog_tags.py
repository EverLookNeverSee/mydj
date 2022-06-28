from django import template
from blog.models import Post

register = template.Library()


@register.simple_tag(name="n_published_posts")
def get_number_of_published_posts():
    return Post.objects.filter(status=1).count()


@register.simple_tag(name="published_posts")
def get_published_posts():
    return Post.objects.filter(status=1)


@register.filter
def snippet(value, word_count):
    return value[:word_count] + "..."


@register.inclusion_tag("blog/blog-latest-posts.html")
def latest_posts(count=3):
    posts = Post.objects.filter(status=1).order_by("-published_date")[:count]
    return {"posts": posts}
