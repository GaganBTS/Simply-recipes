from django.urls import path


from .views import *
urlpatterns = [
    path('',homepage,name='home'),
    path('recipes',all_recipes,name='all_recipes'),
    path('about',about,name='about'),
    path('contact',contact,name='contact'),
    path('privacy-policy',privacy,name='privacy'),
    path('terms-and-conditions',terms,name='terms'),
    path('products',products,name='products'),
    path('recipes/<slug:slug>',single_recipe,name='single_recipe'),
    path('sitemap',sitemap,name='sitemap'),
]
