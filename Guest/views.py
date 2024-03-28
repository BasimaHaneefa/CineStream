from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import *


# Create your views here.

def Main(request):
    return render(request,"Guest/index.html")


def filmuploader(request):
    filmupobj=tbl_filmuploader.objects.all()
    if request.method=="POST":
        confirm=request.POST.get("txtcpword")
        password=request.POST.get("txtpword")
        if confirm == password :
            tbl_filmuploader.objects.create(uploader_name=request.POST.get("txtname"),
        uploader_email=request.POST.get("txtmail"),
        uploader_contact=request.POST.get("txtcno"),
        uploader_address=request.POST.get("txtaddress"),
        uploader_photo=request.FILES.get("txtimg"),
        uploader_proof=request.FILES.get("txtproof"),
        uploader_password=request.POST.get("txtpword"))
            return render(request,"Guest/FilmUploader.html",{'data':filmupobj})
        else:
            msg="Password Missmatch"
            return render(request,"Guest/FilmUploader.html",{'data':filmupobj})
    else:
        return render(request,"Guest/FilmUploader.html",{'data':filmupobj})

def user(request):
    userobj=tbl_user.objects.all()
    if request.method=='POST':
        confirm=request.POST.get("txtcpword")
        password=request.POST.get("txtpword")
        if confirm == password :
            tbl_user.objects.create(user_name=request.POST.get("txtname"),
        user_email=request.POST.get("txtmail"),
        user_photo=request.POST.get("txtimg"),
        user_password=request.POST.get("txtpword"))
            return render(request,"Guest/User.html",{'data':userobj})
        else:
            msg="Password Missmatch"
            return render(request,"Guest/User.html",{'data':userobj})
    else:
        return render(request,"Guest/User.html",{'data':userobj})

def login(request):
    if request.method=="POST":
        email=request.POST.get("txtmail")
        password=request.POST.get("txtpword")
        admincount=tbl_admin.objects.filter(admin_email=email,admin_pword=password).count()
        uploadercount=tbl_filmuploader.objects.filter(uploader_email=email,uploader_password=password,uploader_vstatus=1).count()
        usercount=tbl_user.objects.filter(user_email=email,user_password=password).count()
        if admincount>0:
            admin=tbl_admin.objects.get(admin_email=email,admin_pword=password)
            request.session["adminid"]=admin.id
            request.session["aname"]=admin.admin_name
            return redirect("webadmin:HomePage")

        elif uploadercount>0:
            uploader=tbl_filmuploader.objects.get(uploader_email=email,uploader_password=password)
            request.session["uploaderid"]=uploader.id
            request.session["upname"]=uploader.uploader_name
            return redirect("webuploader:HomePage")

        elif usercount>0:
            user=tbl_user.objects.get(user_email=email,user_password=password)
            request.session["userid"]=user.id
            request.session["usname"]=user.user_name
            return redirect("webuser:HomePage")

        else:
            msg="Invalid Credentials !"
            return render(request,"Guest/Login.html",{'msg':msg})
    else:
        return render(request,"Guest/Login.html")        
