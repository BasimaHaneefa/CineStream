from django.urls import path,include
from Admin import views


app_name="webadmin"


urlpatterns = [
    path('HomePage/',views.HomePage,name="HomePage"),

    path('genre/',views.genre,name="Genre"),
    path('del_genre/<int:did>',views.del_genre,name="Del_genre"),
    path('edt_genre/<int:eid>',views.edt_genre,name="Edt_genre"),

    path('language/',views.language,name="Language"),
    path('del_lang/<int:did>',views.del_lang,name="Del_lang"),
    path('edt_lang/<int:eid>',views.edt_lang,name="Edt_lang"),

    path('New Uploader/',views.filmuploaderverification,name='New Uploader'),
    path('acc_filmuploaderverification/<int:aid>',views.acc_filmuploaderverification,name="acc_filmuploaderverification"),
    path('rej_filmuploaderverification/<int:rid>',views.rej_filmuploaderverification,name="rej_filmuploaderverification"),

    path('Subscription/',views.subscription,name="Subscription"),
    path('del_subscription/<int:did>',views.del_subscription,name="Del_subscription"),
    path('edt_subscription/<int:eid>',views.edt_subscription,name="Edt_subscription"),

    path('VerifyFilm/',views.verifyfilm,name="VerifyFilm"),
    path('acc_film/<int:aid>',views.acc_film,name="acc_film"),
    path('rej_film/<int:rid>',views.rej_film,name="rej_film"),

    path('ViewComplaint/',views.viewcomplaint,name="ViewComplaint"),
    path('viewfeedback/',views.viewfeedback,name="viewfeedback"),

    path('reply/<int:cid>',views.reply,name="reply"),

    path('msglist/',views.msglist,name='msglist'),
    path('chatpage/<int:id>',views.chatpage,name="chatpage"),
    path('ajaxchat/',views.ajaxchat,name="ajaxchat"),
    path('ajaxchatview/',views.ajaxchatview,name="ajaxchatview"),
    path('clearchat/',views.clearchat,name="clearchat"),

    path('logout/',views.logout,name='logout'),
    

    




]
