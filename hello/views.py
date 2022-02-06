from django.shortcuts import render
from hello.apidata import NewsNasaApi, ImageDayApi


def index(request):
  return render(request, 'index.html')
  
  
def home(request):
  return render(request, 'home.html')


def news(request):
  context = {'ListNews': NewsNasaApi() }
  return render(request, 'news.html', context)


def imageday(request):
  context = ImageDayApi() 
  return render(request, 'imageday.html', context)
  

def track(request):
  return render(request, 'track.html')