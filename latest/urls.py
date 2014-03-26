from django.conf.urls import patterns,url

from latest import views


urlpatterns = patterns('',
                       url(r'^$', views.ListGameView.as_view(), name='game-list'),
                       url(r'^new/', views.CreateGameView.as_view(), name='game-new'),
                       url(r'^games/', views.game, name='game'),
                       url(r'^about/$', views.about, name='about'),
                       url(r'^register/', views.register, name='register'),
                       url(r'^login/$', views.user_login, name='login'),
                       url(r'^logout/$', views.user_logout, name='logout'),
                       )
