from django.contrib import admin
from django.urls import path
from . import views
from .views import PostView,IncrementLikeView
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('inc-like', csrf_exempt(IncrementLikeView.as_view()), name='ajax_like'),
    path('post/<int:pk>/inc-like', csrf_exempt(IncrementLikeView.as_view()), name='ajax_like'),
    path('post', csrf_exempt(PostView.as_view()), name='home'),
    path('ajax-post', csrf_exempt(views.AjaxPost.as_view()), name='ajax_post'),
    path('live-post', csrf_exempt(views.LivePost.as_view()), name='live_post'),
    path('chat/user', csrf_exempt(views.request_user), name='request_user'),
    path('images', csrf_exempt(views.ImagePost.as_view()), name='images'),
    path('post/<int:pk>/', views.postdetails, name='postdetails'),
    path('product/<int:pk>/', views.Productdetails, name='productdetails'),
    path('chat', views.chat,name='chat'),
    path('chat/<int:pk>', views.chatdetail,name='chatdetail'),
    # path('chat/<int:pk>', views.chatdetail,name='chatdetail'),
    path('store', views.store, name='store'),
    # path('upload', views.uploadproduct, name='upload'),
    path('', views.ProductView.as_view(), name='market'),
    
]