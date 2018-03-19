from django.conf.urls import url
from task import views

urlpatterns =[
	url(r'^$',views.help,name='help'),
]