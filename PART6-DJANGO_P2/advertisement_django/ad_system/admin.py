from django.contrib import admin, messages
from ad_system.models import Ad, Advertiser, Click, View


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ['title', 'advertiser', 'is_approved']
    list_filter = ['is_approved', 'title']
    search_fields = ['title', 'advertiser__name']

    actions = ['approve', 'disapprove']
    view_on_site = False

    fieldsets = (
        ('General info', {
            'fields': ['title', 'advertiser', 'is_approved']
        }),
        ('Media info', {
            'fields': ['image_url', 'link']
        })
    )

    def approve(self, request, queryset):
        updated = queryset.update(is_approved=True)
        self.message_user(
            request, f'{updated} ads mark as approved', messages.SUCCESS
        )

    def disapprove(self, request, queryset):
        updated = queryset.update(is_approved=False)
        self.message_user(request, f'{updated} ads mark as disapproved', messages.ERROR)


admin.site.register(Advertiser)
admin.site.register(Click)
admin.site.register(View)
