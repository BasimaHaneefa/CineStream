from django.urls import path,include
from User import views


app_name="webuser"

urlpatterns = [
    path('HomePage/',views.HomePage,name="HomePage"),
    path('MyProfile/',views.MyProfile,name="MyProfile"),
    path('EditProfile/',views.EditProfile,name="EditProfile"),
    path('ChangePassword/',views.ChangePassword,name='ChangePassword'),

    path('SearchFilm/',views.searchfilm,name='SearchFilm'),
    path('ajaxfilm/',views.AjaxFilm,name="AjaxFilm"),
    path('ajaxkey/',views.AjaxKey,name="AjaxKey"),
    path('FilmDetails/<int:detailid>',views.filmdetails,name='FilmDetails'),
    path('Wishlist/<int:filmid>',views.wishlist,name='Wishlist'),

    path('SendComplaint/',views.sendcomplaint,name='SendComplaint'),
    path('Del_complaint/<int:cdid>',views.del_complaint,name="Del_complaint"),
    path('Edt_complaint/<int:eid>',views.edt_complaint,name="Edt_complaint"),

    path('SendFeedback/',views.sendfeedback,name='SendFeedback'),
    path('Del_feedback/<int:did>',views.del_feedback,name="Del_feedback"),
    path('Edt_feedback/<int:eid>',views.edt_feedback,name="Edt_feedback"),

    path('ViewSubscription/',views.viewsubscription,name="ViewSubscription"),
    path('subscribe/<int:sid>',views.subscribe,name="subscribe"),
    path('newpayment/',views.newpayment,name="newpayment"),

    path('ViewMySubscription/',views.viewmysubscription,name="ViewMySubscription"),
    path('renewplan/<int:sid>',views.renewplan,name="renewplan"),
    path('Viewwishlist/',views.dwishlist,name="Viewwishlist"),
    path('watch/<int:fid>',views.watch,name="watch"),
    path('watched/',views.watched,name="watched"),
    path('wishlistwatch/<int:fid>',views.wishlistwatch,name="wishlistwatch"),
    path('rating/<str:cid>',views.rating,name="rating"),
    path('ajaxrating',views.ajaxrating,name="ajaxrating"),
    path('starrating/',views.starrating,name="starrating"),

    path('logout/',views.logout,name="logout"),
]