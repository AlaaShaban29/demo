
from rest_framework import serializers
from adhoc_mobile.models import Employee, Country, City, Area, Region , Client, Image, Project, Product, Audit, Plan, Rule, Route





class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model= Project
        fields= ['id', 'name', 'description', 'is_active', 'created_at', 'updated_at']




class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model= Employee
        fileds= ['id', 'username', 'identifier', 'name', 'first_name', 'last_name', 'date_joined', 'email', 'password', 'is_superuser', 'is_active',  'isDisabled', 'profilePicture', 'phone', 'forceOnlineConnectivity', 'job_option','group_id', 'created_at', 'updated_at' ]
        
        
        
        
class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model= Country
        fields= ['id' , 'name' , 'created_at', 'updated_at']
        
        
 
   
class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model= City     
        fileds=['id' , 'name' , 'created_at', 'updated_at', 'country_id']
        
   
   
        
class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model= Area     
        fileds=['id' , 'name' , 'created_at', 'updated_at', 'city_id']
        
        
        
        
        
class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model= Region     
        fileds=['id' , 'name' , 'created_at', 'updated_at', 'area_id']
        


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model=Plan
        fields= ['id', 'name', 'start_date', 'end_date','force_sequence', 'disabled'  , 'employee_id', 'project_id', 'created_at', 'updated_at']

