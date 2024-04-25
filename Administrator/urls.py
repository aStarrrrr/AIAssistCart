from django.contrib import admin
from django.urls import path

from Administrator import views

app_name="Administrator"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('HomePage/', views.LoadingHomePage,name="LoadingHomePage"),

    #District

    path('District/', views.districtInsertSelect,name="districtInsertSelect"),
    path('delDistrict/<int:did>', views.delDistrict,name="delDistrict"),
    path('districtupdate/<int:eid>',views.districtupdate,name="districtupdate"),

    #Admin
   
    path('AdminRegistration/', views.adminInsertSelect,name="adminInsertSelect"),
    path('delAdmin/<int:eid>', views.delAdmin,name="delAdmin"),
    path('adminupdate/<int:kid>',views.adminupdate,name="adminupdate"),
  
    #Category

    path ('Category/', views.categoryInsertSelect,name="categoryInsertSelect"),
    path('delCategory/<int:cid>', views.delCategory,name="delCategory"),
    path('categoryupdate/<int:fid>',views.categoryupdate,name="categoryupdate"),

    #Brand

    path ('Brand/', views.BrandInsertSelect,name="BrandInsertSelect"),
    path('delBrand/<int:zid>', views.delBrand,name="delBrand"),
    path('brandupdate/<int:xid>',views.brandupdate,name="brandupdate"),

    #Offer
   
    path('Offer/', views.offerInsertSelect,name="offerInsertSelect"),
    path('deloffer/<int:pid>', views.deloffer,name="deloffer"),
    path('offerupdate/<int:sid>',views.offerupdate,name="offerupdate"),

    #Place

    path('Place/', views.placeInsertSelect,name="placeInsertSelect"),
    path('delPlace/<int:did>', views.delPlace,name="delPlace"),
    path('placeupdate/<int:eid>',views.placeupdate,name="placeupdate"),

    #Subcategory

    path('Subcategory/', views.subcategoryInsertSelect,name="subcategoryInsertSelect"),
    path('delsubcategory/<int:tid>', views.delsubcategory,name="delsubcategory"),
    path('subcategoryupdate/<int:lid>', views.subcategoryupdate,name="subcategoryupdate"),

    #Deparment

    path ('department/', views.departmentInsertSelect,name="departmentInsertSelect"),
    path('delDepartment/<int:jid>', views.deldepartment,name="deldepartment"),
    path('departmentupdate/<int:vid>',views.departmentupdate,name="departmentupdate"),

    #Designation

    path ('designation/', views.designationInsertSelect,name="designationInsertSelect"),
    path('delDesignation/<int:wid>', views.deldesignation,name="deldesignation"),
    path('designationupdate/<int:yid>',views.designationupdate,name="designationupdate"),

    #Employee

    path('Employee/', views.employeeInsertSelect,name="employeeInsertSelect"),
    path('delemployee/<int:oid>', views.delemployee,name="delemployee"),
    path('employeeupdate/<int:iid>', views.employeeupdate,name="employeeupdate"),

    #User List

    path('UserList/',views.userList,name="newuserInsertSelect"),

    #Seller List

    path('Sellerlist/',views.sellerlist,name="newsellerInsertSelect"),

    #User Verification

    path('UserListNew/',views.userListNew,name="userListNew"),
    path('acceptuser/<int:aid>',views.acceptuser,name="acceptuser"),
    path('rejectuser/<int:rid>',views.rejectuser,name="rejectuser"),
    path('UserListAccepted/',views.userListAccepted,name="userListAccepted"),
    path('UserListRejected/',views.userListRejected,name="userListRejected"),

    #Seller Verification

    path('SellerListNew/',views.sellerListNew,name="sellerListNew"),
    path('acceptseller/<int:hid>',views.acceptseller,name="acceptseller"),
    path('rejectseller/<int:oid>',views.rejectseller,name="rejectseller"),
    path('SellerListAccepted/',views.sellerListAccepted,name="sellerListAccepted"),
    path('SellerListRejected/',views.sellerListRejected,name="sellerListRejected"),

]