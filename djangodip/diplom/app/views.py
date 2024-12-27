from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator



def platform(request):
    return render(request, 'top.html')

def menu(request):
    context = {
        'hotter': 'Горячие блюда',
        'salads': 'Салаты'
    }
    return render(request, 'menu.html', context)

def menuHotter(request):
    hot = MenuHotter.objects.all().order_by('-title')
    paginator = Paginator(hot, 2)
    page_number = request.GET.get('page')
    hotter = paginator.get_page(page_number)

    return render(request, 'hotter.html', {'hotter': hotter})

def menuSalads(request):
    salad = MenuSalads.objects.all().order_by('-title')
    paginator = Paginator(salad, 2)
    page_number = request.GET.get('page')
    salads = paginator.get_page(page_number)

    return render(request, 'salads.html', {'salads': salads})

def contacts(request):
    return render(request, 'contacts.html')

def News_create(request):
    post = News.objects.all().order_by('-date')
    paginator = Paginator(post, 3)
    page_number = request.GET.get('page')
    news_obj = paginator.get_page(page_number)
    return render(request, 'news.html', {'news': news_obj})





