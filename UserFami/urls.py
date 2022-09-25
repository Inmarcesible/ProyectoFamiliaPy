from django.contrib.auth.views import LogoutView
from django.urls import path, include
from UserFami.views import * #login_request

urlpatterns = [
    path('login/', login_request, name='UserFamiLogin'),
    path('registro/', register, name='UserFamiRegister'),
    path('logout/', LogoutView.as_view(template_name='UserFami/logout.html'), name='UserFamiLogout'),
]


