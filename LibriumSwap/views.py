from django.shortcuts import render

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)

def error_view(request, exception=None):
    return render(request, "404.html", {})