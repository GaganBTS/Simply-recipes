from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .data import recipes


class StaticViewsSitemap(Sitemap):
    changefreq='always'
    def items(self):
        return ['about','contact','home','all_recipes','privacy','terms','products']
    def location(self, item):
        return reverse(item)
    

