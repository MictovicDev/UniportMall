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
        image = images[0]
        details = request.POST.get('text')
        price = request.POST.get('price')
        title = request.POST.get('name')
        product = Product.objects.create(merchant=request.user,
         title=title,
         price=price,
         image=image,
         details=details)

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
        try:
            if data['page'] == 'Next':
                request.session['page'] = request.session['page'] + 1
                print(request.session.get('page'))
                posts = pagination_handler()[request.session['page']-1]
                post_list = []
                post = Post.objects.all()
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
                request.session['posts'] = post_list
                return JsonResponse(post_list, safe=False)
        except KeyError:
            if request.session.get('posts'):
                post_list = request.session.get('posts')
                print(post_list)
                return JsonResponse(post_list, safe=False)
            else:
                post_list = []
                posts = pagination_handler()[0]
                #posts = Post.objects.all()
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
                return JsonResponse(post_list, safe=False)
        return JsonResponse({'content': 'done'})

def Pagination(request):
    data = json.loads(request.body)
    print(request.session.get('page'))
    if data['page'] == 'Previous':
        if request.session.get('page') != 1:
            request.session[page] -= 1
        else:
            page = pagination_handler()[0]
            return JsonResponse({'page': page})
    else:
        request.session['page'] = request.session['page'] + 1
        print(request.session.get('page'))
        posts = pagination_handler()[request.session['page']-1]
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
        print(posts)
        return JsonResponse(post_list,safe=False)

    return JsonResponse({'content': 'Gottten'}) 

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







class PostView(View):
    def get(self, request):
        request.session['posts'] = ''
        save_page =  request.session['page'] = 1
        page = check(request)
        if page == 1:
            posts = pagination_handler()[0]
       # print(posts)
       
        context = {
            'posts' : posts
        }
        return render(request, 'socials/home.html',context)




class IncrementLikeView(View):
    #handling post request for the like views
    def post(self, request):
        #converting the request.body from bytes to python native data types
        data = json.loads(request.body)
        post_id = data.get('id')
        post = Post.objects.get(id=post_id)
        post.likes += 1
        post.save()
        return JsonResponse({'content': 'like added succesfully'}, status=200)



def details(request,pk):
    post = Post.objects.get(id=pk)
    post_images = post.post_images.all()
    first_image = post_images[0].image.url
    comments = Comment.objects.filter(post=post.id)
    print(comments)
    text = request.POST.get('text')
    if request.method == 'POST':
        comment = Comment.objects.create(owner=request.user, post=post, comment=text)
    context = {
        'first_image': first_image,
        'post_images': post_images,
        'post': post,
        'comments' : comments,
    }

    return render(request, 'socials/post_detail.html',context)








def uploadproduct(request):
    pass

def store(request, pk):
    return render(request, 'socials/store.html')



def chat(request):
    return render(request, 'socials/chat.html')