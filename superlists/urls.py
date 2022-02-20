from django.urls import include, re_path
from lists import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    re_path(r'^$', views.home_page, name="home"),
]
