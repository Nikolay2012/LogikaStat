"""LogikaStats URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin 
from django.urls import path

from AppLogikaStats.views import (getBase, getCours, getHome,
                                  getProfile, RegisterUser, LoginView, logoutUser)
from LogikaStats import settings # для работы с медиафайлами в режиме отладки
from django.conf.urls.static import static # импортируем функцию статик для работы проекта
urlpatterns = [
    path('admin/', admin.site.urls),    
    path('home/', getHome, name= 'home'),
    path('mycours/', getCours, name= 'mycours'),
    path('profile/', getProfile, name= 'profile'),
    path('register/', RegisterUser.as_view(), name= 'register'),
    path('', LoginView.as_view(), name= 'login'),
    path('logout/', logoutUser, name='logout')
]
# эта часть кода нужна только для работы в режиме отладки, на сервере уже эта часть прописанна автоматически 
# без этой команды в режиме отладки проект не сможет загружать медиа файлы 
if settings.DEBUG: # проверяем, чтоб значение DEBUG в файле settings.py было = True
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

# handler404 = pageNotFound
