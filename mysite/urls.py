from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import view
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',view.start),
    url(r'^about/$',view.start_about),
    url(r'^blog/category/(?P<ca>.*)/$',view.start),
    url(r'^blog/(?P<t>.*)/$',view.start),
    url(r'^pic/$',view.my_image),
    url(r'^test/$',view.test),
)
