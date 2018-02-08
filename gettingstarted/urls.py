from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
admin.autodiscover()

import rockworthy.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', rockworthy.views.index, name='index'),
    url(r'^db', rockworthy.views.db, name='db'),
    url(r'^api', rockworthy.views.test, name='test'),
    path('admin/', admin.site.urls),
]
