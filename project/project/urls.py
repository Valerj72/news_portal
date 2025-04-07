"""
URL configuration for project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers
from news_portal import views


router = routers.DefaultRouter()
router.register(r'author', views.AuthorViewset)
router.register(r'category', views.CategoryViewset)
router.register(r'subscriber', views.SubscriberViewest)
router.register(r'post', views.PostViewset)
router.register(r'postcategory', views.PostCategoryViewset)
router.register(r'comment', views.CommentViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    path("accounts/", include("allauth.urls")),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('', include('news_portal.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
    path('i18n/', include('django.conf.urls.i18n')),
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
    ]
