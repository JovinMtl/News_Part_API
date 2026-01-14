from django.db import models
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel
from wagtail.api import APIField
from wagtail.images.api.fields import ImageRenditionField

from .blocks import NewsBodyBlock

class NewsPage(Page):
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    intro = models.CharField(max_length=250)

    body = StreamField(
        NewsBodyBlock(),
        blank=True,
        use_json_field=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("image"),
        FieldPanel("intro"),
        FieldPanel("body"),
    ]

    api_fields = [
        APIField("intro"),
        APIField("body"),
        APIField(
            "image_thumbnail",
            serializer=ImageRenditionField(
                "width-400|format-avif",
                source="image"
            ),
        ),
    ]
