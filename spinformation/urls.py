from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('projects',views.projects,name="projects"),
    path('cheats',views.cheats,name="cheats"),
    path('git',views.git,name="git"),
    path('cdn',views.cdn,name="cdn"),
    path('android',views.android,name="android"),
    path('javascript',views.javascript,name="javascript"),
    path('java',views.java,name="java"),
    path('python',views.python,name="python"),
    path('clang',views.clang,name="clang"),
    path('cplus',views.cplus,name="cplus"),
    path('dsalgo',views.dsalgo,name="dsalgo"),
    path('php',views.php,name="php"),
    path('django',views.django,name="django"),
    path('react',views.react,name="react"),
    path('signup',views.handlesignup,name="handlesignup"),
    path('login',views.handlelogin,name="handlelogin"),
    path('logout',views.handlelogout,name="handlelogout"),
    path('contact',views.contact,name='contact'),




]
