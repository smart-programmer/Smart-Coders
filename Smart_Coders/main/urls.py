from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from . import views


urlpatterns = [
    url(r"^$", views.Blogs_query, name="Home"),
    url(r"^Articles/$", views.Article_lists.as_view(), name="Articles_query"),
    url(r"^Articles/(?P<slug>[\w-]+)/(?P<pk>\d+)/$",
        views.Article_obj.as_view(), name="Articles_query_object"),
    url(r"^profile/(?P<slug>[\w-]+)/(?P<pk>\d+)/$",
        views.Article_obj.as_view()),
    url(r"^Articles/(?P<slug>[\w-]+)$", views.Article_lists.as_view()),
    url(r"^(?P<slug>[\w-]+)/(?P<pk>\d+)/$", views.Article_obj.as_view(), name="view_art"),
    url(r"^contact_us/$", views.contact.as_view(), name="contact"),
    url(r'^Login/$', LoginView.as_view(template_name="registration/login_page.html"), name="login"),
    url(r"^AddArticle/$", views.Article_form.as_view(), name="AddArticle"),
    url(r"^profile/$", views.Profile.as_view(), name="profile"),
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),  


]

# ملاحظة: نظام اعادة انشاء كلمة سر مفعل لكن رابط التفعيل يرسل على ال cmd لعدم ربط الخدمة 
# يوزرات المتسجلين في الموقع
#ammar / almowld12
#abdullah / almowld12
#ahmad / almowld123488


#/accounts/profile/
