from django.shortcuts import render,redirect
from Administrator.models import *
from Guest.models import *



def HomePage(request):
    return render(request,"Guest/HomePage.html")

def userRegistration(request):
    district = tbl_district.objects.all()
    if request.method=="POST":
        place = tbl_place.objects.get(id=request.POST.get('sel_place'))
        tbl_user.objects.create(user_name=request.POST.get("txtname"),user_gender=request.POST.get("gender"),user_contact=request.POST.get("txtcontact"),user_email=request.POST.get("txtemail"),user_photo=request.FILES.get("fileImage"),user_proof=request.FILES.get("fileProof"),user_password=request.POST.get("txtpwd"),place=place)
        return redirect("Guest:userRegistration")
    else:
        return render(request,"Guest/NewUser.html",{"districtdata":district})


def ajaxplace(request):
    dis = tbl_district.objects.get(id=request.GET.get("did"))
    place = tbl_place.objects.filter(district=dis)
    return render(request,"Guest/AjaxPlace.html",{"placedata":place})



def sellerRegistration(request):
    district = tbl_district.objects.all()
    if request.method=="POST":
        place = tbl_place.objects.get(id=request.POST.get('sel_place'))
        tbl_seller.objects.create(seller_name=request.POST.get("txtname"),seller_address=request.POST.get("txtaddress"),seller_contact=request.POST.get("txtcontact"),seller_email=request.POST.get("txtemail"),seller_photo=request.FILES.get("fileImage"),seller_proof=request.FILES.get("fileProof"),seller_password=request.POST.get("txtpassword"),place=place)
        return redirect("Guest:sellerRegistration")
    else:
        return render(request,"Guest/NewSeller.html",{"districtdata":district})


def Login(request):
    if request.method == "POST":

        usercount = tbl_user.objects.filter(user_email=request.POST.get("txt_email"),user_password=request.POST.get("txt_password")).count()
        sellercount = tbl_seller.objects.filter(seller_email=request.POST.get("txt_email"),seller_password=request.POST.get("txt_password")).count()
        admincount = tbl_admin.objects.filter(admin_email=request.POST.get("txt_email"),admin_password=request.POST.get("txt_password")).count()

        if usercount > 0:
            user = tbl_user.objects.get(user_email=request.POST.get("txt_email"),user_password=request.POST.get("txt_password"))
            request.session["uid"] = user.id
            request.session["uname"] = user.user_name
            return redirect("User:SearchProduct")
        
        elif sellercount > 0:
            seller = tbl_seller.objects.get(seller_email=request.POST.get("txt_email"),seller_password=request.POST.get("txt_password"))
            request.session["sid"] = seller.id
            request.session["sname"] = seller.seller_name
            return redirect("Seller:homepage")
        
        elif admincount > 0:
            admin = tbl_admin.objects.get(admin_email=request.POST.get("txt_email"),admin_password=request.POST.get("txt_password"))
            request.session["aid"] = admin.id
            request.session["aname"] = admin.admin_name
            return redirect("Administrator:LoadingHomePage")
        
        else:
            return render(request,"Guest/Login.html",{"msg":"Invalid Email Or Password"})
    else:
        return render(request,"Guest/Login.html")