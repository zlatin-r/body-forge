from django.shortcuts import render

def home_page_view(request):
    return render(request, "common/home.html")
