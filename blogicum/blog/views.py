from django.shortcuts import render
from django.http import Http404
# Create your views here.
# Временный список постов (источник данных)


def index(request):
    # Добавляем инвертирование списка постов
    reversed_posts = sorted(posts, key=lambda x: x['id'], reverse=True)
    return render(request, 'blog/index.html', {'posts': reversed_posts})


def post_detail(request, id):
    """Страница с деталями одного поста."""
    for post in posts:
        if post['id'] == id:
            return render(request, 'blog/detail.html', {'post': post})
    raise Http404(f"Пост с id={id} не найден")

def category_posts(request, category_slug):
    """Страница с постами определённой категории."""
    return render(
        request,
        'blog/category.html',
        {'category_slug': category_slug}
    )
