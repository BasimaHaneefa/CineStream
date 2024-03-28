from datetime import date
from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import *
from Filmuploader.models import *
from User.models import *
from django.http import JsonResponse

# Create your views here.

def HomePage(request):
    if 'userid'in request.session:
        user_name=request.session["usname"]
        return render(request,"User/HomePage.html",{'user':user_name})
    else:
        return redirect("Webguest:Login")    


def MyProfile(request):
    userdata=tbl_user.objects.get(id=request.session['userid'])
    return render(request,"User/MyProfile.html",{'user':userdata})

def EditProfile(request):
    userdata=tbl_user.objects.get(id=request.session['userid'])
    if request.method=="POST":
        userdata.user_name=request.POST.get("txtname")
        userdata.user_email=request.POST.get("txtmail")
        userdata.save()
        return redirect('webuser:MyProfile')
    else:
        return render(request,"User/EditProfile.html",{'user':userdata})

def ChangePassword(request):
    if request.method=="POST":
        userdata=tbl_user.objects.get(id=request.session["userid"],user_password=request.POST.get("txtpword"))
        cpword=request.POST.get("txtpword2")
        new=request.POST.get("txtpword1")
        if cpword==new:
            userdata.user_password=request.POST.get("txtpword2")
            userdata.save()
            return redirect('webuser:MyProfile')
        else:
            return render(request,"User/ChangePassword.html")
    else:
        return render(request,"User/ChangePassword.html")

def searchfilm(request):
    if 'userid' in request.session:
        ar=[1,2,3,4,5]
        genobj=tbl_genre.objects.all()
        langobj=tbl_lang.objects.all()
        filmobj=tbl_film.objects.filter(film_status=1)
        avg_list = []  # Create a list to store average ratings for each car

        reviewcount = 0
        for c in filmobj:
            reviewcount = tbl_review.objects.filter(film=c.id).count()
        # print(reviewcount)
            res = 0
            avg = 0
            review = tbl_review.objects.filter(film=c.id)
            for rev in review:
                res = res + rev.user_rating
            # print(res)
                avg = res//reviewcount
            # print(avg)
            avg_list.append(avg)
        print(avg_list)
        cdata = zip(filmobj,avg_list)
    
        return render(request,"User/SearchFilm.html",{'film':cdata,'gen':genobj,'lan':langobj, "avg": avg_list,"ar":ar})
    else:
        return redirect('webguest:Login')
    
def AjaxFilm(request):
    ar=[1,2,3,4,5]
    avg_list = [] 
    reviewcount = 0
    if (request.GET.get("gid") != "") and (request.GET.get("lanid") != ""):
        genredata=tbl_genre.objects.get(id=request.GET.get("gid"))
        landata = tbl_lang.objects.get(id=request.GET.get("lanid"))
        film=tbl_film.objects.filter(film_genre=genredata,film_lang=landata)
        for c in film:
            reviewcount = tbl_review.objects.filter(film=c.id).count()
        # print(reviewcount)
            res = 0
            avg = 0
            review = tbl_review.objects.filter(film=c.id)
            for rev in review:
                res = res + rev.user_rating
            # print(res)
                avg = res//reviewcount
            # print(avg)
            avg_list.append(avg)
        print(avg_list)
        cdata = zip(film,avg_list)
        return render(request,"User/AjaxFilm.html",{"film":cdata, "avg": avg_list,"ar":ar})
    elif request.GET.get("gid") != "":
        genredata=tbl_genre.objects.get(id=request.GET.get("gid"))
        film=tbl_film.objects.filter(film_genre=genredata)
        for c in film:
            reviewcount = tbl_review.objects.filter(film=c.id).count()
        # print(reviewcount)
            res = 0
            avg = 0
            review = tbl_review.objects.filter(film=c.id)
            for rev in review:
                res = res + rev.user_rating
            # print(res)
                avg = res//reviewcount
            # print(avg)
            avg_list.append(avg)
        print(avg_list)
        cdata = zip(film,avg_list)
        return render(request,"User/AjaxFilm.html",{"film":cdata, "avg": avg_list,"ar":ar})
    else:
        landata = tbl_lang.objects.get(id=request.GET.get("lanid"))
        film=tbl_film.objects.filter(film_lang=landata)
        for c in film:
            reviewcount = tbl_review.objects.filter(film=c.id).count()
        # print(reviewcount)
            res = 0
            avg = 0
            review = tbl_review.objects.filter(film=c.id)
            for rev in review:
                res = res + rev.user_rating
            # print(res)
                avg = res//reviewcount
            # print(avg)
            avg_list.append(avg)
        print(avg_list)
        cdata = zip(film,avg_list)
        return render(request,"User/AjaxFilm.html",{"film":cdata, "avg": avg_list,"ar":ar})
    
def AjaxKey(request):
    key=request.GET.get("word")
    data=tbl_film.objects.filter(film_title__istartswith=key)
    return render(request,"User/AjaxKeyWord.html",{"key":data})

def filmdetails(request,detailid):
    detailobj=tbl_film.objects.filter(id=detailid)
    userdata=tbl_user.objects.get(id=request.session['userid'])
    count=tbl_subscribedplans.objects.filter(user=userdata,subscription_status=1).count()
    return render(request,"User/FilmDetails.html",{'details':detailobj,'count':count})

def wishlist(request,filmid):
    filmobj=tbl_film.objects.get(id=filmid)
    # wishdata=tbl_wishlist.objects.get(id=request.session["userid"])
    user=tbl_user.objects.get(id=request.session["userid"])
    tbl_wishlist.objects.create(
                                    film_id=filmobj,
                                    user_id=user
                                   )
    return redirect('webuser:HomePage')

def dwishlist(request):
    user=tbl_user.objects.get(id=request.session["userid"])
    wishdata=tbl_wishlist.objects.filter(user_id=user)
    return render(request,"User/WishList.html",{'user':wishdata})

def sendcomplaint(request):
    user=tbl_user.objects.get(id=request.session['userid'])
    comobj=tbl_complaint.objects.all()
    if request.method=='POST':
        tbl_complaint.objects.create(complaint_title=request.POST.get("txttitle"),
                                    complaint_content=request.POST.get("txtcomplaint"),
                                    user_id=user)
        return render(request,"User/SendComplaint.html",{'data':comobj})
    else:
        return render(request,"User/SendComplaint.html",{'data':comobj})

def del_complaint(request,cdid):
    comdata=tbl_complaint.objects.get(id=cdid).delete()
    return redirect('webuser:SendComplaint')

def edt_complaint(request,eid):
    comdata=tbl_complaint.objects.get(id=eid)
    comobj=tbl_complaint.objects.all()
    if request.method=="POST":
        comdata.complaint_title=request.POST.get("txttitle")
        comdata.complaint_content=request.POST.get("txtcomplaint")
        comdata.save()
        return redirect('webuser:SendComplaint')
    else:
        return render(request,"User/SendComplaint.html",{'cdata':comdata,'data':comobj})

def sendfeedback(request):
    user=tbl_user.objects.get(id=request.session['userid'])
    feeobj=tbl_feedback.objects.all()
    if request.method=='POST':
        tbl_feedback.objects.create(feedback_content=request.POST.get("txtfeedback"),
                                    user_id=user)
        return render(request,"User/SendFeedback.html",{'data':feeobj})
    else:
        return render(request,"User/SendFeedback.html",{'data':feeobj})

def del_feedback(request,did):
    feedata=tbl_feedback.objects.get(id=did).delete()
    return redirect('webuser:SendFeedback')

def edt_feedback(request,eid):
    feedata=tbl_feedback.objects.get(id=eid)
    feeobj=tbl_feedback.objects.all()
    if request.method=="POST":
        feedata.feedback_content=request.POST.get("txtfeedback")
        feedata.save()
        return redirect('webuser:SendFeedback')
    else:
        return render(request,"User/SendFeedback.html",{'fdata':feedata,'data':feeobj})

def viewsubscription(request):
    subObj=tbl_subscription.objects.all()
    return render(request,"User/ViewSubscription.html",{'sdata':subObj})

def subscribe(request,sid):
    plans=tbl_subscription.objects.get(id=sid)
    userdata=tbl_user.objects.get(id=request.session['userid'])
    tbl_subscribedplans.objects.create(plan=plans,user=userdata,subscription_status=1)
    return redirect("webuser:newpayment")
def viewmysubscription(request):
    userdata=tbl_user.objects.get(id=request.session['userid'])
    mysubdata=tbl_subscribedplans.objects.filter(user=userdata)
    return render(request,"User/ViewMySubscription.html",{'datas':mysubdata})

def renewplan(request,sid):
    mysubdata=tbl_subscribedplans.objects.get(id=sid)
    mysubdata.subscription_startdate=date.today()
    mysubdata.save()
    return redirect("webuser:newpayment")

def newpayment(request):
    userdata = tbl_user.objects.get(id=request.session['userid'])

    latest_subscription = tbl_subscribedplans.objects.filter(user=userdata).latest('id')
    subscribe=latest_subscription.id
    print(subscribe)
    plandata=tbl_subscribedplans.objects.get(id=subscribe)

    if request.method=="POST":
        latest_subscription.payment_status=1
        latest_subscription.save()
        return redirect("webuser:ViewMySubscription")
    else:
        return render(request,"User/Payment.html",{'amnt':plandata})
def wishlistwatch(request,fid):
    wish=tbl_wishlist.objects.get(id=fid)
    filmid=wish.film_id.id
    film=tbl_film.objects.get(id=filmid)
    print(film)
    return render(request,"User/ViewFilm.html",{'film':film})

def watch(request,fid):
    filmdata=tbl_film.objects.get(id=fid)
    userdata=tbl_user.objects.get(id=request.session['userid'])
    tbl_watchedfilm.objects.create(film=filmdata,user=userdata)
    return render(request,"User/ViewFilm.html",{'film':filmdata})

def watched(request):
    userdata=tbl_user.objects.get(id=request.session['userid'])
    filmdata=tbl_watchedfilm.objects.filter(user=userdata)
    return render(request,"User/WatchedList.html",{'film':filmdata})

def rating(request,cid):
    if 'userid' in request.session:
        parray=[1,2,3,4,5]
        cid=cid
        print(cid)
        cdata=tbl_film.objects.get(id=cid)
        wdata=tbl_user.objects.get(id=request.session["userid"])
        counts=0
        counts=stardata=tbl_review.objects.filter(film=cdata).count()
        if counts>0:
            res=0
            stardata=tbl_review.objects.filter(film=cdata).order_by('-review_datetime')
            for i in stardata:
                res = res + int(i.user_rating)
                avg=res//counts  
            return render(request,"User/Rating.html",{"cid":cid,"data":stardata,"ar":parray,"avg":avg,"count":counts})
        else:
            return render(request,"User/Rating.html",{'cid':cid})
    else:
        return redirect("Webguest:Login")

def ajaxrating(request):
    parray=[1,2,3,4,5]
    user_rating=request.GET.get('rating_data')
    user_name=request.GET.get('user_name')
    user_review=request.GET.get('user_review')
    film=request.GET.get('workid')
    cdata=tbl_film.objects.get(id=film)
    cust=tbl_user.objects.get(id=request.session["userid"])
    tbl_review.objects.create(user_name=user_name,user_review=user_review,user_rating=user_rating,film=cdata,user=cust)
    stardata=tbl_review.objects.filter(film=film).order_by('-review_datetime')
    return render(request,"User/AjaxRating.html",{'data':stardata,'ar':parray})

def starrating(request):
    r_len = 0
    five = four = three = two = one = 0
    film_id = request.GET.get("pdt")
    cdata = tbl_film.objects.get(id=film_id)
    rate = tbl_review.objects.filter(film=cdata)

    for i in rate:
        if int(i.user_rating) == 5:
            five += 1
        elif int(i.user_rating) == 4:
            four += 1
        elif int(i.user_rating) == 3:
            three += 1
        elif int(i.user_rating) == 2:
            two += 1
        elif int(i.user_rating) == 1:
            one += 1

        r_len += 1
    #print(r_len)

    rlen = r_len / 5
    #print(rlen)
    result = {"five": five, "four": four, "three": three, "two": two, "one": one, "total_review": rlen}
    return JsonResponse(result)

def logout(request):
    if 'userid' in request.session:
        del request.session["userid"]
        return redirect("webguest:Login")
    else:
        return redirect("webguest:Login")



    
    




