from django.urls import path
from . import views
urlpatterns = [
    path('', views.printlogin,name='login'),
    path('Login',views.Login,name='login-Success'),
    path('Register',views.Register,name='Register-Success'),
    path('Debit',views.Debit,name='Debit-Success'),
    path('Credit',views.Credit,name='Credit-Success'),
    path('logout',views.logout,name='logout-success'),
    path('log',views.Log,name='Transaction-History'),
]
