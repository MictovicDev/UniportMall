from django.db import models
from authentication.models import MyUser

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    owner = models.ForeignKey(MyUser, related_name='my_owner', on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    content = models.TextField(null=True)
    likes = models.IntegerField(default=0)
    
    
    

    class Meta:
        ordering = ['-time']
    def __str__(self):
        return self.title



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.comment



class Like(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name="like")

    def __str__(self):
        return f'{self.post.title} has {self.post.likes} likes' 


class PostImage(models.Model):
    image = models.ImageField(upload_to='media/post-images')
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='post_images', blank=True)
    uploaded_time = models.DateTimeField(auto_now_add=True)
    thumbnail = models.FileField(upload_to='media/product-thumbnails', blank=True)

    class Meta:
        ordering = ['-post']


class Chat(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE,related_name='chat_owner')
    receiver = models.ForeignKey(MyUser, on_delete=models.CASCADE,related_name='chat_receiver')

    class Meta:
        ordering = ['-timestamp']


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE,related_name='message',blank=True,default=14)
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='owner')
    receiver = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='receiver')
    body = models.TextField()
    seen = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-time']

    def __str__(self):
        return self.body[0:20]




class Product(models.Model):
    merchant = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=70)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='media/products')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='product', blank=True, null=True)
    details = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumbnail = models.FileField(upload_to='media/product-thumbnails', blank=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title

class OrderedItem(models.Model):
    quantity = models.IntegerField(default=1)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE,)
    product = models.ManyToManyField(Product)
    time_of_order = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} has ordered {self.quantity} of this item"



class Order(models.Model):
    ordered_item = models.ManyToManyField(OrderedItem)
    delivered = models.BooleanField(default=False)
    owner = models.ForeignKey(MyUser, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.owner.username} order"
    



class Store(models.Model):
    owner = models.OneToOneField(MyUser,on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)

    def __str__(self):
        return f"{self.owner.username} Store" 
    




    

