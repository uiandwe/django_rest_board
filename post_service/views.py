from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http.response import HttpResponse
from django.core.paginator import Page, PageNotAnInteger, Paginator, EmptyPage
from django.core.context_processors import csrf
from post_service.forms import LoginForm
from post_service.models import Post
from django.contrib import auth
from django.shortcuts import redirect
import logging
logger = logging.getLogger(__name__)

def post_list(request):
    template = get_template('post_list.html')

    page_data = Paginator(Post.objects.all(), 5)
    page = request.GET.get('page')

    if page is None:
        page = 1

    try:
        posts = page_data.page(page)
    except PageNotAnInteger:
        posts = page_data.page(1)
    except EmptyPage:
        posts = page_data.page(page_data.num_pages)

    context = Context({'post_list': posts, 'current_page': int(page), 'total_page': range(1, page_data.num_pages+1)})

    return HttpResponse(template.render(context))


def login(request):
    template = get_template('login_form.html')

    context = Context({'login_form': LoginForm()})
    context.update(csrf(request))
    return HttpResponse(template.render(context))


def login_validate(request):
    login_form_data = LoginForm(request.POST)

    if login_form_data.is_valid():
        user = auth.authenticate(username=login_form_data.cleaned_data['id'], password=login_form_data.cleaned_data['password'])

        if user is not None:
            if user.is_active:
                auth.login(request, user)

                return redirect('/board/')
        else:
            return HttpResponse('비번')
    else:
        return HttpResponse('폼')

    return HttpResponse('오류')