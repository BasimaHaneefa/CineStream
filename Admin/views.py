from datetime import datetime, timezone
from django.shortcuts import render ,redirect
from Admin.models import *
from Guest.models import *
from Filmuploader.models import *
from User.models import tbl_complaint,tbl_feedback
from django.db.models import Q
# Create your views here.
def HomePage(request):
    if 'adminid'in request.session:
        admin_name=request.session["aname"]
        return render(request,"Admin/HomePage.html",{'admin':admin_name})
    else:
        return redirect("Webguest:Login")    

def genre(request):
    genobj=tbl_genre.objects.all()
    if request.method=="POST":
        tbl_genre.objects.create(genre_name=request.POST.get("txtgenre"))
        return render(request,"admin/Genre.html",{'data':genobj})
    else:
        return render(request,"admin/Genre.html",{'data':genobj})

def del_genre(request,did):
    gendata=tbl_genre.objects.get(id=did).delete()
    return redirect('webadmin:Genre')

def edt_genre(request,eid):
    gendata=tbl_genre.objects.get(id=eid)
    genobj=tbl_genre.objects.all()
    if request.method=="POST":
        gendata.genre_name=request.POST.get("txtgenre")
        gendata.save()
        return redirect('webadmin:Genre')
    else:
        return render(request,"Admin/Genre.html",{'gdata':gendata,'data':genobj})

def language(request):
    langobj=tbl_lang.objects.all()
    if request.method=="POST":
        tbl_lang.objects.create(lang_name=request.POST.get("txtlang"))
        return render(request,"admin/Language.html",{'data':langobj})
    else:
        return render(request,"admin/Language.html",{'data':langobj})

def del_lang(request,did):
    langdata=tbl_lang.objects.get(id=did).delete()
    return redirect('webadmin:Language')

def edt_lang(request,eid):
    langdata=tbl_lang.objects.get(id=eid)
    langobj=tbl_lang.objects.all()
    if request.method=="POST":
        langdata.lang_name=request.POST.get("txtlang")
        langdata.save()
        return redirect('webadmin:Language')
    else:
        return render(request,"Admin/Language.html",{'ldata':langdata,'data':langobj})     

def filmuploaderverification(request):
    vupobj=tbl_filmuploader.objects.filter(uploader_vstatus=0)
    accepted=tbl_filmuploader.objects.filter(uploader_vstatus=1)
    rejected=tbl_filmuploader.objects.filter(uploader_vstatus=2)
    return render(request,"admin/FilmUploaderVerification.html",{'data':vupobj,'accepted':accepted,'rejected':rejected})



def acc_filmuploaderverification(request,aid):
    accdata=tbl_filmuploader.objects.get(id=aid)
    accdata.uploader_vstatus=1
    accdata.save()
    return redirect('webadmin:New Uploader')

def rej_filmuploaderverification(request,rid):
    rejdata=tbl_filmuploader.objects.get(id=rid)
    rejdata.uploader_vstatus=2
    rejdata.save()
    return redirect('webadmin:New Uploader')

def subscription(request):
    subobj=tbl_subscription.objects.all()
    if request.method=="POST":
        tbl_subscription.objects.create(subscription_plan=request.POST.get("txtplan"),
        subscription_details=request.POST.get("txtdetails"),
        subscription_planamt=request.POST.get("txtamt"))
        return render(request,"admin/Subscription.html",{'data':subobj})
    else:
        return render(request,"admin/Subscription.html",{'data':subobj})

def del_subscription(request,did):
    subdata=tbl_subscription.objects.get(id=did).delete()
    return redirect('webadmin:Subscription')

def edt_subscription(request,eid):
    subdata=tbl_subscription.objects.get(id=eid)
    subobj=tbl_subscription.objects.all()
    if request.method=="POST":
        subdata.subscription_plan=request.POST.get("txtplan")
        subdata.subscription_details=request.POST.get("txtdetails")
        subdata.subscription_planamt=request.POST.get("txtamt")
        subdata.save()
        return redirect('webadmin:Subscription')
    else:
        return render(request,"Admin/Subscription.html",{'sdata':subdata,'data':subobj})

def verifyfilm(request):
    vobj=tbl_film.objects.filter(film_status=0)
    accepted=tbl_film.objects.filter(film_status=1)
    rejected=tbl_film.objects.filter(film_status=2)
    return render(request,"Admin/VerifyFilm.html",{'filmdata':vobj,'filmacc':accepted,'filmrej':rejected})

def acc_film(request,aid):
    accdata=tbl_film.objects.get(id=aid)
    accdata.film_status=1
    accdata.save()
    return redirect('webadmin:VerifyFilm')

def rej_film(request,rid):
    rejdata=tbl_film.objects.get(id=rid)
    rejdata.film_status=2
    rejdata.save()
    return redirect('webadmin:VerifyFilm')

def viewcomplaint(request):
    complaint=tbl_complaint.objects.filter(complaint_status=0)
    rcomplaint=tbl_complaint.objects.filter(complaint_status=1)
    return render(request,"Admin/ViewComplaint.html",{'new':complaint,'reply':rcomplaint})

def viewfeedback(request):
    feed=tbl_feedback.objects.all()
    return render(request,"Admin/ViewFeedback.html",{'feed':feed})

def reply(request,cid):
    com=tbl_complaint.objects.get(id=cid)
    if request.method=="POST":
        com.complaint_reply=request.POST.get("txtreply")
        com.complaint_status=1
        com.save()
        return redirect('webadmin:ViewComplaint')
    else:
        return render(request,"Admin/Reply.html")

def msglist(request):
    list=tbl_filmuploader.objects.filter(uploader_vstatus=1)
    return render(request,"Admin/Message.html",{'data':list})


def chatpage(request,id):
    if 'adminid' in request.session:
        uploader  = tbl_filmuploader.objects.get(id=id)
        return render(request,"Admin/Chat.html",{"uploader":uploader})
    else:
        return redirect("Webguest:Login")

def ajaxchat(request):
    file = request.FILES.get("file")
    if file != '':
        if request.POST.get("msg") != '':
            from_admin = tbl_admin.objects.get(id=request.session["adminid"])
            to_uploader = tbl_filmuploader.objects.get(id=request.POST.get("tid"))
            print(request.POST.get("tid"))
            tbl_chat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),admin_from=from_admin,uploader_to=to_uploader,chat_file=request.FILES.get("file"))
            return render(request,"Admin/Chat.html")
        else:
            from_admin = tbl_admin.objects.get(id=request.session["adminid"])
            to_uploader = tbl_filmuploader.objects.get(id=request.POST.get("tid"))
            print(timezone.now())
            tbl_chat.objects.create(chat_content="",chat_time=datetime.now(),admin_from=from_admin,uploader_to=to_uploader,chat_file=request.FILES.get("file"))
            return render(request,"Admin/Chat.html")
    else:
        from_admin = tbl_admin.objects.get(id=request.session["adminid"])
        to_uploader = tbl_filmuploader.objects.get(id=request.POST.get("tid"))
           # print(request.POST.get("tid"))
        print(timezone.now())
        tbl_chat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),admin_from=from_admin,uploader_to=to_uploader,chat_file="")
        return render(request,"Admin/Chat.html")
    
def ajaxchatview(request):
    tid = request.GET.get("tid")
    admin = tbl_admin.objects.get(id=request.session["adminid"])
    chat_data = tbl_chat.objects.filter((Q(admin_from=admin) | Q(admin_to=admin)) & (Q(uploader_from=tid) | Q(uploader_to=tid))).order_by('chat_time')
    return render(request,"Admin/ChatView.html",{"data":chat_data,"tid":int(tid)})

def clearchat(request):
    tbl_chat.objects.filter(Q(admin_from=request.session["adminid"]) & Q(uploader_to=request.GET.get("tid")) | (Q(uploader_from=request.GET.get("tid")) & Q(admin_to=request.session["adminid"]))).delete()
    return render(request,"Admin/ClearChat.html",{"msg":"Chat Deleted Sucessfully...."})

def logout(request):
    if 'adminid' in request.session:
        del request.session["adminid"]
        return redirect("webguest:Login")
    else:
        return redirect("webguest:Login")


            
