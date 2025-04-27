from django.contrib import admin
from django.urls import path
from hello.views import hello_world_json, hello_world_html

urlpatterns = [
    path('admin/', admin.site.urls),
    path('json/', hello_world_json),
    path('html/', hello_world_html),  # Optional Challenge route
]

