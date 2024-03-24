from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static
from django.conf import settings

from products.views import home_page, MyLoginView, logout_view, news_list, delete, edit

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home_page, name="home"),
    path("login/", MyLoginView.as_view()),
    path("logout/", logout_view),
    path('products/', news_list, name='news_list'),
    path('edit/<int:news_id>/', edit, name='edit'),
    path("delete/<int:pk>/", delete),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
