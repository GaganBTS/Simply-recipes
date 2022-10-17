from django.shortcuts import render
from .data import recipes
# Create your views here.
def homepage(request):
    all_recipes = recipes()
    return render(request,'home.html',{'all_recipes':all_recipes})

def all_recipes(request):
    all_recipes = recipes()
    return render(request,'recipes.html',{'all_recipes':all_recipes})

def single_recipe(request,slug):
    all_recipes = recipes()
    recipe = []
    for i in all_recipes:
        if slug==i['slug']:
            recipe.append(i)
    return render(request,'single_recipe.html',{'recipe':recipe})

def about(request):
    all_recipes = recipes()
    featured_recipes = all_recipes[:3]
    return render(request,'about.html',{'recipes':featured_recipes})    
def contact(request):
    all_recipes = recipes()
    featured_recipes = all_recipes[:3]
    return render(request,'contact.html',{'recipes':featured_recipes})    

def privacy(request):
    return render(request,'privacy.html')
def terms(request):
    return render(request,'terms.html')

def page_not_found_view(request,exception):
    return render(request,'404.html',status=404)