from django.shortcuts import render

# Create your views here.


def about(request):
    """Страница «О проекте»."""
    template_name = 'pages/about.html'
    return render(request, template_name)


def rules(request):
    """Страница «Правила»."""
    template_name = 'pages/rules.html'
    return render(request, template_name)
