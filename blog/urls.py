from django.conf.urls import patterns, include, url

from django.contrib import admin
from blog import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blogspot.views.home', name='home'),
    
    #ex: /blog/
    url(r'^$', views.all_blogs, name="all_blogs"),
    
    #ex: /blog/post/{pk}
    url(r'^post/(?P<pk>\d+)/$', views.post, name="post"),

    #ex: /blog/add_comment/{pk}
    url(r'^add_comment/(?P<pk>\d+)/$', views.add_comment, name="add_comment"),

)
