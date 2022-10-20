from django.urls import path

from . import views

# Пространство имен URL
app_name = 'polls'

# Функция path() передает четыре аргумента, два обязательных: route и view, и два необязательных: kwargs и name.
urlpatterns = [
    # /polls/
    path('', views.IndexView.as_view(), name='index'),
    # /polls/5
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # /polls/5/result
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # /polls/5/vote
    path('<int:question_id>/vote/', views.vote, name='vote')

]