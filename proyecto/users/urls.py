from django.urls import path
from users.views import login_request, register,my_profile, delete_account, password_user               
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_request, name='login'),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(template_name = 'users/logout.html'), name='logout'),
    path ('profile/', my_profile, name='my_profile'),
    path('delete_account/', delete_account, name='delete_account'),
    path('password/', password_user, name= 'password_user')
   
    
    
    
]