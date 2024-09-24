from django.contrib import admin
from .models import Service , Booking, Availability, Review, User, Categories, SliderImage

admin.site.register(Service)
# admin.site.register(ServiceProvider)
admin.site.register(Booking)
admin.site.register(Availability)
admin.site.register(Review)
admin.site.register(User)
admin.site. register(Categories)
admin.site.register(SliderImage)