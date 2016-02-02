from django.contrib import admin
from .models import Post, Categories
# Register your models here.

class CategoriesAdmin(admin.ModelAdmin):
	list_display = ('category', )

admin.site.register(Categories, CategoriesAdmin)

class PostModelAdmin(admin.ModelAdmin):
	list_display = ["title", "author", "updated", "timestamp", ]
	list_display_links = ["title", "updated",]
	#list_editable = ["title"]
	list_filter = ["updated", "timestamp",]

	search_fields = ["title", "content",]
	class Meta:
		model = Post


admin.site.register(Post, PostModelAdmin)