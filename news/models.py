from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.api import APIField
from wagtail.images.api.fields import ImageRenditionField
from wagtail.admin.panels import FieldPanel
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
# from wagtail.admin.edit

# Create your models here.

class NewsPage(Page):
    intro = models.CharField(max_length=250)
    # body  = RichTextField(blank=True)
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title", icon="title")),
        ("paragraph", blocks.RichTextBlock(icon="pilcrow")),
        ("image", ImageChooserBlock(icon="image"))
    ])
    image = models.ForeignKey(
        'wagtailimages.Image', 
        null=True, 
        blank=True,
        on_delete=models.SET_NULL
        )

    content_panels = Page.content_panels  + ["intro", "body", 'image']

    api_fields = [
        APIField('intro'),
        APIField('body'),
        APIField('image_thumbnail', serializer=ImageRenditionField('fill-800x450', source='image')),
    ]
