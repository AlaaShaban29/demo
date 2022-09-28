from django import forms

from adhoc_mobile.models import Answer, Employee, Field, Image, Plan, Product, Project,Client ,Country , City , Area , Region, Route, Rule, Visit

class CountryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CountryForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
    class Meta:
        model = Country
        fields = '__all__'
        exclude = ['created_at','updated_at']
class CityForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CityForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
    class Meta:
        model = City
        fields = '__all__'
        exclude = ['created_at','updated_at']
class AreaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AreaForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
    class Meta:
        model = Area
        fields = '__all__'
        exclude = ['created_at','updated_at']
class RegionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RegionForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
    class Meta:
        model = Region
        fields = '__all__'
        exclude = ['created_at','updated_at']
class ClientForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        self.fields['name'].help_text = 'Enter Client Name'
        self.fields['website'].help_text = 'Enter Client website'
        self.fields['email'].help_text = 'Enter Client email'
        self.fields['phone'].help_text = 'Enter Client phone'
        self.fields['zip_code'].help_text = 'Enter Client zip_code'

    class Meta:
        model = Client
        fields = ('__all__')

class EmployeeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['identifier'].widget.attrs.update({'class': 'form-control'})
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['phone'].widget.attrs.update({'class': 'form-control'})
        self.fields['job_option'].widget.attrs.update({'class': 'form-control'})
    class Meta:
        model = Employee
        fields = ('__all__')
        exclude = ['created_at','updated_at']

class ImageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ImageForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['photo'].widget.attrs.update({'class': 'form-control'})
    class Meta:
        model = Image
        fields = ('__all__')
        exclude = ['created_at','updated_at']

class PlanForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PlanForm, self).__init__(*args, **kwargs)
        self.fields['project'].widget.attrs.update({'class': 'form-control'})
        self.fields['employee'].widget.attrs.update({'class': 'form-control'})
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['force_sequence'].widget.attrs.update({'class': 'form-control'})
        self.fields['disabled'].widget.attrs.update({'class': 'form-control'})
        self.fields['project'].help_text = 'Select a project'
        self.fields['employee'].help_text = 'Select an employee'
        self.fields['name'].help_text = 'Enter a name for the plan'
        self.fields['start_date'].help_text = 'Enter a start date for the plan'
        self.fields['end_date'].help_text = 'Enter an end date for the plan'
        self.fields['force_sequence'].help_text = 'Force sequence'
        self.fields['disabled'].help_text = 'Disable the plan'

    class Meta: 
        model = Plan
        fields = '__all__'
        
class ProjectForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'required': 'required'})
        self.fields['name'].help_text = 'Enter Project Name'
    class Meta: 
        model = Project 
        fields = ('__all__')



class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['name'].help_text = 'Enter Product Name'
        self.fields['local_name'].help_text = 'Enter Product Local Name'
        self.fields['sku'].help_text = 'Enter Product SKU'
        self.fields['barcode'].help_text = 'Enter Product Barcode'
        self.fields['description'].help_text = 'Enter Product Description'
        self.fields['retailSelling_price'].help_text = 'Enter Product Retail Selling Price'
        self.fields['brand'].help_text = 'Enter Product Brand'
        self.fields['tax'].help_text = 'Enter Product Tax'
        self.fields['measure_unit'].help_text = 'Enter Product Measure Unit'
        self.fields['auditable'].help_text = 'Enter Product Auditable'
        self.fields['active'].help_text = 'Enter Product Status'
        self.fields['frozen_preSale'].help_text = 'Enter Product Frozen Pre Sale'
        self.fields['frozen_sale'].help_text = 'Enter Product Frozen Sale'
        self.fields['image'].help_text = 'Enter Product Image'

        self.fields['name'].widget.attrs.update({'class': 'form-control'})

        self.fields['local_name'].widget.attrs.update({'class': 'form-control'})

        self.fields['sku'].widget.attrs.update({'class': 'form-control'})
        self.fields['barcode'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['retailSelling_price'].widget.attrs.update({'class': 'form-control'})
        self.fields['brand'].widget.attrs.update({'class': 'form-control'})
        self.fields['tax'].widget.attrs.update({'class': 'form-control'})
        self.fields['measure_unit'].widget.attrs.update({'class': 'form-control'})
        self.fields['image'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Product
        fields = ('__all__')

class VisitForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(VisitForm, self).__init__(*args, **kwargs)
        self.fields['employee'].help_text = 'Select an employee'
        self.fields['client'].help_text = 'Select a client'
        self.fields['route'].help_text = 'Select a route'
        self.fields['start_date'].help_text = 'Enter a start date'
        self.fields['end_date'].help_text = 'Enter an end date'
        self.fields['total_duration'].help_text = 'Enter a total duration'
        self.fields['store_location'].help_text = 'Enter a store location'
        self.fields['end_location'].help_text = 'Enter an end location'
        self.fields['distance'].help_text = 'Enter a distance'
        self.fields['start_distance'].help_text = 'Enter a start distance'
        self.fields['end_distance'].help_text = 'Enter an end distance'
        self.fields['delta_distance'].help_text = 'Enter a delta distance'
        self.fields['start_in_geofence'].help_text = 'Enter a start in geofence'
        self.fields['end_in_geofence'].help_text = 'Enter an end in geofence'
        self.fields['auto_closed_by_geofence'].help_text = 'Enter an auto closed by geofence'

    class Meta:
        model = Visit
        fields = '__all__'

class RouteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RouteForm, self).__init__(*args, **kwargs)
        self.fields['project'].widget.attrs.update({'class': 'form-control'})
        self.fields['rule'].widget.attrs.update({'class': 'form-control'})
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['force_sequence'].widget.attrs.update({'class': 'form-control'})
        self.fields['disabled'].widget.attrs.update({'class': 'form-control'})
        self.fields['project'].help_text = 'Select a project'
        self.fields['rule'].help_text = 'Select a rule'
        self.fields['name'].help_text = 'Enter a name for the route'
        self.fields['force_sequence'].help_text = 'Force sequence'
        self.fields['disabled'].help_text = 'Disable the route'
    class Meta:
        model = Route
        fields = '__all__'
       
class RuleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RuleForm, self).__init__(*args, **kwargs)
        self.fields['project'].widget.attrs.update({'class': 'form-control'})
        self.fields['plan'].widget.attrs.update({'class': 'form-control'})

        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['type'].widget.attrs.update({'class': 'form-control'})
        self.fields['note'].widget.attrs.update({'class': 'form-control'})
        self.fields['name'].help_text = 'Enter a name for the rule'
        self.fields['plan'].help_text = 'Select a plan'
        self.fields['type'].help_text = 'Select a type for the rule'
        self.fields['note'].help_text = 'Enter a note for the rule'
        self.fields['project'].help_text = 'Select a project'
        self.fields['plan'].help_text = 'Select a plan'
        self.fields['start_date'].help_text = 'Enter a start date for the rule'
        self.fields['end_date'].help_text = 'Enter an end date for the rule'
        self.fields['force_sequence'].help_text = 'Force sequence'
        self.fields['disabled'].help_text = 'Disable the rule'


    class Meta: 
        model = Rule
        fields = '__all__'
        exclude = ('created_at', 'updated_at', 'created_by', 'updated_by')
        
# class FieldsForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):

#         super(FieldsForm, self).__init__(*args, **kwargs)
#         self.fields['input_type'].help_text = 'if type has multiple choose separate words with "," comma'

#     class Meta:
#         model = Field
#         fields = '__all__'








