from django.urls import path
from django.contrib.sitemaps.views import sitemap
from . import views
from blog.models import Blog
from django.contrib.sitemaps import GenericSitemap
from blog.sitemaps import StaticViewSitemap
sitemaps = {
    'blog': GenericSitemap({
        'queryset': Blog.objects.all(),
        'date_field': 'publishdate',
    },changefreq='always', priority=0.9),
    'static': StaticViewSitemap
}
urlpatterns = [
    path('',views.home,name='home'),
    path('articles',views.articles,name='articles'),
    path('team',views.team,name='team'),
    path('contact',views.contact,name='contact'),
    path('blog/<id>/',views.blog,name='blog-full'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
]
