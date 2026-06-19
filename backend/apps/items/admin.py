from django.contrib import admin

from .models import (
    Category,
    Item,
    ItemPhoto,
    Favorite,
)


admin.site.register(Category)
admin.site.register(Item)
admin.site.register(ItemPhoto)
admin.site.register(Favorite)

# END OF FILE
