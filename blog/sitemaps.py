from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import Blog
class StaticViewSitemap(Sitemap):   
    changefreq = "daily"
    priority = 0.9
    date = 22-8-2020

    def items(self):
        return ['home','articles','team','contact']

    def location(self, item):
        return reverse(item)
