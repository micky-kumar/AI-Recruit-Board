from django.urls import path

from django.contrib import admin
from apps.core.views import frontpage, signup

admin.autodiscover()

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", frontpage, name="frontpage"),
    path("signup/", signup, name="signup"),
    path("admin/", admin.site.urls),
]
