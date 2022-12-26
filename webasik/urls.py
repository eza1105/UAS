"""webasik URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from MSY.views import*
from userview.views import*
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # URL MSY KEBUTUHAN ADMIN
    path("admin/", admin.site.urls),
    path("adm/", msy, name='adm'),
    path("task/", task, name='task'),
    path("adm/updata/<int:id>",up_data, name='up_data'),
    path("adm/deldata/<int:id>", del_data, name='del_data'),
    path("adm/add_data/", add_data, name='add_data'),

    # LOGIN 
    path("login/", LoginView.as_view(), name='login'),
    path("logout/", LogoutView.as_view(next_page ='user' ), name='logout'),

    # KEBUTUHAN USER 
    path("user/",user, name='user',  ),
    path("table-MSY/", table, name='table'),
    path("chart/", chart, name= 'chart'),
    path("about/", about, name='about'),
    path("fax/",send_fax, name= 'FAX'),
    path('upload/', file_upload, name='upload'),
    path('persebaran/', persebaran, name='persebaran')
]
