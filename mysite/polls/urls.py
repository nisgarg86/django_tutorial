from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [path('', views.IndexView.as_view(), name='index'),
               path('<int:pk>/details', views.DetailView.as_view(), name='details'),  # ex = polls/5/details
               path('<int:pk>/results', views.ResultView.as_view(), name='results'),
               path('<int:question_id>/vote', views.vote, name='vote')
               ]

