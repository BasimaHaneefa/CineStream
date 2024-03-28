from datetime import datetime, timezone
from django.shortcuts import render,redirect
from Filmuploader.models import *
from Guest.models import *
from django.db.models import Q
# Create your views here.
def HomePage(request):
    if 'uploaderid'in request.session:
        uploader_name=request.session["upname"]
        return render(request,"Filmuploader/HomePage.html",{'uploader':uploader_name})
    else:
        return redirect("Webguest:Login")    

def MyProfile(request):
    filmupdata=tbl_filmuploader.objects.get(id=request.session['uploaderid'])
    return render(request,"Filmuploader/MyProfile.html",{'uploader':filmupdata})

def EditProfile(request):
    filmupdata=tbl_filmuploader.objects.get(id=request.session['uploaderid'])
    if request.method=="POST":
        filmupdata.uploader_name=request.POST.get("txtname")
        filmupdata.uploader_address=request.POST.get("txtaddress")
        filmupdata.uploader_contact=request.POST.get("txtcno")
        filmupdata.uploader_email=request.POST.get("txtmail")
        filmupdata.save()
        return redirect('webuploader:MyProfile')
    else:
        return render(request,"Filmuploader/EditProfile.html",{'uploader':filmupdata})

def ChangePassword(request):
    if request.method=="POST":
        filmupdata=tbl_filmuploader.objects.get(id=request.session["uploaderid"],uploader_password=request.POST.get("txtpword"))
        cpword=request.POST.get("txtpword2")
        new=request.POST.get("txtpword1")
        if cpword==new:
            filmupdata.uploader_password=request.POST.get("txtpword2")
            filmupdata.save()
            return redirect('webuploader:MyProfile')
        else:
            return render(request,"Filmuploader/ChangePassword.html")
    else:
        return render(request,"Filmuploader/ChangePassword.html")

def UploadFilm(request):
    uploader=tbl_filmuploader.objects.get(id=request.session["uploaderid"])
    upfilmobj=tbl_film.objects.filter(film_uploader=uploader)
    genobj=tbl_genre.objects.all()
    lanObj=tbl_lang.objects.all()
    if request.method=="POST":
        gen=tbl_genre.objects.get(id=request.POST.get('sel_genre'))
        lang=tbl_lang.objects.get(id=request.POST.get('sel_lang'))
        uploader=tbl_filmuploader.objects.get(id=request.session["uploaderid"])
        tbl_film.objects.create(film_title=request.POST.get("txttitle"),
                                film_disc=request.POST.get("txtdisc"),
                                film_duration=request.POST.get("txtduration"),
                                film_poster=request.FILES.get("txtposter"),
                                film_file=request.FILES.get("txtfile"),
                                film_genre=gen,
                                film_lang=lang,
                                film_uploader=uploader)

        return render(request,"Filmuploader/UploadFilm.html",{'gendata':genobj,'updata':upfilmobj})
    else:
        return render(request,"Filmuploader/UploadFilm.html",{'gendata':genobj,'landata':lanObj,'updata':upfilmobj})

def del_film(request,did):
    filmdata=tbl_film.objects.get(id=did).delete()
    return redirect('webuploader:UploadFilm')
       
        
def msglist(request):
    list=tbl_admin.objects.all()
    return render(request,"Filmuploader/Message.html",{'data':list})
        
def chatpage(request,id):
    if 'uploaderid' in request.session:
        admin  = tbl_admin.objects.get(id=id)
        return render(request,"Filmuploader/Chat.html",{"admin":admin})
    else:
        return redirect("Webguest:Login")

def ajaxchat(request):
    file = request.FILES.get("file")
    if file != '':
        if request.POST.get("msg") != '':
            from_uploader = tbl_filmuploader.objects.get(id=request.session["uploaderid"])
            to_admin = tbl_admin.objects.get(id=request.POST.get("tid"))
            print(request.POST.get("tid"))
            tbl_chat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),uploader_from=from_uploader,admin_to=to_admin,chat_file=request.FILES.get("file"))
            return render(request,"Filmuploader/Chat.html")
        else:
            from_uploader = tbl_filmuploader.objects.get(id=request.session["uploaderid"])
            to_admin = tbl_admin.objects.get(id=request.POST.get("tid"))
            print(timezone.now())
            tbl_chat.objects.create(chat_content="",chat_time=datetime.now(),uploader_from=from_uploader,admin_to=to_admin,chat_file=request.FILES.get("file"))
            return render(request,"Filmuploader/Chat.html")
    else:
        from_uploader = tbl_filmuploader.objects.get(id=request.session["uploaderid"])
        to_admin = tbl_admin.objects.get(id=request.POST.get("tid"))
        # print(request.POST.get("tid"))
        print(timezone.now())
        tbl_chat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),uploader_from=from_uploader,admin_to=to_admin,chat_file="")
        return render(request,"Filmuploader/Chat.html")
    
def ajaxchatview(request):
    tid = request.GET.get("tid")
    uploader =tbl_filmuploader.objects.get(id=request.session["uploaderid"])
    chat_data = tbl_chat.objects.filter((Q(uploader_from=uploader) | Q(uploader_to=uploader)) & (Q(admin_from=tid) | Q(admin_to=tid))).order_by('chat_time')
    return render(request,"Filmuploader/ChatView.html",{"data":chat_data,"tid":int(tid)})

def clearchat(request):
    tbl_chat.objects.filter(Q(uploader_from=request.session["uploaderid"]) & Q(admin_to=request.GET.get("tid")) | (Q(admin_from=request.GET.get("tid")) & Q(uploader_to=request.session["uploaderid"]))).delete()
    return render(request,"Filmuploader/ClearChat.html",{"msg":"Chat Deleted Sucessfully...."})

def logout(request):
    if 'uploaderid' in request.session:
        del request.session["uploaderid"]
        return redirect("webguest:Login")
    else:
        return redirect("webguest:Login")


            
