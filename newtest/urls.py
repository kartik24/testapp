from django.conf.urls import url, include
from django.templatetags.static import static
from newtest import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',views.New, name='product'),
    url(r'^product/$',views.New, name='product'),
    url(r'^contact/$',views.Contact, name ='contact'),
    url(r'^register/$',views.Register_form, name ='register'),
    url(r'^thanks/$',views.Thanks, name ='thanks'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)