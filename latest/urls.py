from django.conf.urls import patterns,url

from latest import views

urlpatterns=patterns('',
		url(r'^$',views.index,name='index'),
		url(r'games/',views.game,name='game')
		)
