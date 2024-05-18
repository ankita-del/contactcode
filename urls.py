from django.urls import path
from .views import ContactDetailsList

urlpatterns = [
    path('contacts/', ContactDetailsList.as_view(), name='contact-list'),
]
