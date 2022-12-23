from import_export import resources
from product.models import Review


class ReviewResource(resources.ModelResource):

    class Meta:
        model = Review # default all fields
        # fields = ("is_released", "product")