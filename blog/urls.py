from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
url(r'^home/', views.post_list, name='post_list'),
url(r'^login/$', auth_views.login),
url(r'^$', views.home, name='home'),
url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
url(r'^post/new/$', views.post_new, name='post_new'),
url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
url(r'^faqs/', views.faqs, name='faqs'),
    url(r'^logout/$', auth_views.logout),
    url(r'^topics/', views.topics, name='topics'),
    url(r'^education/', views.education, name='education'),
    url(r'^lifestyle/', views.lifestyle, name='lifestyle'),
    url(r'^health/', views.health, name='health'),
    url(r'^tech/', views.tech, name='tech'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
] +  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
