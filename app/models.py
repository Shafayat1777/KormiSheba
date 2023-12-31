from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
        email=self.normalize_email(email),
			username=username,
		)

        user.set_password(password)
        user.save(using=self._db)
        return user 
    
    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
            )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


#def get_profile_pic_filepath(self,filepath):
    #return 'profile_pics/' + str(self.pk) + '/profile_pics.png'
        

class Account(AbstractBaseUser):
    email = models.EmailField (verbose_name="email", max_length=60, unique=True)
    username = models.CharField (max_length=30, unique=True)
    date_joined	= models.DateTimeField (verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField (verbose_name='last login', auto_now=True)
    address = models.CharField (max_length=100,default="")
    mobile_number = models.IntegerField(default=0)
    is_admin = models.BooleanField (default=False)
    is_active = models.BooleanField (default=True)
    is_worker = models.BooleanField (default=False)
    is_staff = models.BooleanField (default=False)
    is_superuser = models.BooleanField (default=False)
    profile_pics = models.ImageField(default='default.png',)
    
    working_fields = models.CharField (max_length=20,default="None")
    experience = models.IntegerField(default=0)
    ratings =   models.BigIntegerField(default=0)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

	# For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

	# Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True

    #def get_profile_pics_filename(self):
       # return str(self.profile_pics)[str(self.profile_pics).index('profile_pics/' + str(self.pk) + "/"):]

# my work -------------------
class Services(models.Model):

    seller = models.ForeignKey(Account, default=None, on_delete=models.CASCADE)

    title = models.CharField(max_length=300, null=False)
    category = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=1000, null=True)
    infoOfBuyer = models.CharField(max_length=1000, null=True)
    images = models.ImageField(default='default.png',)
    price = models.IntegerField(default=0)
    deliveryTime = models.IntegerField(default=0)

    







