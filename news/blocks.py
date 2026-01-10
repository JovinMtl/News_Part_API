from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.api.fields import ImageRenditionField
from wagtail.api import APIField


class ResponsiveImageBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=True)

    api_fields = [
        APIField(
            "small",
            # serializer=ImageRenditionField("fill-400x300", source="image"),
            serializer=ImageRenditionField("width-350", source="image"),
        ),
        APIField(
            "medium",
            serializer=ImageRenditionField("width-780", source="image"),
        ),
        APIField(
            "large",
            serializer=ImageRenditionField("width-1600", source="image"),
        ),
    ]

    def get_api_representation(self, value, context=None):
        image = value["image"]

        return {
            "image": {
                "id": image.id,
                "title": image.title,
            },
            "small": ImageRenditionField(
                "width-400|format-avif",
                source="image"
            ).to_representation(image),
            "medium": ImageRenditionField(
                "width-800|format-avif",
                source="image"
            ).to_representation(image),
            "large": ImageRenditionField(
                "width-1080|format-avif",
                source="image"
            ).to_representation(image),
            "xlarge": ImageRenditionField(
                "width-1600|format-avif",
                source="image"
            ).to_representation(image),
        }


    # class Meta:
    #     icon = "image"
    #     label = "Responsive image"
