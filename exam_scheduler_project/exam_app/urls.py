from django.conf.urls import url
from exam_app import views

# TEMPLATE TAGGING

app_name = 'exam_app'

urlpatterns= [
    url(r'^course/$',views.course,name='course'),
    url(r'^room/$',views.room,name='room'),
    url(r'^invigilator/$',views.invigilator,name='invigilator'),
    url(r'^schedule/$',views.schedule,name='schedule'),
    url(r'^student/$',views.student,name='student'),
    url(r'^form/$',views.form_name_view,name='form'),
    # url(r'^ajax/load-courses/$', views.load_courses, name='ajax_load_courses'),
]
