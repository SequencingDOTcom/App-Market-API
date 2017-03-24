from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^development_console$', views.dev_console),
    url(r'^genetic_file_retrieval_test$', views.dev_genetic_file_retrieval_test),
    url(r'^job_status_notification_test$', views.dev_job_status_notification_test),
    url(r'^connect_to_sequencing_test$', views.dev_connect_to_test),
]
