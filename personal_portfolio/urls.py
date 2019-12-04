"""personal_portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include,re_path
from django.conf.urls import url
from accounts import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home,name="home"),
    path('admin/', admin.site.urls),
    path('signup/',views.signup,name="signup"),
    path('login/',views.login_view,name="login"),
    path('logout/',views.logout,name="logout_page"),
    path("projects/", include("projects.urls")),
    path("blog/", include("blog.urls")),
    path("visitor_app/", include("visitor_app.urls")),
    re_path(r'^password_reset/$', auth_views.PasswordResetView.as_view(),
        {'template_name': "registration/password_reset_form.html"},
        name='password_reset'),
    re_path(r'^password_reset/done/$', auth_views.PasswordResetDoneView.as_view(),
        {'template_name': "registration/password_reset_done.html"},
        name='password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(),
        {'template_name': "registration/password_reset_confirm.html"},
        name='password_reset_confirm'),
    re_path(r'^reset/done/$', auth_views.PasswordResetCompleteView.as_view(),
        {'template_name': "registration/password_reset_complete.html"},
        name='password_reset_complete'),
]
