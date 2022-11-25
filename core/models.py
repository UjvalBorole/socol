from django.db import models
from django.contrib.auth import get_user_model
from crum import get_current_user

User = get_user_model()

#Post models
class Post(models.Model):
    text = models.CharField(max_length=140,blank=True,null=True)
    image = models.ImageField(upload_to='post_images')
    user = models.ForeignKey(User, on_delete=models.PROTECT,editable=None)
    created_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.pk)
    
    #this function is used to save the post which the post was created
    def save(self,*args,**kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:     #pk will get at the time the model was built means the data save then get the primary key
            self.user = user
        super(Post,self).save(*args,**kwargs)

#Comment Model
class Comment(models.Model):
    text = models.CharField(max_length=240)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE,editable=None)
    created_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.text)
    
    def save(self,*args,**kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:     #pk will get at the time the model was built means the data save then get the primary key
            self.user = user
        super(Comment,self).save(*args,**kwargs)

#Likes Model
class Like(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE,editable=None)
    is_like = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.is_like)
    
    def save(self,*args,**kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:     #pk will get at the time the model was built means the data save then get the primary key
            self.user = user
        super(Like,self).save(*args,**kwargs)

#Follower Model
class Follow(models.Model):
    user = models.ForeignKey(User,related_name='follow_follower',on_delete=models.CASCADE,editable=None)
    followed = models.ForeignKey(User,related_name="follow_followed",on_delete=models.CASCADE)
    # is_follow = models.BooleanField(default=True)
    followed_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} ---> {self.followed}"
    
    def save(self,*args,**kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:     #pk will get at the time the model was built means the data save then get the primary key
            self.user = user
        super(Follow,self).save(*args,**kwargs)

   
    @property
    def follower_count(self):
        count = self.follow_followed.count()    #it counts the current instance user has how much followings 
        return count
    
    @property
    def following_count(self):
        count= self.follow_follower.count()
        return count
    
    