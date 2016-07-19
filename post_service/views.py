from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http.response import HttpResponse
from django.core.paginator import Page, PageNotAnInteger, Paginator, EmptyPage

from post_service.models import Post


def post_list(request):
    template = get_template('post_list.html')

    page_data = Paginator(Post.objects.all(), 5)
    page = request.GET.get('page')
    try:
        posts = page_data.page(page)
    except PageNotAnInteger:
        posts = page_data.page(1)
    except EmptyPage:
        posts = page_data.page(page_data.num_pages)

    context = Context({'post_list': posts, 'current_page': int(page), 'total_page': range(1, page_data.num_pages+1)})

    return HttpResponse(template.render(context))