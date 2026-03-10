from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.api.fields import ImageRenditionField
from wagtail.fields import StreamField
# from wagtail.images.blocks import ImageBlock

class ResponsiveImageBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=True)

    def get_api_representation(self, value, context=None):
        image = value["image"]

        return {
            "image": {
                "id": image.id,
                "title": image.title,
            },
            "small": ImageRenditionField(
                "fill-400x300|format-avif", source="image"
            ).to_representation(image),
            "medium": ImageRenditionField(
                "fill-800x450|format-avif", source="image"
            ).to_representation(image),
            "large": ImageRenditionField(
                "fill-1080x720|format-avif", source="image"
            ).to_representation(image),
            "xlarge": ImageRenditionField(
                "fill-1600x900|format-avif", source="image"
            ).to_representation(image),
        }

    class Meta:
        icon = "image"
        label = "Responsive image"

class ResponsiveProfileBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=True)

    def get_api_representation(self, value, context=None):
        image = value["image"]

        return {
            "image": {
                "id": image.id,
                "title": image.title,
            },
            "small": ImageRenditionField(
                "width-400|format-avif", source="image"
            ).to_representation(image),
            "medium": ImageRenditionField(
                "width-800|format-avif", source="image"
            ).to_representation(image),
        }

    class Meta:
        icon = "image"
        label = "image du profil"


class NewsBodyBlock(blocks.StreamBlock):
    sous_titre = blocks.CharBlock(classname="full title", icon="title")
    paragraphe = blocks.RichTextBlock(icon="pilcrow")
    image = ResponsiveImageBlock()
    citation = blocks.BlockQuoteBlock()

