from django.urls import path
from .views import YourProfile

app_name = 'yprofile'
urlpatterns = [
    path('<int:user_id>/', YourProfile, name='your_profile'),
    #path('mod/<int:user_id>/', ProfileMod, name='profile_mod'),
]
