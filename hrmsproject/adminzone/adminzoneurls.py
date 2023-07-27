from django.conf.urls import url
from  . import views
urlpatterns=[
    url(r'^adminhome',views.adminhome,name='adminhome'),
    url(r'^jobseeker',views.jobseeker,name='jobseeker'),
    url(r'^enquiries',views.enquiries,name='enquiries'),
    url(r'^changepassword',views.changepassword,name='changepassword'),
    url(r'^logout',views.logout,name="logout"),
    url(r'^adminchangepwd',views.adminchangepwd,name='adminchangepwd'),
    url(r'^deleteenquiries/(?P<id>\d+)$',views.deleteenquiries,name='deleteenquiries'),
    url(r'deletejobseekers/(?P<emailid>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$',views.deletejobseekers,name='deletejobseekers'),
    url(r'^addnotification',views.addnotification,name='addnotification'),
    url(r'deletenotification/(?P<id>\d+)$',views.deletenotification,name='deletenotification'),
]
