# Create your views here.
from django.shortcuts import render,redirect
from django.contrib import messages
from django.core import serializers
from django.http import JsonResponse,HttpResponse
from django.views import View
from socials.models import *
from django.db.models import Prefetch
import json
from django.core.paginator import Paginator

# Create your views here.
#getting data in real time
class AjaxPost(View):
    #handling post request
    def post(self, request):
        #getting all the images sent by the user
        images = request.FILES.getlist('images')
        images = images[0:2]
        print(images)
        #gettting the text
        text = request.POST.get('text')
        print(request.user)
        #creating the post
        post = Post.objects.create(owner=request.user,content=text,title=text[0:5])
        for image in images:
            PostImage.objects.create(post=post, image=image)
        messages.success(request, 'created succesfully')
        return JsonResponse({'content': 'post created succesfully'}, status=200)



class ProductView(View):
    def post(self, request):
        images = request.FILES.getlist('images')
        three_images = images[0:3]
        image = images[0]
        details = request.POST.get('text')
        price = request.POST.get('price')
        title = request.POST.get('name')

        post = Post.objects.create(title=title,
        owner=request.user,
        content=details)

        for image in three_images:
            PostImage.objects.create(post=post, image=image)

        product = Product.objects.create(merchant=request.user,
         title=title,
         price=price,
         image=image,
         details=details,
         post=post)

        return redirect('market')

    def get(self,request):
        products = Product.objects.all()
        context = {
            'products': products
        }
        return render(request,'socials/marketplace.html',context)



        


class LivePost(View):
    def post(self, request):
        data = json.loads(request.body)
        print(data)
        return JsonResponse({'content': 'done'})

class ImagePost(View):
    def get(self, request):
        images = PostImage.objects.all()
        return JsonResponse({'images':list(images.values())})

#handling the pagination for the javascripts with my own pagination algorithm
def pagination_handler():
    posts = Post.objects.all()
    paginated_post = []
    while len(posts) !=0:
        paginated_post.append(posts[0:4])
        posts = posts[4:]
    print(paginated_post)
    return paginated_post

def check(request):
    page = request.session.get('page')
    return page


# def PostView(request):
#     posts = Post.objects.all()
#     context = {
#         'posts' : posts
#     }
#     if request.method == 'POST':
#          data = json.loads(request.body)
#          print(data)
#     return render(request,'socials/home.html',context)





class PostView(View):
    def get(self, request):
        print(request.user.id)
        posts = Post.objects.all()
        context = {
            'posts' : posts
        }
        return render(request, 'socials/home.html',context)
    
    def post(self, request):
        posts = Post.objects.all()
        try:
            data = json.loads(request.body)
            id = data.get('id')
            text = data.get('text')
            post = Post.objects.get(id=id)
            comment = Comment.objects.create(post=post, 
            owner=request.user,
            comment=text)
            comment.save()
            context = {
                'posts' : posts
            }
        except:
            context = {
                'posts' : posts
            }
        return redirect('home')
        
        

       
        
        
        



class IncrementLikeView(View):
    #handling post request for the like views
    def post(self, request):
        #converting the request.body from bytes to python native data types
        data = json.loads(request.body)
        post_id = data.get('id')
        post = Post.objects.get(id=post_id)
        try:
            like = Like.objects.get(post=post, user=request.user)
            if like:
                post.likes -= 1
                like.delete()
                post.save()
        except:
            like = Like.objects.create(post=post, user=request.user)
            post.likes += 1
            post.save()
        return JsonResponse({'content': 'like added succesfully','likes': post.likes}, status=200)



def postdetails(request,pk):
    post = Post.objects.get(id=pk)
    post_images = post.post_images.all()
    first_image = post_images[0].image.url
    comments = Comment.objects.filter(post=post.id)
    if request.method == 'POST':
        text = request.POST.get('text')
        comment = Comment.objects.create(owner=request.user, post=post, comment=text)
    context = {
        'first_image': first_image,
        'post_images': post_images,
        'post': post,
        'comments' : comments,
    }
    return render(request, 'socials/post_detail.html',context)


def Productdetails(request,pk):
    product = Product.objects.get(id=pk)
    context = {
        'product': product
    }

    return render(request, 'socials/productdetail.html',context)






def uploadproduct(request):
    pass

def store(request, pk):
    return render(request, 'socials/store.html')

def chat(request):
    chats = Chat.objects.filter(owner=request.user)
    context = {
        'chats': chats
    }
    return render(request,'socials/chat.html',context)


def chatdetail(request,pk):
    print(request.user)
    chat = Chat.objects.get(owner=request.user, receiver=pk)
    context = {
        'chat': chat
    }
    return render(request, 'socials/chatdetail.html',context)