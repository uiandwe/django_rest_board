from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http.response import HttpResponse
from django.core.context_processors import csrf
from user_manager.forms import LoginForm, JoinForm
from django.contrib import auth
from django.shortcuts import redirect
from django.contrib.auth.models import User
# Create your views here.


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


def join_page(request):

    if request.method == "POST":
        form_data = JoinForm(request.POST)

        if form_data.is_valid():
            username = form_data.cleaned_data['id']
            password = form_data.cleaned_data['password']
            User.objects.create_user(username=username, password=password)

            return redirect('/user/login/')
    else:
        form_data = JoinForm()
    template = get_template('join_page.html')

    context = Context({'join_page': form_data})
    context.update(csrf(request))
    return HttpResponse(template.render(context))