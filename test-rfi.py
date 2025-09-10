#!/usr/bin/python


import os
from datetime import datetime
from typing import Any

import requests
from bs4 import BeautifulSoup

from news_app.models import Article

os.environ["DJANGO_SETTINGS_MODULE"] = "acnews.settings"


def parse(article: Any) -> None:
    print(article.find("a", {"class": "modal"}))


url = "https://rfi.fr/afrique"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

sections = soup.findAll("section", {"id": "news"})

# anchors = [td.find('a') for td in soup.findAll('li', {'data-bo-type':'article'})]
articles = soup.findAll("li", {"data-bo-type": "article"})
print("Number of article:", len(articles))
for article in articles:
    if article:
        a = article.find("a")
        if a.get("title"):
            post = Article()
            print(a.get("title").encode("utf-8"))
            post.title = a.get("title").encode("utf-8")

            print("Link:", a["href"])
            post.link = "http://rfi.fr" + a["href"]

            print(a.get("data-height"))
            if a.get("data-image"):
                print("Image:", a.get("data-image"))
                post.thumbnail = a.get("data-image")

            posts = Article.objects.filter(link=post.link)
            if posts.count() == 0:
                post.source = "RFI Afrique"
                post.view_count = 0
                post.fetched_on = datetime.now()
                print(post.__dict__)
                post.save()

            print("---" * 20)

            print("\n\nFrom my database:")
posts = Article.objects.all()
for post in posts:
    print(post.link.encode("utf-8"), post.title.encode("utf-8"))
print("\n\nArticle #", posts.count())
