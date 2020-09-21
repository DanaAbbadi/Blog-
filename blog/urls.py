from .views import HomePageView, ViewPostDetails
from django.urls import path

urlpatterns = [ 
path ('', HomePageView.as_view() , name = 'home'),
path('post/<int:pk>', ViewPostDetails.as_view(), name = 'details')
]
