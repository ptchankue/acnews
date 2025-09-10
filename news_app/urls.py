from django.urls import path

from news_app.views import CategoryView

urlpatterns = [
    path("blog", CategoryView.as_view(), name="blog"),
]
