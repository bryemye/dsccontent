from django.contrib import admin

# Register your models here.
from .models import ContentPiece, Author

admin.site.register(ContentPiece)
admin.site.register(Author)
