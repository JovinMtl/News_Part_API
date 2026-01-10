from django.db import models

from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.api import APIField
from wagtail.images.api.fields import ImageRenditionField
from wagtail.admin.panels import FieldPanel
from wagtail import blocks
# from wagtail.admin.edit

from .blocks import ResponsiveImageBlock

# Create your models here.

class NewsPage(Page):
    image = models.ForeignKey(
        'wagtailimages.Image', 
        null=True, 
        blank=True,
        on_delete=models.SET_NULL
        )
    intro = models.CharField(max_length=250)
    # body  = RichTextField(blank=True)
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title", icon="title")),
        ("paragraph", blocks.RichTextBlock(icon="pilcrow")),
        ("image", ResponsiveImageBlock(icon="image"))
        ], blank=True, use_json_field=True)

    content_panels = Page.content_panels  + [
        FieldPanel("intro"),
        FieldPanel("body"),
        FieldPanel("image")
    ]

    api_fields = [
        APIField('intro'),
        APIField('body'),
        APIField('image_thumbnail', serializer=ImageRenditionField('width-400|format-avif', source='image')),
    ]
