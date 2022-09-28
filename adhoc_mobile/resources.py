from threading import local
from adhoc_mobile.models import Audit, Product, Project, Visit
from adhoc_mobile.widgets import CustomBooleanWidget
from import_export import resources, fields, widgets
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget, DateWidget


            # "image",
class ProductDetailsAdminResource(resources.ModelResource):
    id =fields.Field(column_name='Repzo Id',attribute="id")

    project = fields.Field(
        column_name="Company Name",attribute="project",widget=ForeignKeyWidget(Project, 'name'))
    audit = fields.Field(
        column_name="Audit ID",attribute="audit",widget=ForeignKeyWidget(Audit, 'id'))

    name =fields.Field(column_name='Name',attribute="name")
    local_name =fields.Field(column_name='Local Name',attribute="local_name")
    sku =fields.Field(column_name='SKU',attribute="sku")
    barcode =fields.Field(column_name='Barcode',attribute="barcode")
    description =fields.Field(column_name='Description',attribute="description")
    category = fields.Field(column_name="Category", attribute="category_name")

    retailSelling_price =fields.Field(column_name='Retail Selling Price',attribute="retailSelling_price")
    brand =fields.Field(column_name='Brand',attribute="brand")
    tax =fields.Field(column_name='Tax	Measure Unit',attribute="tax")
    measure_unit =fields.Field(column_name='Measure Unit Family',attribute="measure_unit")
    auditable = fields.Field(
        column_name="Auditable",
        attribute="auditable",
        widget=CustomBooleanWidget(active=Product.auditable),
    )

    active = fields.Field(
        column_name="Active",
        attribute="active",
        widget=CustomBooleanWidget(active=Product.active),
    )
  
    frozen_preSale = fields.Field(
        column_name="Frozen Pre Sales",
        attribute="frozen_preSale",
        widget=CustomBooleanWidget(active=Product.frozen_preSale),
    )
    frozen_sale = fields.Field(
        column_name="Frozen Sales",
        attribute="frozen_sale",
        widget=CustomBooleanWidget(active=Product.frozen_sale),
    )

    image =fields.Field(column_name='Image',attribute="image")



    def before_import_row(self, row, **kwargs):
        
        name = row.get('Company Name')
        audit_id = row.get('Audit ID')
                
 

        if name and audit_id:      
            project = row['Company Name']
            audit = row['Audit ID']
            row['Company Name'] = Project.objects.get_or_create(name=name)
            row['Audit ID'] = Audit.objects.get_or_create(id=audit_id)

            for item in Project.objects.all():
                if item.name == name:
                    row['Company Name'] = item
                    break
            for item in Audit.objects.all():
                if item.id == audit_id:
                    row['Audit ID'] = item
                    break
        else:
            row['Company Name'] = None



        return super().before_import_row(row, **kwargs)


        




    class Meta:
        model = Product
        exclude =('project__id')
        fields=(
            'id',
            'name',
            'local_name',
            'sku', 'barcode',
            'description','category','retailSelling_price','brand','tax','measure_unit','auditable',
            'active','frozen_preSale','frozen_sale','image', 'project'

        )

