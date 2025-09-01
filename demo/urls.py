"""
URL configuration for demo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from myapp.views import *
from django.conf import settings
from restaurant.views import*
from Student.views import*
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from instagram.views import*


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',myapp,name="myapp"),
    path('',success_page,name="success"),
    path('form/',restaurant_view,name="form"),
    path('Car/',Car_view,name="Car"),
    path('delete-Car/<id>/',delete_Car_view,name='delete_Car_view'),
    path('student/',Student_view,name="student"),
    path('delete-student/<id>/',delete_Student_view,name='delete_Student_view'),
    path('instagram/',instagram,name='instagram'),
    path('logintask/',login_page, name="logintask"),
    path('hello/',hello,name='hello'),
    path('send-email/',send_email_view, name='send_email')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

 
