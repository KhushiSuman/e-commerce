from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings
from django.db import models


urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include('store.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


class Category(models.Model):
	name = models.CharField(max_length=50)

	@staticmethod
	def get_all_categories():
		return Category.objects.all()

	def __str__(self):
		return self.name
