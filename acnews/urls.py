from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

import news_app
from news_app.views import HomeView, ContactView

admin.autodiscover()

from django.conf import settings

urlpatterns = [
    path('admin', admin.site.urls),

    path('', HomeView.as_view(), name="index"),
    path('test', news_app.views.test, name="test"),
    path('contact', ContactView.as_view(), name="contact"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

