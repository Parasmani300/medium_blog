from django.urls import path
from django.conf.urls import url
from blog_app import views

app_name = "blog_app"

urlpatterns = [
    path('category/',views.create_category,name='category'),
    path('register/',views.register,name="register"),
    path('user_login/',views.user_login,name='user_login'),
    path('add_post/',views.add_post,name='add_post'),
    url(r'^cat_details/(?P<value>.*?)/$',views.cat_details,name="cat_details"),
    url(r'^post_details/(?P<value>.*?)/$',views.post_details,name="post_details"),
    path('update_profile/',views.update_profile,name="update_profile"),
    path('more_post/',views.more_posts,name="more_post")
]