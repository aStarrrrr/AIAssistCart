from django.db import models

# District

class tbl_district(models.Model):
    district_name=models.CharField(max_length=50)

# Admin

class tbl_admin(models.Model):
    admin_name=models.CharField(max_length=50)
    admin_contact=models.CharField(max_length=50)
    admin_email=models.CharField(max_length=50)
    admin_password=models.CharField(max_length=50)
    
#Category

class tbl_category(models.Model):
    category_name=models.CharField(max_length=50)

#Brand
    
class tbl_brandname(models.Model):
    brand_name=models.CharField(max_length=50)

#Offer
    
class tbl_offer(models.Model):
    offer_name=models.CharField(max_length=50)
    offer_fromdate=models.CharField(max_length=50)
    offer_todate=models.CharField(max_length=50)
    offer_discription=models.CharField(max_length=50)

#Place

class tbl_place(models.Model):
    place_name=models.CharField(max_length=50)
    district = models.ForeignKey(tbl_district, on_delete=models.CASCADE)

#Subcategory
    
class tbl_subcategory(models.Model):
    subcategory_name=models.CharField(max_length=50)
    category = models.ForeignKey(tbl_category, on_delete=models.CASCADE)

#Department

class tbl_department(models.Model):
    department_name=models.CharField(max_length=50)

#Designation

class tbl_designation(models.Model):
    designation_name=models.CharField(max_length=50)

#Employee
    
class tbl_employee(models.Model):
    employee_name=models.CharField(max_length=50)
    employee_contact=models.CharField(max_length=50)
    employee_salary=models.CharField(max_length=50)
    department = models.ForeignKey(tbl_department, on_delete=models.CASCADE)
    designation = models.ForeignKey(tbl_designation, on_delete=models.CASCADE)