from django.urls import path
from .views import main_page, by_rubric, create, update, delete


urlpatterns = [
    path('', main_page, name='main_page'),
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('create/', create, name='create'),
    path('<int:pk>/edit/', update, name='update'),
    path('<int:pk>/delete/', delete, name='delete')
]
