from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
app_name = 'dbms'

urlpatterns = [
    path('aboutus/',views.about,name='aboutus'),
    path('customer/', views.customer, name='customers'),
    path('contact-us/', views.contact, name='contactus'),
    path('user/<int:id>', views.userpg),
    path('transfer/<int:id>', views.transfer),
    path('success/',views.success,name='success'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
