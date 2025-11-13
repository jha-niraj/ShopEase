from django.contrib import admin
from django.utils import timezone
from .models import Product, Order, Contact

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['Product_Name', 'seller', 'Price', 'Cateogary', 'is_approved', 'created_at', 'approved_date']
    list_filter = ['is_approved', 'Cateogary', 'created_at']
    search_fields = ['Product_Name', 'Description', 'seller__username']
    readonly_fields = ['created_at', 'updated_at']
    list_editable = ['is_approved']
    
    fieldsets = (
        ('Product Information', {
            'fields': ('Product_Name', 'Cateogary', 'Price', 'Description', 'image', 'linkToDownload')
        }),
        ('Seller Information', {
            'fields': ('seller',)
        }),
        ('Approval Status', {
            'fields': ('is_approved', 'approved_date', 'pub_date')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    actions = ['approve_products', 'unapprove_products']
    
    def approve_products(self, request, queryset):
        """Bulk action to approve selected products"""
        updated = queryset.update(is_approved=True, approved_date=timezone.now())
        self.message_user(request, f'{updated} product(s) approved successfully.')
    approve_products.short_description = "✓ Approve selected products"
    
    def unapprove_products(self, request, queryset):
        """Bulk action to unapprove selected products"""
        updated = queryset.update(is_approved=False, approved_date=None)
        self.message_user(request, f'{updated} product(s) unapproved.')
    unapprove_products.short_description = "✗ Unapprove selected products"
    
    def save_model(self, request, obj, form, change):
        """Auto-set approval date when product is approved"""
        if obj.is_approved and not obj.approved_date:
            obj.approved_date = timezone.now()
        elif not obj.is_approved:
            obj.approved_date = None
        
        # If admin is adding product, mark as approved and set seller to None
        if not change and not obj.seller:
            obj.is_approved = True
            obj.approved_date = timezone.now()
        
        super().save_model(request, obj, form, change)

admin.site.register(Order)
admin.site.register(Contact)

admin.site.site_header = 'ShopEase Artisan Marketplace Administration'
admin.site.site_title = 'ShopEase Admin'
admin.site.index_title = 'Welcome to ShopEase Administration'