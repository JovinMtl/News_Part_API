from django.contrib.auth.models import User
from django.utils import timezone

from django.db import models
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel
from wagtail.api import APIField
from wagtail.images.api.fields import ImageRenditionField

from taggit.models import TagBase, TaggedItemBase
from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from wagtail.snippets.models import register_snippet

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

@register_snippet
class CategorieArticle(models.Model):
    nom = models.CharField(max_length=25, default="Témoignages")

    panels = [
        FieldPanel("nom"),
    ]

    def __str__(self):
        return self.nom


class Mention(TagBase):
    class Meta:
        verbose_name = "Mention"
        verbose_name_plural = "Mentions"

class PageMention(TaggedItemBase):
    tag = models.ForeignKey(
        Mention,
        related_name="tagged_pages",
        on_delete=models.CASCADE
    )
    content_object = ParentalKey(
        "news.Articles",
        on_delete=models.CASCADE,
        related_name="tagged_items"
    )

class Articles(Page):
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    auteur = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    categorie = models.ForeignKey(CategorieArticle, on_delete=models.SET_NULL, null=True, blank=True)
    intro = models.CharField(max_length=250)

    contenu = StreamField(
        NewsBodyBlock(),
        blank=True,
        use_json_field=True,
    )
    date_d_edition = models.DateTimeField(default=timezone.now)
    temps_de_lecture = models.IntegerField(verbose_name='Temps ecute (en Minute)', default=5)
    tags = ClusterTaggableManager(
        through=PageMention,
        blank=True,
        verbose_name="Tags / Mentions"
    )
    score = models.IntegerField(default=0)

    content_panels = Page.content_panels + [
        FieldPanel("image"),
        FieldPanel("intro"),
        FieldPanel("contenu"),
        FieldPanel("auteur"),
        FieldPanel("categorie"),
        FieldPanel("date_d_edition"),
        FieldPanel("temps_de_lecture"),
        FieldPanel("tags"),
        FieldPanel("score"),
    ]

    api_fields = [
        APIField("intro"),
        APIField("contenu"),
        APIField(
            "image_thumbnail",
            serializer=ImageRenditionField(
                "width-800|format-avif",
                source="image"
            ),
        ),
        APIField("tags"),
    ]

    def get_admin_display_title(self):
        return f"{str(self.date_d_edition)[:10]} · {self.title}"
