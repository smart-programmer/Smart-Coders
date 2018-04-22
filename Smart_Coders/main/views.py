from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.contrib.auth.views import PasswordResetForm, PasswordResetView
from django.views.generic import TemplateView, DetailView, ListView, CreateView
from main.models import Article
from main.forms import Article_form
from django.contrib.auth import get_user_model
import random


#                                                                          بسم الله الرحمن الرحيم

def Blogs_query(request):
    a = ['blue', 'aqua', 'red', 'green', 'yellow', 'purple', 'black']
    b = random.choice(a)
    template_name = "main/main.html"
    queryset = Article.objects.all().order_by('-post_time')[:15]
    context = {"object_list": queryset, 'colors': b}
    return render(request, template_name, context)


class Article_lists(ListView):
    template_name = "main/Articles_list.html"

    def get_queryset(self, *args, **kwrgs):
        slug = self.kwargs.get('slug')
        if slug:
            queryset = Article.objects.filter(Q(slug__iexact=slug) | Q(
                slug__icontains=slug)).order_by("-post_time")
        else:
            queryset = Article.objects.all().order_by("-post_time")
        return queryset


class Article_obj(DetailView):
    template_name = "main/Article.html"
    queryset = Article.objects.all()


class Article_form(LoginRequiredMixin, CreateView):
    form_class = Article_form
    login_url = "/Login/"
    template_name = "main/form.html"
    success_url = "/"

    def form_valid(self, form):
        # if self.request.user.is_authenticated:
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super().form_valid(form)
        # else:
        #     return HttpResponseRedirect("/")


class contact(TemplateView):
    template_name = 'main/portfolio.html'

 

class Profile(LoginRequiredMixin, ListView):
    template_name = "main/profile.html"
    login_url = "/Login/"
    success_url = "/profile/"

    def get_queryset(self, *args, **kwrgs):
    	user = self.request.user
    	queryset = user.article_set.all()
    	return queryset

class pass_word(PasswordResetView):
    template_name = "registration/password_reset_form.html"
    form_class = PasswordResetForm
    email_template_name = "registration/password_reset_email.html"
    subject_template_name = "registration/password_reset_subject.txt"


# @login_required(login_url="")you can also setup the login url in settings.py under ROOT_URLCONF if you don't want to rewrite it every time:ملاحظة غيرت هذا الview الى class based view لقصر الكود في ال class based view لكن كلاهما فعال
# def Blogs_form(request):
#     errors = None
#     form = Article_form(request.POST or None)
#     if form.is_valid():
#         if request.user.is_authenticated:
#             instance = form.save(commit=False)
#             instance.owner = request.user
#             instance.save()
#
#             return HttpResponseRedirect("/")
#         else:
#             return HttpResponseRedirect("/admin/")
#
#         # form.save()
#         # obj = Article.objects.create(
#         #     title=form.cleaned_data.get("title"),
#         #     body=form.cleaned_data.get("body")
#         # )
#
#         return HttpResponseRedirect("/")
#     if form.errors:
#         errors = form.errors
#     template_name = "main/Article_form.html"
#     queryset = Article.objects.all()
#     context = {"errors": errors, "query": queryset, "as_p": form}
#     return render(request, template_name, context)
