
from django.contrib import admin
import django.apps
from rest_framework.authtoken.models import TokenProxy
from adhoc_mobile.resources import ProductDetailsAdminResource

from nested_admin import NestedStackedInline, NestedModelAdmin
from advanced_filters.admin import AdminAdvancedFiltersMixin 

from django_summernote.admin import SummernoteModelAdmin
from django.contrib.auth.models import User

from advanced_filters.admin import AdminAdvancedFiltersMixin 
from .models import  Answer, Audit, Client ,Country , City , Area, Employee, Field, Image,Form ,Plan, Product, Project , Region, Route, Rule, Visit

from .forms import  ClientForm ,CountryForm , CityForm , AreaForm, EmployeeForm, ImageForm, PlanForm, ProductForm, ProjectForm , RegionForm, RouteForm, RuleForm, VisitForm

from import_export.admin import ImportExportModelAdmin

# Register your models here.

class CountryAdmin(AdminAdvancedFiltersMixin,admin.ModelAdmin):
    form = CountryForm
    list_display = ('name',)
    advanced_filter_fields = ('name',)
    list_per_page = 10
class CityAdmin(AdminAdvancedFiltersMixin,admin.ModelAdmin):
    form = CityForm
    list_display = ('name',)
    advanced_filter_fields = ('name',)
    list_per_page = 10
    
class AreaAdmin(AdminAdvancedFiltersMixin,admin.ModelAdmin):
    form = AreaForm
    list_display = ('name',)
    advanced_filter_fields = ('name',)
    list_per_page = 10
    
class RegionAdmin(AdminAdvancedFiltersMixin,admin.ModelAdmin):
    form = RegionForm
    list_display = ('name',)
    advanced_filter_fields = ('name',)
    list_per_page = 10
    

class ClientAdminModel(AdminAdvancedFiltersMixin,admin.ModelAdmin):
    form = ClientForm
    list_display = [field.name for field in Client._meta.fields]
    advanced_filter_fields = [field.name for field in Client._meta.fields]
    list_per_page = 25
class AdvancedFilterAdmin(admin.ModelAdmin):
    pass

class EmployeeAdmin(AdminAdvancedFiltersMixin,admin.ModelAdmin):
    form = EmployeeForm
    list_display = [field.name for field in Employee._meta.fields]
    advanced_filter_fields   = [field.name for field in Employee._meta.fields]

class ImageAdmin(AdminAdvancedFiltersMixin,admin.ModelAdmin):
    form = ImageForm
    list_display = ['name', 'photo']
    advanced_filter_fields = ['name', 'photo']
    list_per_page = 10

class planInline(NestedStackedInline):
    model = Plan
    extra = 1

class PlanAdmin(AdminAdvancedFiltersMixin,admin.ModelAdmin):
    form = PlanForm
    list_display =[field.name for field in Plan._meta.fields]
    advanced_filter_fields = [field.name for field in Plan._meta.fields]
    list_per_page = 25
class ProductAdminModel(SummernoteModelAdmin,AdminAdvancedFiltersMixin,ImportExportModelAdmin):
    form = ProductForm
    resource_class =ProductDetailsAdminResource
    list_display = ('name','category_name','sku','barcode','retailSelling_price','brand','tax','measure_unit','auditable','active','frozen_preSale','frozen_sale','image')
    advanced_filter_fields   = ('name','category_name','sku','barcode','retailSelling_price','brand','tax','measure_unit','auditable','active','frozen_preSale','frozen_sale','image')
    summernote_fields = ('description',)
   
    list_per_page = 25

class ProductAdminInline(NestedStackedInline):
    model = Product
    form = ProductForm

    extra = 1

class ProjectAdminForm(AdminAdvancedFiltersMixin,NestedModelAdmin):
    form = ProjectForm
    extra = 1
   
    list_display = [field.name for field in Project._meta.fields]
    list_editable = ['name']
    list_per_page = 10
    advanced_filter_fields =  (
        'name')


class VisitAdmin(AdminAdvancedFiltersMixin,admin.ModelAdmin):
    form = VisitForm
    list_display =[field.name for field in Visit._meta.fields]
    advanced_filter_fields = [field.name for field in Visit._meta.fields]
    list_per_page = 25
class routeInline(NestedStackedInline):
    model = Route
    extra = 1

class RouteAdmin(AdminAdvancedFiltersMixin,admin.ModelAdmin):
    list_display =[field.name for field in Route._meta.fields]
    advanced_filter_fields = [field.name for field in Route._meta.fields]
    list_per_page = 25
    form = RouteForm
class ruleInline(NestedStackedInline):
    model = Rule
    extra = 1

class RuleAdmin(AdminAdvancedFiltersMixin,admin.ModelAdmin):
    form = RuleForm
    list_display =[field.name for field in Rule._meta.fields]
    list_per_page = 25
class EmployeeAdminInline(admin.StackedInline):
    model = Employee
    form = EmployeeForm
    extra = 1

class UserAdminModelAdmin(admin.ModelAdmin):
    list_per_page = 25
    inlines = [EmployeeAdminInline]  
class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 1
class FieldsInline(admin.ModelAdmin):
    model = Field
    extra = 1
    inlines = [AnswerInline]




class FormBuilderAdmin(AdminAdvancedFiltersMixin,admin.ModelAdmin):
    list_display =  [field.name for field in Form._meta.fields]
    advanced_filter_fields = [field.name for field in Form._meta.fields]
    list_per_page = 25

# admin.site.register(Field)

admin.site.register(Form,FormBuilderAdmin)
admin.site.register(Field,FieldsInline)
admin.site.unregister(User)  
admin.site.register(User,UserAdminModelAdmin)
admin.site.register(Rule, RuleAdmin)
admin.site.register(Route, RouteAdmin)
admin.site.register(Visit, VisitAdmin)

admin.site.register(Project, ProjectAdminForm)
admin.site.register(Product,ProductAdminModel)

admin.site.register(Plan, PlanAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Audit)

admin.site.register(Client,ClientAdminModel)
admin.site.register(Country,CountryAdmin)
admin.site.register(City,CityAdmin)
admin.site.register(Area,AreaAdmin)
admin.site.register(Region,RegionAdmin)




admin.site.unregister(TokenProxy)
admin.site.register(django.contrib.admin.models.LogEntry)
admin.site.register(django.contrib.auth.models.Permission)
