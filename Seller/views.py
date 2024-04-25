from django.shortcuts import render,redirect
from Guest.models import *
from Seller.models import *
from User.models import *

def homepage(request):
    if 'sid' in request.session:
        return render(request,"Seller/HomePage.html")
    else:
        return redirect("Guest:Login")

def my_pro(request):
    if 'sid' in request.session:
        data=tbl_seller.objects.get(id=request.session["sid"])
        return render(request,"Seller/MyProfile.html",{'data':data})
    else:
        return redirect("Guest:Login")

def editprofile(request):
    if 'sid' in request.session:
        prodata=tbl_seller.objects.get(id=request.session["sid"])
        if request.method=="POST":
            prodata.seller_name=request.POST.get('txtname')
            prodata.seller_contact=request.POST.get('txtcon')
            prodata.seller_email=request.POST.get('txtemail')
            prodata.save()
            return render(request,"Seller/EditProfile.html",{'msg':"Profile Updated"})
        else:
            return render(request,"Seller/EditProfile.html",{'prodata':prodata})
    else:
        return redirect("Guest:Login")

def changepassword(request):
    if 'sid' in request.session:
        if request.method=="POST":
            ccount=tbl_seller.objects.filter(id=request.session["sid"],seller_password=request.POST.get('txtcurpass')).count()
            if ccount>0:
                if request.POST.get('txtnewpass')==request.POST.get('txtconpass'):
                    sellerdata=tbl_seller.objects.get(id=request.session["sid"],seller_password=request.POST.get('txtcurpass'))
                    sellerdata.seller_password=request.POST.get('txtnewpass')
                    sellerdata.save()
                    return render(request,"Seller/ChangePassword.html",{'msg':"Password Updated"})
                else:
                    return render(request,"Seller/ChangePassword.html",{'msg1':"Error in confirm Password"})
            else:
                return render(request,"Seller/ChangePassword.html",{'msg1':"Error in current password"})
        else:
            return render(request,"Seller/ChangePassword.html")
    else:
        return redirect("Guest:Login")
    

#Product

def ajaxsubcategory(request):
    cat = tbl_category.objects.get(id=request.GET.get("did"))
    subcategory = tbl_subcategory.objects.filter(category=cat)
    return render(request,"Seller/AjaxSubcategory.html",{"subcategorydata":subcategory})

def product_details(request):
    if 'sid' in request.session:
        category = tbl_category.objects.all()
        brand = tbl_brandname.objects.all()
        productData=tbl_product.objects.filter(sellerID=request.session["sid"])
        if request.method=="POST":
            subcategory = tbl_subcategory.objects.get(id=request.POST.get('sel_subcategory'))
            brand = tbl_brandname.objects.get(id=request.POST.get('sel_brand'))
            sellerId = tbl_seller.objects.get(id=request.session["sid"])
            tbl_product.objects.create(product_name=request.POST.get("txtname"),product_details=request.POST.get("txtdetails"),product_photo=request.FILES.get("fileImage"),product_price=request.POST.get("txtprice"),subcategory=subcategory,brand=brand,sellerID=sellerId)
            return redirect("Seller:product_details")
        else:
            return render(request,"Seller/Product.html",{"categorydata":category,"branddata":brand,"productdata":productData})
    else:
        return redirect("Guest:Login")

def delproduct(request,oid):
    if 'sid' in request.session:
        tbl_product.objects.get(id=oid).delete()
        return redirect("Seller:product_details")
    else:
        return redirect("Guest:Login")

#Gallery

def product_images(request):
    if 'sid' in request.session:
        category = tbl_category.objects.all()
        gallerydata=tbl_productimages.objects.all()
        if request.method=="POST":
            product = tbl_product.objects.get(id=request.POST.get('sel_product'))
            tbl_productimages.objects.create(product_details=request.POST.get("txtdetails"),productimage_photo=request.FILES.get("fileImage"),product=product)
            return redirect("Seller:product_images")
        else:
            return render(request,"Seller/Gallery.html",{"categorydata":category,"gallerydata":gallerydata})
    else:
        return redirect("Guest:Login")
    
def ajaxproduct(request):
    prdt = tbl_subcategory.objects.get(id=request.GET.get("did"))
    product = tbl_product.objects.filter(subcategory=prdt)
    return render(request,"Seller/Ajaxproduct.html",{"productdata":product})

def logout(request):
    if 'sid' in request.session:
        del request.session["sid"]
        return redirect("Guest:Login")
    else:
        return redirect("Guest:Login")
    
def vieworder(request):
    pdt = tbl_cart.objects.filter(productID__sellerID=request.session["sid"])
    bkids = []
    for i in pdt:
        bkids.append(i.bookingID_id)
    bk = tbl_booking.objects.filter(id__in=bkids)
    return render(request,"Seller/View_orders.html",{"data":bk})

def Myorders(request,mid):
    OrderData=tbl_cart.objects.filter(bookingID=mid)
    return render(request,"Seller/View_product.html",{"data":OrderData})