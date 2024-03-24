from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, redirect
from products.models import NewsCategoryModel

from django.contrib.auth import logout

from .models import NewsModel
from django.shortcuts import get_object_or_404


def home_page(request):
    categories = NewsCategoryModel.objects.all()
    products = NewsModel.objects.all()
    context = {"categories": categories, "products": products}
    return render(request, template_name="index.html", context=context)


class MyLoginView(LoginView):
    template_name = "login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        return "/"


def logout_view(request):
    logout(request)
    return redirect("home")


def news_list(request):
    news = NewsModel.objects.all()
    return render(request, 'shop / index.html', {'products': news})


def index(request):
    news1 = NewsModel.objects.all()
    return render(request, "index.html", {"news1": news1})


def create(request):
    if request.method == "POST":
        news_create = NewsModel()
        news_create.news_title = request.POST.get("news_title")
        news_create.news_descriptions = request.POST.get("news_descriptions")
        news_create.news_image = request.POST.get("news_image")
        news_create.news_created_at = request.POST.get("news_created_at")
        news_create.save()
    return HttpResponseRedirect("/")


def edit(request, pk):
    try:
        news_edit = NewsModel.objects.get(pk=pk)

        if request.method == "POST":
            news_edit.news_title = request.POST.get("news_title")
            news_edit.news_descriptions = request.POST.get("news_descriptions")
            news_edit.news_image = request.POST.get("news_image")
            news_edit.news_created_at = request.POST.get("news_created_at")
            news_edit.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {"news_edit": news_edit})
    except NewsModel.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


def delete(request, pk):
    try:
        news_delete = NewsModel.objects.get(pk=pk)
        news_delete.delete()
        return HttpResponseRedirect("/")
    except NewsModel.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


def edit_news(request, news_id):
    news_article = get_object_or_404(NewsModel, pk=news_id)
