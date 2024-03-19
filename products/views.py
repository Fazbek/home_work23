from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from products.models import NewsCategoryModel

from django.contrib.auth import logout

from .models import NewsModel


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
    return render(request, 'shop / index.html', {'news': news})
