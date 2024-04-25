from django.shortcuts import render,redirect
from Administrator.models import *
from Guest.models import *

def LoadingHomePage(request):
    if 'aid' in request.session:
        return render(request,"Administrator/HomePage.html")
    else:
        return redirect("Guest:Login")

def logout(request):
    del request.session["aid"]
    return redirect("Guest:Login")

#District

def districtInsertSelect(request):
    if 'aid' in request.session:
        dis=tbl_district.objects.all()
        if request.method=="POST":
            disName=request.POST.get('txtdistrict')
            tbl_district.objects.create(district_name=disName)
            return redirect("Administrator:districtInsertSelect")
        else:
            return render(request,"Administrator/District.html",{'data':dis})
    else:
        return redirect("Guest:Login")
    
def delDistrict(request,did):
    tbl_district.objects.get(id=did).delete()
    return redirect("Administrator:districtInsertSelect")

def districtupdate(request,eid):
    editdata=tbl_district.objects.get(id=eid)
    if request.method=="POST":
        editdata.district_name=request.POST.get("txtdistrict")
        editdata.save()
        return redirect("Administrator:districtInsertSelect")
    else:
        return render(request,"Administrator\District.html",{"editdata":editdata})

#Admin
    
def adminInsertSelect(request):
    if 'aid' in request.session:
        data=tbl_admin.objects.all()
        if request.method=="POST":
            name=request.POST.get('txtname')
            contact=request.POST.get('txtcontact')
            email=request.POST.get('txtemail')
            password=request.POST.get('txtpassword')
            tbl_admin.objects.create(admin_name=name,admin_contact=contact,admin_email=email,admin_password=password)
            return redirect("Administrator:adminInsertSelect")
        else:
            return render(request,"Administrator/AdminRegistration.html",{'data':data})
    else:
        return redirect("Guest:Login")
    
def delAdmin(request,eid):
    tbl_admin.objects.get(id=eid).delete()
    return redirect("Administrator:adminInsertSelect")

def adminupdate(request,kid):
    editdata=tbl_admin.objects.get(id=kid)
    if request.method=="POST":
        editdata.admin_name=request.POST.get("txtname")
        editdata.admin_contact=request.POST.get("txtcontact")
        editdata.admin_email=request.POST.get("txtemail")
        editdata.admin_password=request.POST.get("txtpassword")
        editdata.save()
        return redirect("Administrator:adminInsertSelect")
    else:
        return render(request,"Administrator\AdminRegistration.html",{"editdata":editdata})

#Category

def categoryInsertSelect(request):
    if 'aid' in request.session:
        cat=tbl_category.objects.all()
        if request.method=="POST":
            categorytype=request.POST.get('txtcategory')
            tbl_category.objects.create(category_name=categorytype)
            return redirect("Administrator:categoryInsertSelect")
        else:
            return render(request,"Administrator/Category.html",{'data':cat})
    else:
        return redirect("Guest:Login")
    
def delCategory(request,cid):
    tbl_category.objects.get(id=cid).delete()
    return redirect("Administrator:categoryInsertSelect")

def categoryupdate(request,fid):
    editdata=tbl_category.objects.get(id=fid)
    if request.method=="POST":
        editdata.category_name=request.POST.get("txtcategory")
        editdata.save()
        return redirect("Administrator:categoryInsertSelect")
    else:
        return render(request,"Administrator\Category.html",{"editdata":editdata})
    
#Brand

def BrandInsertSelect(request):
    if 'aid' in request.session:
        data=tbl_brandname.objects.all()
        if request.method=="POST":
            brandtype=request.POST.get('txtbrand')
            tbl_brandname.objects.create(brand_name=brandtype)
            return redirect("Administrator:BrandInsertSelect")
        else:
            return render(request,"Administrator/Brand.html",{'data':data})
    else:
        return redirect("Guest:Login")
    
def delBrand(request,zid):
    tbl_brandname.objects.get(id=zid).delete()
    return redirect("Administrator:BrandInsertSelect")

def brandupdate(request,xid):
    editdata=tbl_brandname.objects.get(id=xid)
    if request.method=="POST":
        editdata.brand_name=request.POST.get("txtbrand")
        editdata.save()
        return redirect("Administrator:BrandInsertSelect")
    else:
        return render(request,"Administrator\Brand.html",{"editdata":editdata})
    
#Offer
    
def offerInsertSelect(request):
    if 'aid' in request.session:
        data=tbl_offer.objects.all()
        if request.method=="POST":
            name=request.POST.get('txtname')
            fromdate=request.POST.get('txtfromdate')
            todate=request.POST.get('txttodate')
            discription=request.POST.get('txtdiscription')
            tbl_offer.objects.create(offer_name=name,offer_fromdate=fromdate,offer_todate=todate,offer_discription=discription)
            return redirect("Administrator:offerInsertSelect")
        else:
            return render(request,"Administrator/Offer.html",{'data':data})
    else:
        return redirect("Guest:Login")
    
def deloffer(request,pid):
    tbl_offer.objects.get(id=pid).delete()
    return redirect("Administrator:offerInsertSelect")

def offerupdate(request,sid):
    editdata=tbl_offer.objects.get(id=sid)
    if request.method=="POST":
        editdata.offer_name=request.POST.get("txtname")
        editdata.offer_fromdate=request.POST.get("txtfromdate")
        editdata.offer_todate=request.POST.get("txttodate")
        editdata.offer_discription=request.POST.get("txtdiscription")
        editdata.save()
        return redirect("Administrator:offerInsertSelect")
    else:
        return render(request,"Administrator\Offer.html",{"editdata":editdata})
    
#Place
    
def placeInsertSelect(request):
    if 'aid' in request.session:
        district = tbl_district.objects.all()
        data=tbl_place.objects.all()
        if request.method=="POST":
            placeName=request.POST.get('txtname')
            dis = tbl_district.objects.get(id=request.POST.get('sel_district'))
            tbl_place.objects.create(place_name=placeName,district=dis)
            return render(request,"Administrator/Place.html",{'data':data,"districtdata":district})
        else:
            return render(request,"Administrator/Place.html",{'data':data,"districtdata":district})
    else:
        return redirect("Guest:Login")

def delPlace(request,did):
    tbl_place.objects.get(id=did).delete()
    return redirect("Administrator:placeInsertSelect")

def placeupdate(request,eid):
    district = tbl_district.objects.all()
    editdata=tbl_place.objects.get(id=eid)
    if request.method=="POST":
        editdata.place_name=request.POST.get("txtname")
        dis = tbl_district.objects.get(id=request.POST.get('sel_district'))
        editdata.district = dis
        editdata.save()
        return redirect("Administrator:placeInsertSelect")
    else:
        return render(request,"Administrator\Place.html",{"editdata":editdata,"districtdata":district})

#Sub Category
    
def subcategoryInsertSelect(request):
    if 'aid' in request.session:
        category = tbl_category.objects.all()
        data=tbl_subcategory.objects.all()
        if request.method=="POST":
            subcategoryName=request.POST.get('txtname')
            dis = tbl_category.objects.get(id=request.POST.get('sel_category'))
            tbl_subcategory.objects.create(subcategory_name=subcategoryName,category=dis)
            return redirect("Administrator:subcategoryInsertSelect")
        else:
            return render(request,"Administrator/Subcategory.html",{'data':data,"categorydata":category})
    else:
        return redirect("Guest:Login")
    
def delsubcategory(request,tid):
    tbl_subcategory.objects.get(id=tid).delete()
    return redirect("Administrator:subcategoryInsertSelect")

def subcategoryupdate(request,lid):
    category = tbl_category.objects.all()
    editdata=tbl_subcategory.objects.get(id=lid)
    if request.method=="POST":
        editdata.subcategory_name=request.POST.get("txtname")
        dis = tbl_category.objects.get(id=request.POST.get('sel_category'))
        editdata.category = dis
        editdata.save()
        return redirect("Administrator:subcategoryInsertSelect")
    else:
        return render(request,"Administrator\Subcategory.html",{"editdata":editdata,"categorydata":category})
    
#Department

def departmentInsertSelect(request):
    if 'aid' in request.session:
        dog=tbl_department.objects.all()
        if request.method=="POST":
            departmenttype=request.POST.get('txtdepartment')
            tbl_department.objects.create(department_name=departmenttype)
            return redirect("Administrator:departmentInsertSelect")
        else:
            return render(request,"Administrator/Department.html",{'data':dog})
    else:
        return redirect("Guest:Login")
    
def deldepartment(request,jid):
    tbl_department.objects.get(id=jid).delete()
    return redirect("Administrator:departmentInsertSelect")

def departmentupdate(request,vid):
    editdata=tbl_department.objects.get(id=vid)
    if request.method=="POST":
        editdata.department_name=request.POST.get("txtdepartment")
        editdata.save()
        return redirect("Administrator:departmentInsertSelect")
    else:
        return render(request,"Administrator\Department.html",{"editdata":editdata})
    
#Designation

def designationInsertSelect(request):
    if 'aid' in request.session:
        mob=tbl_designation.objects.all()
        if request.method=="POST":
            designationtype=request.POST.get('txtdesignation')
            tbl_designation.objects.create(designation_name=designationtype)
            return redirect("Administrator:designationInsertSelect")
        else:
            return render(request,"Administrator/Designation.html",{'data':mob})
    
    else:
        return redirect("Guest:Login")
    
def deldesignation(request,wid):
    tbl_designation.objects.get(id=wid).delete()
    return redirect("Administrator:designationInsertSelect")

def designationupdate(request,yid):
    editdata=tbl_designation.objects.get(id=yid)
    if request.method=="POST":
        editdata.designation_name=request.POST.get("txtdesignation")
        editdata.save()
        return redirect("Administrator:designationInsertSelect")
    else:
        return render(request,"Administrator\Designation.html",{"editdata":editdata})
    
#Employee
    
def employeeInsertSelect(request):
    if 'aid' in request.session:
        department = tbl_department.objects.all()
        designation = tbl_designation.objects.all()
        data=tbl_employee.objects.all()
        if request.method=="POST":
            employeeName=request.POST.get('txtname')
            employeecontact=request.POST.get('txtcontact')
            employeesalary=request.POST.get('txtsalary')
            deptID = tbl_department.objects.get(id=request.POST.get('sel_department'))
            desigID = tbl_designation.objects.get(id=request.POST.get('sel_designation'))
            tbl_employee.objects.create(employee_name=employeeName,employee_contact=employeecontact,employee_salary=employeesalary,department=deptID,designation=desigID)
            
            return redirect("Administrator:employeeInsertSelect")
        else:
            return render(request,"Administrator/Employee.html",{'data':data,"departmentdata":department,"designationdata":designation})
    else:
        return redirect("Guest:Login")
    
def delemployee(request,oid):
    tbl_employee.objects.get(id=oid).delete()
    return redirect("Administrator:employeeInsertSelect")

def employeeupdate(request,iid):
    department = tbl_department.objects.all()
    designation = tbl_designation.objects.all()
    editdata=tbl_employee.objects.get(id=iid)
    if request.method=="POST":
        editdata.employee_name=request.POST.get("txtname")
        editdata.employee_contact=request.POST.get("txtcontact")
        editdata.employee_salary=request.POST.get("txtsalary")
        deptID= tbl_department.objects.get(id=request.POST.get('sel_department'))
        editdata.department = deptID
        desigID = tbl_designation.objects.get(id=request.POST.get('sel_designation'))
        editdata.designation = desigID
        editdata.save()
        return redirect("Administrator:employeeInsertSelect")
    else:
        return render(request,"Administrator\Employee.html",{"editdata":editdata,"departmentdata":department,"designationdata":designation})
    
#User List

def userList(request):
    if 'aid' in request.session:

        data=tbl_user.objects.all()
        return render(request,"Administrator/UserList.html",{'data':data})
    else:
        return redirect("Guest:Login")

#Seller List

def sellerlist(request):
    if 'aid' in request.session:

        data=tbl_seller.objects.all()
        return render(request,"Administrator/SellerList.html",{'data':data})
    else:
        return redirect("Guest:Login")

#User Verification

def userListNew(request):
    if 'aid' in request.session:

        userdata = tbl_user.objects.filter(user_status=0)
        return render(request,"Administrator/UserListNew.html",{"userdata":userdata})
    else:
        return redirect("Guest:Login")

def acceptuser(request,aid):
    if 'aid' in request.session:

        user = tbl_user.objects.get(id=aid)
        user.user_status = 1
        user.save()
        return redirect("Administrator:LoadingHomePage")
    else:
        return redirect("Guest:Login")

def rejectuser(request,rid):
    if 'aid' in request.session:

        user = tbl_user.objects.get(id=rid)
        user.user_status = 2
        user.save()
        return redirect("Administrator:LoadingHomePage")
    else:
        return redirect("Guest:Login")

def userListAccepted(request):
    if 'aid' in request.session:

        userdata = tbl_user.objects.filter(user_status=1)
        return render(request,"Administrator/UserListAccepted.html",{"userdata":userdata})
    else:
        return redirect("Guest:Login")

def userListRejected(request):
    if 'aid' in request.session:

        userdata = tbl_user.objects.filter(user_status=2)
        return render(request,"Administrator/UserListRejected.html",{"userdata":userdata})
    else:
        return redirect("Guest:Login")

#Seller Verification

def sellerListNew(request):
    if 'aid' in request.session:

        sellerdata = tbl_seller.objects.filter(seller_status=0)
        return render(request,"Administrator/SellerListNew.html",{"sellerdata":sellerdata})
    else:
        return redirect("Guest:Login")

def acceptseller(request,hid):
    if 'aid' in request.session:

        seller = tbl_seller.objects.get(id=hid)
        seller.seller_status = 1
        seller.save()
        return redirect("Administrator:LoadingHomePage")
    else:
        return redirect("Guest:Login")

def rejectseller(request,oid):
    if 'aid' in request.session:

        seller = tbl_seller.objects.get(id=oid)
        seller.seller_status = 2
        seller.save()
        return redirect("Administrator:LoadingHomePage")
    else:
        return redirect("Guest:Login")

def sellerListAccepted(request):
    if 'aid' in request.session:

        sellerdata=tbl_seller.objects.filter(seller_status=1)
        return render(request,"Administrator/SellerListAccepted.html",{"sellerdata":sellerdata})
    else:
        return redirect("Guest:Login")

def sellerListRejected(request):
    if 'aid' in request.session:

        sellerdata = tbl_seller.objects.filter(seller_status=2)
        return render(request,"Administrator/SellerListRejected.html",{"sellerdata":sellerdata})
    else:
        return redirect("Guest:Login")