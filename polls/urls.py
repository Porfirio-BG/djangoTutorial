from django.urls import path

from . import views

#When you have multiple apps in one project, you must name the url patterns in this 
#file in order to identify the origin of the url pattern 
app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]