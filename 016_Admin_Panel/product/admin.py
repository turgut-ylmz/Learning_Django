from django.contrib import admin
from django.utils.safestring import mark_safe
# Register your models here.
from .models import Category, Product,Review
from django.utils import timezone 
from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter, DropdownFilter
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter
from .resources import ReviewResource
from import_export.admin import ImportExportModelAdmin



class ReviewInline(admin.TabularInline):  # StackedInline farklı bir görünüm aynı iş
    '''Tabular Inline View for '''
    model = Review
    extra = 3
    classes = ('collapse',)
    #min_num = 3
    # max_num = 20

class ProductAdmin(admin.ModelAdmin):
    # readonly_fields = ("create_date",)
    list_display = ("name", "create_date", "is_in_stock", "update_date","added_days_ago","how_many_reviews", "bring_img_to_list")
    list_editable = ( "is_in_stock", )
    list_filter = ("is_in_stock", ("create_date", DateTimeRangeFilter), ("name", DropdownFilter) )
    list_display_links = ("name",)
    search_fields = ("name","create_date")
    prepopulated_fields = {'slug' : ('name',)}
    list_per_page = 15
    date_hierarchy = "update_date"
    inlines = (ReviewInline,)
    readonly_fields = ("bring_image",)
    # fields = (('name', 'slug'), 'description', "is_in_stock")
    fieldsets = (
        ("General fields", {
            "fields": (
                ('name', 'slug'), "is_in_stock" 
            ),
        }),
        ('Optionals Settings', {
            "classes" : ("collapse", ),
            "fields" : ("description","categories", "product_img", "bring_image"),
            'description' : "You can use this section for optionals settings"
        }), 
    )
    # filter_horizontal = ("categories", )
    filter_vertical = ("categories", )
    actions = ("is_in_stock",)

    def is_in_stock(self, request, queryset):
        count = queryset.update(is_in_stock=True)
        self.message_user(request, f"{count} çeşit ürün stoğa eklendi")
        
    is_in_stock.short_description = 'İşaretlenen ürünlerin stok drumunu güncelle'
    
    def added_days_ago(self, product):
        fark = timezone.now() - product.create_date
        return fark.days
    
    def bring_img_to_list(self, obj):
        if obj.product_img:
            return mark_safe(f"<img src={obj.product_img.url} width=50 height=50></img>")
        return mark_safe("******")
    
    def bring_image(self, obj):
        if obj.product_img:
            return mark_safe(f"<img src={obj.product_img.url} width=400 height=400></img>")
        return mark_safe(f"<h3>{obj.name} has not image </h3>")

class ReviewAdmin(ImportExportModelAdmin):
    list_display = ('__str__', 'created_date', 'is_released')
    list_per_page = 50
    raw_id_fields = ('product',) 
    list_filter = (('product', RelatedDropdownFilter) , )
    resource_class = ReviewResource


admin.site.register(Product,ProductAdmin)
admin.site.register(Review,ReviewAdmin)
admin.site.register(Category)

admin.site.site_title = "Clarusway Title"
admin.site.site_header = "Clarusway Admin Portal"  
admin.site.index_title = "Welcome to Clarusway Admin Portal"