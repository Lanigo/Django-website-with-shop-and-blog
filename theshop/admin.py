from django.contrib import admin
from .models import AcrylicPainting, OilPainting, PencilSketch, PastelDrawing

admin.site.register(AcrylicPainting)
admin.site.register(OilPainting)
admin.site.register(PencilSketch)
admin.site.register(PastelDrawing)