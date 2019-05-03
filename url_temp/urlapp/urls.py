from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url
from urlapp import views

app_name='url_app'

urlpatterns = [
    url(r'^relative/$',views.relative,name='relative'),
    url(r'^other/$',views.other,name='other'),
    path('admin/', admin.site.urls),
]
