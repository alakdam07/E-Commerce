
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
##TemplateView for react file
from django.views.generic import TemplateView

urlpatterns = [
     path('admin/', admin.site.urls),
     path('api/', include('api.urls')),
     path('', TemplateView.as_view(template_name='index.html')),
]
