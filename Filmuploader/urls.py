from django.urls import path,include
from Filmuploader import views


app_name="webuploader"

urlpatterns = [
    path('HomePage/',views.HomePage,name="HomePage"),
    path('MyProfile/',views.MyProfile,name="MyProfile"),
    path('EditProfile/',views.EditProfile,name="EditProfile"),
    path('ChangePassword/',views.ChangePassword,name='ChangePassword'),
    path('UploadFilm/',views.UploadFilm,name='UploadFilm'),

    path('del_film/<int:did>',views.del_film,name="Del_film"),

    path('msglist/',views.msglist,name='msglist'),
    
    path('chatpage/<int:id>',views.chatpage,name="chatpage"),
    path('ajaxchat/',views.ajaxchat,name="ajaxchat"),
    path('ajaxchatview/',views.ajaxchatview,name="ajaxchatview"),
    path('clearchat/',views.clearchat,name="clearchat"),

    path('logout/',views.logout,name="logout"),
]