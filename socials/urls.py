from django.contrib import admin
from django.urls import path
from . import views
from .views import PostView,IncrementLikeView
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('inc-like', csrf_exempt(IncrementLikeView.as_view()), name='ajax_like'),
    path('post', PostView.as_view(), name='home'),
    path('ajax-post', csrf_exempt(views.AjaxPost.as_view()), name='ajax_post'),
    path('pagination', csrf_exempt(views.Pagination),name='paginate'),
    path('live-post', csrf_exempt(views.LivePost.as_view()), name='live_post'),
    path('images', csrf_exempt(views.ImagePost.as_view()), name='images'),
    path('details/<int:pk>/', views.details, name='details'),
    path('chat', views.chat,name='chat'),
    path('store', views.store, name='store'),
    # path('upload', views.uploadproduct, name='upload'),
    path('', views.ProductView.as_view(), name='market'),
    # path('', views.Product.as_view(),name='product')
    
]