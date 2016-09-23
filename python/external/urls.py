from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^sequencing/auth$', views.sequencing_auth),
    url(r'^sequencing/job/register$', views.sequencing_job_register),
    url(r'^sequencing/job/get$', views.sequencing_job_results),
]
