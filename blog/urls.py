from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.get_posts, name='post_view'),
    path('post/<int:id>/', views.post_detail, name='post_detail_view'),

]