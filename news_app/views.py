from typing import Any, Dict

from django.http import HttpResponse
from django.utils import timezone
from django.views.generic import TemplateView

# Create your views here.
from news_app.models import Article, Visitor



def test(request) -> HttpResponse:
    return HttpResponse("This is a test...<img src=/statics/images/social.png></img>")


class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs: Dict[str, Any]) -> Dict[str, Any]:
        context = super(HomeView, self).get_context_data(**kwargs)

        articles = Article.objects.all().order_by("-fetched_on")

        ip = self.request.META.get("REMOTE_ADDR")
        visitor = Visitor.objects.filter(ip=ip).first()
        if visitor is None:
            # New visit
            visitor = Visitor.objects.create(
                ip=self.request.META["REMOTE_ADDR"],
            )
            print(visitor.__dict__)
        else:
            # Not a new visit
            visitor.nb_visit += 1
            visitor.last_visit = timezone.now()
            visitor.save()
            print(visitor.__dict__)

        context["author"] = "Dr Patrick Tchankue"
        context["articles"] = articles

        return context


class ContactView(TemplateView):
    template_name = "contact.html"


class CategoryView(TemplateView):
    template_name = "contact.html"
