from django.shortcuts import render

# Create your views here.
def home_page_view(request):
    context = {
        "name": "Ivan",
    }
    return render(request, 'common/home-page.html', context)