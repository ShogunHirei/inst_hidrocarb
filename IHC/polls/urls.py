from django.urls import path

from . import views
from .views import FoliumView

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:question_id>/choices/', views.choices, name='choices'),
    path('map_page/', FoliumView.as_view())
    # path('map_page/', views.map_show, name='map')

]
