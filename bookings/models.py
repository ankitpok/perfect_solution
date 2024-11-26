from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.conf import settings

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None):
        user = self.create_user(email, name, password)
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email  # Corrected the method name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='static/service_images', null=True, blank=True)

    def __str__(self):
        return self.name
    
class Category(models.Model):  # Rename to Category for consistency
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='categories')
    name = models.CharField(max_length=255)
    description = models.TextField()
    photo = models.ImageField(upload_to='static/category_images', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    added_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
    

class Booking(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bookings')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='bookings')
    booking_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='bookings', null=True)
    booking_status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    has_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Booking {self.id} by {self.customer.email}"

class Availability(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def _str_(self):
        return f"{self.service_provider.name} - {self.date}"

class Payment(models.Model):
    booking = models.OneToOneField('Booking', on_delete=models.CASCADE, related_name='payment')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _str_(self):
        return f"Payment {self.id} for Booking {self.booking.id}"
    
class SliderImage(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='static/herosection_slider_images/')
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title if self.title else f"Slider Image {self.pk}"
    

class Review(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    review_text = models.TextField(null=False, blank=False)
    rating = models.FloatField(default=0.0) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Review by {self.user_name} - {self.rating} stars'

    # Method to round the rating to nearest 0.5
    def rounded_rating(self):
        return round(self.rating * 2) / 2
