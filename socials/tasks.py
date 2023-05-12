from celery import shared_task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import time
from .models import *
import json


channel_layer = get_channel_layer()

@shared_task(bind=True)
def obtain_data(request):
    posts = Post.objects.all()
    post_list = []
    for post in posts:
        post_list.append({
        'id': post.id,
        'title': post.title,
        'username': post.owner.username,
        'content': post.content,
        'likes': post.likes,
        # 'comments': [for comment in post.comment.all()]
        'post_image': [image.thumbnail.url for image in post.post_images.all()]
        })
    async_to_sync(channel_layer.group_send('mygroup',{'type':'send_post', 'text':post_list}))
    print('Data Sent')
    
    # post_list = []
    # for post in posts:
    #     post_list.append({
    #     'id': post.id,
    #     'title': post.title,
    #     'username': post.owner.username,
    #     'content': post.content,
    #     'likes': post.likes,
    #     # 'comments': [for comment in post.comment.all()]
    #     'post_image': [image.thumbnail.url for image in post.post_images.all()]
    #     })
    
    



#celery -A mictovic worker --pool=solo -l info