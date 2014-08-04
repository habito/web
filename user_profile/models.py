from django.db import models
from django.contrib.auth.models import User
import datetime
# to display users facebook profile pic
from allauth.socialaccount.models import SocialAccount
<<<<<<< HEAD
import hashlib
=======
>>>>>>> master
from allauth.account.models import EmailAddress

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
<<<<<<< HEAD
    profile_pic = models.ImageField(upload_to='../media/profile_images', default='../media/profile_images/pp.png')
=======
    profile_pic = models.ImageField(upload_to='profile_images', default='profile_images/pp.png')
>>>>>>> master
    phone_number = models.IntegerField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    annual_pay = models.IntegerField(blank=True, null=True)
    
    class Meta:
        db_table = 'user_profile'
    
    def account_verified(self):
        if self.user.is_authenticated:
            result = EmailAddress.objects.filter(email=self.user.email)
            if len(result):
                return result[0].verified
        return False

<<<<<<< HEAD
    def profile_image_url(self):
        fb_uid = SocialAccount.objects.filter(user_id=self.user.id, provider='facebook')
        
        if len(fb_uid):
            return "http://graph.facebook.com/{}/picture?width=40&height=40".format(fb_uid[0].uid)
       
        return "http://www.gravatar.com/avatar/{}?s=40".format(hashlib.md5(self.user.email).hexdigest())
=======
    def profile_image_url(self, dim):
        fb_uid = SocialAccount.objects.filter(user_id=self.user.id, provider='facebook')
        if len(fb_uid):
            return "http://graph.facebook.com/{}/picture?width={:d}&height={:d}".format(fb_uid[0].uid, dim, dim)
        return self.profile_pic

    def __unicode__(self):
        return self.__str__()
>>>>>>> master

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name
        
<<<<<<< HEAD
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
=======
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
>>>>>>> master
