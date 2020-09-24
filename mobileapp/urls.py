from django.urls import path
from . views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('list/', Product.as_view(), name='list'),
    path('upload/', UploadPage.as_view(), name='upload'),
    path('delete/', ProductDel.as_view(), name='delete'),
    path('write_date/', Write_date, name='write_date'),
    path('prediction/', prediction, name='prediction'),
    path('write_date/logic/', logic, name='logic'),
    path('test/', uploader, name='test')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)