from django.conf.urls import patterns, url
from post.views import PostIndexView, PostView


urlpatterns = patterns('',
	url(r'^$', PostIndexView.as_view()),
	url(r'^(?P<slug>[-\w]+)/$', PostView.as_view(), name='post_detail'),
	url(r'^tag/(?P<tag>[-\w]+)/$', 'post.views.tagpage', name='tag_detail'),

	
	
)