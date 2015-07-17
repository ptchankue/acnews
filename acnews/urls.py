from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'acnews.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^/$', 'news_app.views.index', name = "index"), url(r'^$', 'news_app.views.index', name = "index"),

    url(r'^test/$', 'news_app.views.test', name="test"),

    url(r'^contact/$', 'news_app.views.contact', name="contact"), url(r'^contact$', 'news_app.views.contact', name="contact"),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^statics/(?P<path>.*)$', 'django.views.static.serve', 
		{'document_root': settings.STATICFILES_DIRS[0]}),
    )

urlpatterns += staticfiles_urlpatterns()

