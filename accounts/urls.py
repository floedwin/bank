from django.conf.urls import url
from. import views

from  django.contrib.auth.views import login,logout
urlpatterns =[

    url(r'^$', views.home),
    url(r'^login/$',login,{'template_name':'accounts/login.html'}),
    url(r'^logout/$',logout,{'template_name':'accounts/logout.html'}),
    url(r'^register/$', views.register, name='register'),
    url(r'^RegisterCustomer/$', views.RegisterCustomer, name='RegisterCustomer'),
    url(r'^CustomerBankAccount/$', views.CustomerBankAccount, name='CustomerBankAccount'),
    url(r'^RegisterCustomerTranscations/$', views.RegisterCustomerTranscations, name='RegisterCustomerTranscations'),
    url(r'^about_us/$', views.about_us, name='about_us'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^profile/$', views.view_profile, name='view_profile'),


    ]