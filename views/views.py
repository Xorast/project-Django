from django.shortcuts   import render


def get_home_page(request):
    return render(request, "views/index.html")

def get_about_page(request):
    return render(request, "views/about.html")