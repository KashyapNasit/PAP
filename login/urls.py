from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views

from login import views as core_views


urlpatterns = [
    url(r'^$', auth_views.LoginView.as_view(template_name='login.html'), {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name='logout.html'), {'next_page': 'login'}, name='logout'),
     # url(r'^signup/$', core_views.signup, name='signup'),
]