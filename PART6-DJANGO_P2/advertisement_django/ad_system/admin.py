from django.contrib import admin, messages
from ad_system.models import Ad, Advertiser, Click, View


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ['ad_title', 'advertiser_id', 'is_approved']
    list_filter = ['is_approved', 'ad_title']
    search_fields = ['ad_title', 'advertiser_id__advertiser_name']

    actions = ['approve', 'disapprove']
    view_on_site = True
    fieldsets = (
        ('General info', {
            'fields': ['ad_title', 'advertiser_id', 'is_approved']
        }),
        ('Media info', {
            'fields': ['ad_image_url', 'ad_link']
        })
    )

    def approve(self, request, queryset):
        updated = queryset.update(approved=True)
        self.message_user(
            request, f'{updated} ads mark as approved', messages.SUCCESS
        )

    def disapprove(self, request, queryset):
        updated = queryset.update(approved=False)
        self.message_user(request, f'{updated} ads mark as disapproved', messages.ERROR)


admin.site.register(Advertiser)
admin.site.register(Click)
admin.site.register(View)
