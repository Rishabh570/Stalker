from django.conf.urls import url
from app import views

app_name = "app"
urlpatterns = [
    url(r'^login/$', views.log_in, name='login'),
    url(r'^logout/$', views.log_out, name='logout'),
    url(r'^signup/$', views.sign_up, name='signup'),
    url(r'^home/$', views.home, name='home'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),

    url(r'^stalk_on_github/$', views.stalk_on_github, name="stalk_on_github"),
    url(r'^github-report/$', views.github_report, name='github-report'),
    url(r'^remove-github/$', views.remove_github, name='remove-github'),

]