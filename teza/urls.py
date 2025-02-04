from django.contrib import admin
from django.urls import path
from teza_app.views import index, generate_content

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path("generate/", generate_content, name="generate"),

]
