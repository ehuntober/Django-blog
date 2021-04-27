from django.urls import path

from .views import (
BlogListView,
BlogUpdateView,
BlogDetailView,
BlogCreateView,
BlogDeleteView,
CommentCreateView, # new
)


urlpatterns = [
path('post/<int:pk>/comment/', CommentCreateView.as_view() ,name='comment'),
path('post/<int:pk>/delete/', # new
BlogDeleteView.as_view(), name='post_delete'),
path('post/new/', BlogCreateView.as_view(), name='post_new'),
path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
path('post/<int:pk>/edit/',
BlogUpdateView.as_view(), name='post_edit'),
path('', BlogListView.as_view(), name='home'),
]


