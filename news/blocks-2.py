


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
        """
        Custom API serialization for ResponsiveImageBlock
        """
        data = {
            "image": {
                "id": value["image"].id,
                "title": value["image"].title,
            }
        }

        for field in self.api_fields:
            data[field.name] = field.serializer.to_representation(
                value["image"]
            )

        return data


    # class Meta:
    #     icon = "image"
    #     label = "Responsive image"
