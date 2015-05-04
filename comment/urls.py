from django.conf.urls import patterns, url


urlpatterns = patterns(
    'comment.views',
    url(r'^comment/create/(?P<pk>\d+)/$', 'create_comment', name="create_comment"),
)
