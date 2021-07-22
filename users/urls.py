# uers子应用的路由管理
from django.urls import path
from users.views import RegisterView
from users.views import ImageCodeView
from users.views import SmsCodeView
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('imagecode/', ImageCodeView.as_view(), name='imagecode'),
    path('smscode/', SmsCodeView.as_view(), name='smscode'),

]
