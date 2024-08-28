from typing import Any, Dict

from django.http import HttpResponse
from django.utils import timezone
from django.views.generic import TemplateView

# Create your views here.
# from extractor import Extractor
from news_app.models import Article, Visitor

# from django.contrib.gis.geoip import GeoIP


# unescaped = html_parser.unescape(my_string)

# bot = Extractor()
# bot.parseRadiOkapi()


def test(request) -> HttpResponse:
    return HttpResponse("This is a test...<img src=/statics/images/social.png></img>")


class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs: Dict[str, Any]) -> Dict[Any, Any]:
        context = super(HomeView, self).get_context_data(**kwargs)

        articles = Article.objects.all().order_by("-fetched_on")

        ip = self.request.META.get("REMOTE_ADDR")
        visitor = Visitor.objects.filter(ip=ip)
        if visitor.count() == 0:
            # New visit
            visitor = Visitor()
            visitor.ip = self.request.META["REMOTE_ADDR"]
            visitor.save()
            print(visitor.__dict__)
        else:
            # Not a new visit
            visitor = visitor.first()
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
