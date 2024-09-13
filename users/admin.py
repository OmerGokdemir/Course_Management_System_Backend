from django.contrib import admin
from users.models import CustomUser

# admin.site.register(CustomUser)

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["id", "email", "first_name", "last_name", "is_active", "is_staff"]
    list_display_links = ["email"]
    list_filter = ["is_active"]
    list_editable = ["is_active"]
    search_fields = ["email"]