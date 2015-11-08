from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request, "about.html", {})

def articles(request):
    return render(request, "articles.html", {})

def photos(request):
    return render(request, "photos.html", {})

def bio(request):
    return render(request, "bio.html", {})

def videos(request):
    return render(request, "videos.html", {})