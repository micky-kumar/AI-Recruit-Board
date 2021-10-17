from django.urls import path

from django.contrib import admin
from apps.core.views import frontpage, signup
from django.contrib.auth import views
from apps.job.views import job_detail

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", frontpage, name="frontpage"),
    path("signup/", signup, name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path("admin/", admin.site.urls),
    path("jobs/<int:job_id>/", job_detail, name='job_detail')
]
