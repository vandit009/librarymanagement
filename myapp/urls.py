from django.conf.urls import patterns, url
from myapp import views
from myapp import genviews

urlpatterns = patterns('',
        url(r'^$', genviews.IndexView.as_view(),name='index'),
        url(r'^about$', views.about, name='about'),
        url(r'^(?P<course_no>\d{3})$', genviews.DetailView.as_view(), name='detail'),
        url(r'^topics$', views.topics, name='topics'),
        url(r'^addtopic',views.addtopic,name='addtopic'),
        url(r'^topics/(?P<topic_id>\d+)/$', views.topicdetail, name='topicdetail'),
        url(r'^user_logout', views.user_logout, name='user_logout'),
        url(r'^user_login', views.user_login, name='user_login'),
        url(r'^mycourses', views.mycourses, name='mycourses'),
        url(r'^register', views.register, name='register'),
        url(r'^instructor/(?P<id>\d+)/$', views.instructor, name='instructor'),
        url(r'^mystudents', views.mystudents, name='mystudents'),
        )
