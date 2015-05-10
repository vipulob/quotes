# Created: 05/02/2015   Modified: 05/02/2015

# Author: Vipul Borikar

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^practice/', include('practice.urls')),
    url(r'^quotes/', include('quotes.urls'))
]
